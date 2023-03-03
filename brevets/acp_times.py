"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import math

#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#
INTERVAL_SPEEDS = {200: (34, 15), 400: (32, 15), 600: (30, 15), 1000: (28, 11.428)}

RACE_DURATION = {200: {"max_time": 13.5}, 300: {"max_time": 20}, 400: {"max_time": 27}, 600: {"max_time": 40},
                 1000: {"max_time": 75}, }


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km <= 0:
        return brevet_start_time

    if control_dist_km >= brevet_dist_km:
        control_dist_km = brevet_dist_km

    total_time = 0
    remaining_distance = 0
    for km, l in INTERVAL_SPEEDS.items():
        (max, min) = l
        if control_dist_km - km > 0:
            total_time += 200 / max
        elif control_dist_km <= 200:
            total_time += control_dist_km / max
            break
        elif 0 < remaining_distance <= 400:
            total_time += remaining_distance / max
        remaining_distance = control_dist_km - km

    minutes = round((total_time % 1) * 60)
    hours = math.floor(total_time)

    return brevet_start_time.shift(hours=hours, minutes=minutes)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km <= 60:
        if control_dist_km == 0:
            return brevet_start_time.shift(hours=1)
        total_time = control_dist_km / 20
        hours = (math.floor(total_time) + 1)
        minutes = round((total_time % 1) * 60)
        return brevet_start_time.shift(hours=hours, minutes=minutes)

    if control_dist_km >= brevet_dist_km:
        time = RACE_DURATION[brevet_dist_km]
        return brevet_start_time.shift(hours=math.floor(time["max_time"]), minutes=round((time["max_time"] % 1) * 60))

    total_time = 0
    remaining_distance = 0
    for km, l in INTERVAL_SPEEDS.items():
        (max, min) = l
        if control_dist_km - km > 0:
            total_time += 200 / min
        elif control_dist_km <= 200:
            total_time += control_dist_km / min
            break
        elif 0 < remaining_distance <= 400:
            total_time += remaining_distance / min
        remaining_distance = control_dist_km - km

    minutes = round((total_time % 1) * 60)
    hours = math.floor(total_time)

    return brevet_start_time.shift(hours=hours, minutes=minutes)
