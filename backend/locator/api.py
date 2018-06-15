import datetime
import flask
import sqlalchemy as sa

from   .model import Event

#-------------------------------------------------------------------------------

class APIError(Exception):

    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code



def parse_date(string):
    try:
        return datetime.datetime.strptime(string, "%Y-%m-%d").date()
    except ValueError:
        raise APIError(f"invalid date: {string}")


def format_date(date):
    return format(date, "%Y-%m-%d")


def event_to_jso(event):
    return {
        "event_id"  : str(event.event_id),
        "user_id"   : event.user_id,
        "dates"     : {
            "start" : format_date(event.start_date),
            "end"   : format_date(event.end_date),
        },
        "status"    : event.status,
        "notes"     : event.notes,
    }


#-------------------------------------------------------------------------------

# This will be set by initialize_db().
# Flask loves globals.  I hate globals.
SESSION = None

API = flask.Blueprint("locator", __name__)

@API.errorhandler(APIError)
def handle_invalid_usage(exc):
    response = flask.jsonify({
        "status": exc.status_code,
        "message": exc.message,
    })
    response.status_code = exc.status_code
    return response


@API.route("/events", methods=["GET"])
def get_events():
    cfg = flask.current_app.config
    
    # Start with all undeleted events.
    query = SESSION.query(Event).filter_by(deleted=False)
    args = flask.request.args

    # Apply filters based on query parameters.
    start_date = args.get("start", type=parse_date)
    if start_date is not None:
        query = query.filter(Event.end_date >= start_date)

    end_date = args.get("end", type=parse_date)
    if end_date is not None:
        query = query.filter(Event.start_date <= end_date)

    user_ids = args.getlist("user")
    if len(user_ids) > 0:
        query = query.filter(Event.user_id.in_(user_ids))

    group_ids = args.getlist("group")
    if len(group_ids) > 0:
        # Collect all user IDs in the given groups.
        user_ids = { u for g in group_ids for u in cfg["groups"][g] }
        query = query.filter(Event.user_id.in_(user_ids))

    statuses = args.getlist("status")
    if len(statuses) > 0:
        query = query.filter(Event.status.in_(statuses))

    notes = args.getlist("notes")
    if len(notes) > 0:
        query = query.filter(
            sa.or_( Event.notes.like("%" + n + "%") for n in notes ))

    # Fetch and return events.
    return flask.jsonify({
        "status": 200,
        "events": [ event_to_jso(e) for e in query.all() ],
    })


@API.route("/events", methods=["POST"])
def put_events():
    jso = flask.request.json
    cfg = flask.current_app.config
    
    user_id = jso["user_id"]
    if user_id not in cfg["users"]:
        raise APIError(f"unknown user: {user_id}")

    start_date = parse_date(jso["dates"]["start"])
    end_date = parse_date(jso["dates"]["end"])
    if end_date < start_date:
        raise APIError(f"end date {end_date} before start date {start_date}")
    
    status = jso["status"]
    if status not in cfg["statuses"]:
        raise APIError(f"unknown status: {status}")

    event = Event(
        deleted     =False,
        user_id     =user_id,
        start_date  =start_date,
        end_date    =end_date,
        status      =status,
        notes       =jso.get("notes", ""),
    )
    SESSION.add(event)
    SESSION.commit()

    # FIXME: Return a proper response.
    return flask.jsonify({
        "status": 201,
        "event": event_to_jso(event),
    }), 201


@API.route("/groups", methods=["GET"])
def get_groups():
    groups = flask.current_app.config["groups"]
    return flask.jsonify({
        "status": 200,
        "groups": [
            {
                "group_id": i,
                "user_ids": sorted(g),
            }
            for i, g in groups.items() 
        ],
    })


@API.route("/statuses", methods=["GET"])
def get_statuses():
    return flask.jsonify({
        "status": 200,
        "statuses": sorted(flask.current_app.config["statuses"]),
    })


@API.route("/users", methods=["GET"])
def get_users():
    users = flask.current_app.config["users"]
    return flask.jsonify({
        "status": 200,
        "users": [
            {
                "user_id": i,
            }
            for i in users
        ],
    })


