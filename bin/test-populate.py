#!/usr/bin/env python

import argparse
import datetime
import logging
from   random import randint, choice
import requests

DAY         = datetime.timedelta(1)

NUM_EVENTS  = 64
START_DATE  = datetime.date(2018, 1, 1)
END_DATE    = datetime.date(2019, 1, 1)
MAX_LENGTH  = 14

WORDS = [
    "piquant", "drip", "moldy", "repeat", "tin", "classy", "zip", "join", 
    "pencil", "hate", "ready", "tip", 
]

logging.basicConfig(
    level   =logging.INFO,
    format  ="%(asctime)s [%(levelname)-7s] %(name)s: %(message)s",
    datefmt ="%Y-%m-%dT%H:%M:%S",
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--host", metavar="HOST", default="localhost",
    help="serve on interface HOST [def: localhost]")
parser.add_argument(
    "--port", metavar="PORT", type=int, default=11619,
    help=f"serve on PORT [def: 11619]")
args = parser.parse_args()

url = f"http://{args.host}:{args.port}/api/v1"

rsp = requests.get(f"{url}/statuses")
rsp.raise_for_status()
statuses = rsp.json()["statuses"]

rsp = requests.get(f"{url}/users")
rsp.raise_for_status()
user_ids = [ u["user_id"] for u in rsp.json()["users"] ]

for _ in range(NUM_EVENTS):
    start_date = START_DATE + DAY * randint(0, (END_DATE - START_DATE).days)
    end_date = start_date + DAY * randint(1, MAX_LENGTH)
    notes = None if randint(0, 1) else " ".join( choice(WORDS) for _ in range(randint(3, 8)) )
    rsp = requests.post(
        f"{url}/events", 
        json={
            "user_id": choice(user_ids),
            "dates": {
                "start": str(start_date),
                "end": str(end_date),
            },
            "status": choice(statuses),
            "notes": notes,
        },
    )
    rsp.raise_for_status()
    event = rsp.json()["event"]
    logging.info(f"created event {event['event_id']}")


