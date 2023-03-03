"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import logging

import arrow

from acp_times import open_time, close_time

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_brevet_200():
    start_time = arrow.get("2023-02-17T00:00", "YYYY-MM-DDTHH:mm")
    distance = 200
    checkpoint = {
        0: (start_time, start_time.shift(hours=1)),
        30: (start_time.shift(hours=0, minutes=53), start_time.shift(hours=2, minutes=30)),
        100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10, minutes=0)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=30)),
    }

    for km, time_tuple in checkpoint.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, distance, start_time) == checkpoint_open
        assert close_time(km, distance, start_time) == checkpoint_close


def test_brevet_300():
    start_time = arrow.get("2023-02-17T00:00", "YYYY-MM-DDTHH:mm")
    distance = 300
    checkpoint = {
        0: (start_time, start_time.shift(hours=1)),
        23: (start_time.shift(hours=0, minutes=41), start_time.shift(hours=2, minutes=9)),
        60: (start_time.shift(hours=1, minutes=46), start_time.shift(hours=4, minutes=0)),
        125: (start_time.shift(hours=3, minutes=41), start_time.shift(hours=8, minutes=20)),
        210: (start_time.shift(hours=6, minutes=12), start_time.shift(hours=14, minutes=0)),
        300: (start_time.shift(hours=9, minutes=0), start_time.shift(hours=20, minutes=0)),
        4321: (start_time.shift(hours=9, minutes=0), start_time.shift(hours=20, minutes=0))
    }

    for km, time_tuple in checkpoint.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, distance, start_time) == checkpoint_open
        assert close_time(km, distance, start_time) == checkpoint_close


def test_brevet_400():
    start_time = arrow.get("2023-02-17T00:00", "YYYY-MM-DDTHH:mm")
    distance = 400
    checkpoint = {
        0: (start_time, start_time.shift(hours=1)),
        50: (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3, minutes=30)),
        100: (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10, minutes=0)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13, minutes=20)),
        350: (start_time.shift(hours=10, minutes=34), start_time.shift(hours=23, minutes=20)),
        400: (start_time.shift(hours=12, minutes=8), start_time.shift(hours=27, minutes=0))
    }

    for km, time_tuple in checkpoint.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, distance, start_time) == checkpoint_open
        assert close_time(km, distance, start_time) == checkpoint_close


def test_brevet_600():
    start_time = arrow.get("2023-02-17T00:00", "YYYY-MM-DDTHH:mm")
    distance = 600
    checkpoint = {
        0: (start_time, start_time.shift(hours=1)),
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10, minutes=0)),
        300: (start_time.shift(hours=9, minutes=0), start_time.shift(hours=20, minutes=0)),
        450: (start_time.shift(hours=13, minutes=48), start_time.shift(hours=30, minutes=0)),
        601: (start_time.shift(hours=18, minutes=48), start_time.shift(hours=40, minutes=0)),
    }

    for km, time_tuple in checkpoint.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, distance, start_time) == checkpoint_open
        assert close_time(km, distance, start_time) == checkpoint_close


def test_brevet_1000():
    start_time = arrow.get("2023-02-17T00:00", "YYYY-MM-DDTHH:mm")
    distance = 1000
    checkpoint = {
        0: (start_time, start_time.shift(hours=1)),
        39: (start_time.shift(hours=1, minutes=9), start_time.shift(hours=2, minutes=57)),
        234: (start_time.shift(hours=6, minutes=57), start_time.shift(hours=15, minutes=36)),
        545: (start_time.shift(hours=16, minutes=58), start_time.shift(hours=36, minutes=20)),
        690: (start_time.shift(hours=22, minutes=1), start_time.shift(hours=47, minutes=53)),
        804: (start_time.shift(hours=26, minutes=5), start_time.shift(hours=57, minutes=51)),
        922: (start_time.shift(hours=30, minutes=18), start_time.shift(hours=68, minutes=11)),
        1000: (start_time.shift(hours=33, minutes=5), start_time.shift(hours=75, minutes=0)),

    }

    for km, time_tuple in checkpoint.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, distance, start_time) == checkpoint_open
        assert close_time(km, distance, start_time) == checkpoint_close
