import datetime
import flask
import sqlalchemy as sa

from   .model import Event

# FIXME: We keep deleted events (deleted=true) but don't keep revisions of
# patched events.  To do this, we'd have to manage event IDs ourselves rather
# than relying on an autoincrement key.

#-------------------------------------------------------------------------------

class APIError(Exception):

    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code



def jsonify(jso, status_code=200):
    jso = {**jso, "status_code": status_code}
    return flask.jsonify(jso), status_code


def parse_date(string):
    try:
        return datetime.datetime.strptime(string, "%Y-%m-%d").date()
    except ValueError:
        raise APIError(f"invalid date: {string}")


def format_date(date):
    return format(date, "%Y-%m-%d")


def validate_user_id(jso):
    cfg = flask.current_app.config
    try:
        user_id = jso["user_id"]
    except KeyError:
        raise APIError(f"missing user_id")
    if user_id in cfg["users"]:
        return user_id
    else:
        raise APIError(f"unknown user: {user_id}")


def validate_dates(jso):
    try:
        dates = jso["dates"]
    except KeyError:
        raise APIError(f"missing dates")
    sdate = parse_date(dates["start"])
    edate = parse_date(dates["end"])
    if edate >= sdate:
        return sdate, edate
    else:
        raise APIError(f"end date {edate} before start date {sdate}")


def validate_status(jso):
    cfg = flask.current_app.config
    try:
        status = jso["status"]
    except KeyError:
        raise APIError(f"missing status")
    if status in cfg["statuses"]:
        return status
    else:
        raise APIError(f"unknown status: {status}")


def validate_notes(jso):
    try:
        notes = jso["notes"]
    except KeyError:
        raise APIError(f"missing notes")
    if notes is None or isinstance(notes, str):
        return notes
    else:
        raise APIError(f"invalid notes: {notes}")


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


def look_up_event(event_id):
    query = SESSION.query(Event).filter_by(
        deleted=False, 
        event_id=int(event_id)
    )
    try:
        return query.one()
    except sa.orm.exc.NoResultFound:
        raise APIError(f"no event_id: f{event_id}", 404)


#-------------------------------------------------------------------------------

# This will be set by initialize_db().
# Flask loves globals.  I hate globals.
SESSION = None

API = flask.Blueprint("locator", __name__)

@API.errorhandler(APIError)
def handle_invalid_usage(exc):
    return jsonify({"message": exc.message}, exc.status_code)


#-------------------------------------------------------------------------------
# Events

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
            sa.or_( Event.notes.ilike("%" + n + "%") for n in notes ))

    # Fetch and return events.
    events = query.all()
    return jsonify({"events": [ event_to_jso(e) for e in events ]})


@API.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    event = look_up_event(event_id)
    return jsonify({"event": event_to_jso(event)})


@API.route("/events", methods=["POST"])
def put_events():
    jso = flask.request.json

    sdate, edate = validate_dates(jso)
    event = Event(
        deleted     =False,
        user_id     =validate_user_id(jso),
        start_date  =sdate,
        end_date    =edate,
        status      =validate_status(jso),
        notes       =validate_notes(jso),
    )
    SESSION.add(event)
    SESSION.commit()

    return jsonify({"event": event_to_jso(event)}, 201)


@API.route("/events/<event_id>", methods=["PATCH"])
def patch_events(event_id):
    jso     = flask.request.json
    event   = look_up_event(event_id)

    if "user_id" in jso:
        event.user_id = validate_user_id(jso)
    if "dates" in jso:
        event.start_date, event.end_date = validate_dates(jso)
    if "status" in jso:
        event.status = validate_status(jso)
    if "notes" in jso:
        event.notes = validate_notes(jso)
    SESSION.commit()

    return flask.jsonify({"event": event_to_jso(event)})


#-------------------------------------------------------------------------------
# Config

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


