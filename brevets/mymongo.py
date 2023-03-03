import os

from pymongo import MongoClient

# Set up MongoDB connection
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

# Use database "brevets"
db = client.brevets

# Use collection "lists" in the database
collection = db.lists


def brevets_insert(start_time, brevet_distance, brevet_checkpoints):
    """
    Inserts a new brevet with its three main attributes into the database "brevets-db", under the collection "lists".
    Args:
        start_time:
            (str) The beginning time of our race.
        brevet_distance:
            The maximum distance of our brevet.
        brevet_checkpoints:
            (list) Each km interval and the additional attributes that come with it

    Returns:

    """
    output = collection.insert_one({
        "start_time": start_time,
        "brevet_distance": brevet_distance,
        "brevet_checkpoint": brevet_checkpoints})
    _id = output.inserted_id  # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)


def brevets_fetch():
    """
    Our fetch function which returns our prevision stored submissions in the database
    Returns:
            (list of tuples) Our database table

    """

    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.
    lists = collection.find().sort("_id", -1).limit(1)
    # lists is a PyMongo cursor, which acts like a pointer.
    # We need to iterate through it, even if we know it has only one entry:

    for list_of_brevets in lists:
        # We store all of our lists as documents with three fields:
        # start_time: string # opening time of our race
        # brevet_distance: string  # the max distance of our brevet
        # brevet_checkpoints: list # each checkpoint interval

        return list_of_brevets["start_time"], list_of_brevets["brevet_distance"], list_of_brevets["brevet_checkpoint"]
