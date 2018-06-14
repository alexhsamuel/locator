import datetime
import flask

from   . import model

#-------------------------------------------------------------------------------

def parse_date(string):
    return datetime.datetime.strptime(string, "%Y-%m-%d").date()


#-------------------------------------------------------------------------------

# This will be set by initialize_db().
# Flask loves globals.  I hate globals.
SESSION = None

API = flask.Blueprint("locator", __name__)

@API.route("/events", methods=["GET"])
def get_events():
    return flask.jsonify({
        "event_id": None,
    })


@API.route("/events", methods=["POST"])
def put_events():
    jso = flask.request.json

    # FIXME: Validate user_id.
    # FIXME: Validate date range.
    # FIXME: Validate status.
    event = model.Event(
        deleted     =False,
        user_id     =jso["user_id"],
        start_date  =parse_date(jso["dates"]["start"]),
        end_date    =parse_date(jso["dates"]["end"]),
        status      =jso["status"],
        notes       =jso.get("notes", ""),
    )

    SESSION.add(event)
    SESSION.commit()

    # FIXME: Return a proper response.
    return flask.jsonify({}), 201


@API.route("/statuses", methods=["GET"])
def get_statuses():
    return flask.jsonify({
        "status": 200,
        "statuses": sorted(flask.current_app.config["statuses"]),
    })


