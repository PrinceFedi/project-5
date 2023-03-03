""""
Nose tests for pymongo.py
"""

import arrow

import logging

from mymongo import brevets_insert, brevets_fetch

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_insert():
    start_time = arrow.get("2023-01-01 00:00", "YYYY-MM-DD HH:mm")
    brevet_distance = 200
    brevet_checkpoints = [
        {"close": str(start_time.shift(hours=1)), "km": 0, "miles": 0, "location": "", "open": str(start_time),
         },
        {"close": str(start_time.shift(hours=3, minutes=30)), "km": 50, "miles": 31.0686, "location": "",
         "open": str(start_time.shift(hours=1, minutes=28)),
         },
        {"close": str(start_time.shift(hours=6, minutes=40)), "km": 100, "miles": 62.137100, "location": "",
         "open": str(start_time.shift(hours=2, minutes=56)),
         },
        {"close": str(start_time.shift(hours=10)), "km": 150, "miles": 93.205650, "location": "",
         "open": str(start_time.shift(hours=4, minutes=25)),
         },

        {"close": str(start_time.shift(hours=13, minutes=30)), "km": 200, "miles": 124.274200, "location": "",
         "open": str(start_time.shift(hours=5, minutes=53)),
         },
    ]
    brevet_id = brevets_insert(str(start_time), brevet_distance, brevet_checkpoints)
    assert type(brevet_id) == str
    assert brevet_id is not None


def test_fetch():
    start_time = arrow.get("2023-01-01 00:00", "YYYY-MM-DD HH:mm")
    brevet_distance = 200
    brevet_checkpoints = [
        {"close": str(start_time.shift(hours=1)), "km": 0, "miles": 0, "location": "", "open": str(start_time),
         },
        {"close": str(start_time.shift(hours=3, minutes=30)), "km": 50, "miles": 31.0686, "location": "",
         "open": str(start_time.shift(hours=1, minutes=28)),
         },
        {"close": str(start_time.shift(hours=6, minutes=40)), "km": 100, "miles": 62.137100, "location": "",
         "open": str(start_time.shift(hours=2, minutes=56)),
         },
        {"close": str(start_time.shift(hours=10)), "km": 150, "miles": 93.205650, "location": "",
         "open": str(start_time.shift(hours=4, minutes=25)),
         },

        {"close": str(start_time.shift(hours=13, minutes=30)), "km": 200, "miles": 124.274200, "location": "",
         "open": str(start_time.shift(hours=5, minutes=53)),
         },
    ]

    brevets_insert(str(start_time), brevet_distance, brevet_checkpoints)
    db_lists = brevets_fetch()
    print(db_lists)
    assert db_lists == (str(start_time), brevet_distance, brevet_checkpoints)


