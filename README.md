# UOCIS322 - Project 5 #
Brevet time calculator with MongoDB!

## Overview

You'll add a storage to your previous project using MongoDB and `docker-compose`.
As we discussed, `docker-compose` makes it easier to create, manage and connect multiple container to create a single service comprised of different sub-services.

Presently, there's only a placeholder directory for your Flask app, and a `docker-compose` configuration file. You will copy over `brevets/` from your completed project 4, add a MongoDB service to docker-compose and your Flask app. You will also add two buttons named `Submit` and `Display` to the webpage. `Submit` must store the information (brevet distance, start time, checkpoints and their opening and closing times) in the database (overwriting existing ones). `Display` will fetch the information from the database and fill in the form with them.

Recommended: Review [MongoDB README](MONGODB.md) and[Docker Compose README](COMPOSE.md).

# Tasks

1. Add two buttons `Submit` and `Display` in the ACP calculator page.

	- Upon clicking the `Submit` button, the control times should be inserted into a MongoDB database, and the form should be cleared (reset) **without** refreshing the page.

	- Upon clicking the `Display` button, the entries from the database should be filled into the existing page.

	- Handle error cases appropriately. For example, Submit should return an error if no control times are input. One can imagine many such cases: you'll come up with as many cases as possible.

2. An automated `nose` test suite with at least 2 test cases: at least one for for DB insertion and one for retrieval.

3. Update README.md with brevet control time calculation rules (you were supposed to do this for Project 4), and additional information regarding this project.
	- This project will be peer-reviewed, so be thorough.

# docker-compose.yml

This project consists of us mounting the previous existing project container too an additional database container using `docker compose`
This was done as a way to allow more flexibility in organizing our services, building our image, running our two containers and keeping a
updated list of our data. We build the core components of our service through our `docker-compose.yml`. See configurations in that file for more detail.

# mymongo.py

This module is the interface which allows our communication (fetching and inserting) with our data output in our brevets application to take place.


# flask_brevets.py (Update)

In order to link the communication to our data base from both the back-end to the front-end, two new methods were created.
- `Insert`:
  - Created with an app route directing to our submit button
  - Allows our flask app to insert a brevet object based on its core attributes into our database
- `Fetch`:
  - Created with a flask app route directing our front-end to our display button
  - Enables us to retrieve previous submissions based upon our User-input

# calc.html
Modifications to our previous front end logic incorporated adding two buttons, `Submit` (insert), `Display` (fetch) which allows us to communicate, store and retrieve data based on sending request back to our back-end application.
Two methods located in the javascript were also incorporated to do this, so the functionality of each button works properly.

# Testing
After building our docker container run the following commands to test: 
```
docker compose exec brevets bash
```
This will allow you to enter into the database shell where you can run the following:

```
./run_tests.sh
```
This gives us access to run each nose test with the created script.

### Note:
Source code is heavily documented :)


## UOCIS322 - Project 4 (Recap)
You'll learn how to write test cases and test your code, along with more JQuery.

## Overview

You will reimplement RUSA ACP controle time calculator with Flask and AJAX.
> That's *"controle"* with an *e*, because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

### ACP controle times

This project consists of a web application that is based on RUSA's online calculator. The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). The description is ambiguous, but the examples help. Part of finishing this project is clarifying anything that is not clear about the requirements, and documenting it clearly. 

We are essentially replacing the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data. 

## Implementation

### flask_brevets.py

This module contains our web framework `flask` which we use to listen and receive user-input responses from the front-end (the website) to the back_end where it is run through our algorithm. Initially the file contained the logic to only make a`GET request` when the user inputted/adjusted the km distance for each checkpoint in our race. To solve this issue, following the similar design pattern, two arguments were created: `
* `time_and_date: (the begining start time to our race)` 
* `brevet_distance: (the total amount of distance(km) of the race)` 

Using the `arrow` library which allows us to create a date/time object, I was able to instantiate an arrow object which modified our `time_and_date` argument in the format of `"YYYY-MM-DDTHH:mm"`. This was then sent to acp_times along with the other two arguements `km` and `brevet_distance` for our algorithm to interact with those User inputed features on the website. After this it was then loaded into a JSON object that our JQUERY would be able to accept and send output to our client side of our web server in `calc.html`. 

### calc.html

The AJAX logic was already implemented which allowed our JQuery to implement the functionality for when a km checkpoint was manipulated by the User on the client side. My implementation followed this pattern by creating two varibles that accessed the specific id's for the start time of our interval and the total brevet distance. Once that was found I passed those arguements into our `Ajax` method `$.getJSON` which is used to get the JSON object we passed early and load the results. The variables created in calc.html were used as the values while the keys instantiated in our GET request argument `request.args.get` in `flask_brevets.py` 
were used as the keys. This allowed us to now communicate from end-to-end based on our User's input from the website.

### acp_times.py

#### Background

In order to generate the correct calculations for the opening and closing time of our brevet checkpoints, the following criteria was taken into consideration from the descritiption of the algorithm which can be found in the website link in the above section `acp_control_times`.

#### Algorithm

Following the logic described from the website I created a data structure which contained a dictionary of tuples. Our Key in this dictionary would be our interval distance, which as explained in the website is shown to have varying min/max speeds depending on which threshold is traversed in our total brevet distance; while our value would be that specific intervals max/min speed our racers can go for that specific interval distance. To calcaute the necerssay time I would do the following procedure:
* Create an accumulator `total_time` that we can later convert to hours and minutes based upon the sum of the intervals it traversed

* Create a remainder variable `remaining_distance` that will track the leftover distance.
  * This case occurs when for instance, in a 400km brevet race, we have a checkpoint at 650km. According to the website criteria, to calculate its opening time we would say `200/34 + 200/32 + 200/30 + 50/28` with the divisor being the max time of those specific intervals. This would also be the case for closing time but the divisor being replaced with the minimum speed values. As you may notice, 650 does not divide evenly between each of our interval starting points `(0,200,400,600,1000)` so that leftover distance is automatically divided by the next intervals min/max speed values after the previous interval finishes. Thus, 50 in this case our remainder would be incorporated into the 600-1000 intervals max/min speed rather then the 400-600 max/min speed making it a remainder.

* Iterate through the dictionary of tuples
* Instantiate the min/max to their proper amount depending on if we are calculating the closed time (min) or open time (max)
#### 1st Case:
* If the km distance of the checkpoint minus the interval starting point is a positive integer, we can divide 200/(max or min) speed depending on which time and add it to our accumulator.
  * Having our numerator set to 200 for this check takes care of the sums from the first 3 out of 4 intervals `0-200, 200-400, 400-600` since all of them are a distance of 200 exactly.
#### 2nd Case:
* If that case fails check for the edge case in which our checkpoint distance is in between the range of our first interval `0-200`
  * In this case our checkpoint distance `km` can be the numerator, and we will divide it by the min or max speed of the first interval and add it to our accumulator. Once this is done we can break from our iteration since the total time would be fully accumulated and ready for conversion.
#### 3rd Case:
* Finally, if the previous cases fail we check if our remaining distance is between 1 and 400 since that range covers for all the potential remaining distances we want to calculate. As explained above we will divide the remaining distance by the next interval.
  * Setting the range to 400 solves the case in which our checkpoint distance is 1000 km. On the 4th iteration, 1000 being our subtractor from our checkpoint will fail the first two cases. We can then assume that its remaining distance will be 400 which we will then be able to divide by the `600-1000` max or min speed and then add it to our accumulator.
#### Conclusion:
* After each case is checked, we instantiate `remaining_distance` to be our checkpoint distance minus our interval.
  * `Note:` This variable will be repeatedly overwritten through each iteration. The value stored in it will only be used when the check_point distance fails the first two cases. The remaining distance from our previous interation will thus be our true remaining distance to calculate.

* Once our interation is finished, we will convert our accumulated sum of all the intervals `total_time` to minutes and hours
  * To convert to hours, we take the floor of `total_time` to get the integer of our accumulated sum
  * To convert to minutes, we extract the decimal part of `total_time` and multiply it by 60 since in our integer is originally scaled to hours. We then round it to the nearest minute
* Using the `shift` method from the `arrow` library, we modify are passed in arrow object `brevet_start_time` which stores our original start time and shift by the amount of hours and minutes we calculated based on the steps above. Returning this object gives us our intended opening and closing time.
#### Edge Cases

#### Open Time
* When calculating our opening time, if our checkpoint distance is 0, we can assume that is the starting point, so we just return our original starting time which is stored in `brevet_start_time`
* If our checkpoint distance exceeds the total length of the brevet race, we assume that it will have the same start time to the total distance of the race
  * `For example: 450km checkpoint start_time == 400km total_brevet_distance start_time`

#### Close Time
* Please refer to Oddities section in the link [https://rusa.org/pages/acp-brevet-control-times-calculator#:~:text=The%20algorithm%20used,used%20outside%20France]  to see how closing time is calculated for check points between 0 and 60.
* If our checkpoint distance exceeds the length or is equal to the brevet time we use the exact end time calculations given in the following link to calculate the closing times [https://en.wikipedia.org/wiki/Randonneuring#Time_limits:~:text=specific%20Super%20Randonneur.-,Time%20limits,-%5Bedit%5D]
  * Implementing this case, I used a double hash map data structures (Dictionary of Dictionaries). The initially keys to the main dictionary are the total brevet distances. Our nested dictionary then contains a `"max_time"` key and a value which is the integer/float representation of how long the race should last scaled to hours. This allowed me to consistently access the nested dictionary pair based on which checkpoint distance corresponded to the key.
  From their I could immediately use the nested key to get the total duration value and then modify it to correctly shift by the corresponding minutes and hours (refer to `conclusion` section above to see more details on conversion)

### Testing

A suite of nose test cases is a requirement of this project. Design of the test cases are based on an interpretation of rules here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Use of the official brevet time calculator [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html) was used to increase validity.
See more details in the `README.md` documentation in the test directory.


## Authors
Fedi Aniefuna