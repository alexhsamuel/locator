#!/usr/bin/env python

import argparse
import flask
import logging
import pathlib

import coordinates
import coordinates.api
import coordinates.config
import coordinates.model

DEFAULT_PORT = 11619
DIST_DIR = pathlib.Path(coordinates.__file__).parents[2] / "vue" / "dist"

#-------------------------------------------------------------------------------

logging.basicConfig(
    format  ="%(asctime)s [%(levelname)-7s] %(name)s: %(message)s",
    datefmt ="%Y-%m-%dT%H:%M:%S",
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--database", metavar="PATH", default="./coordinates.db",
    help="use database at PATH")
parser.add_argument(
    "--debug", action="store_true", default=False,
    help="run Flask server with debug and auto reload")
parser.add_argument(
    "--host", metavar="HOST", default="0.0.0.0",
    help="serve on interface HOST [def: all]")
parser.add_argument(
    "--port", metavar="PORT", type=int, default=DEFAULT_PORT,
    help=f"serve on PORT [def: {DEFAULT_PORT}]")
parser.add_argument(
    "config_path", metavar="CFG-FILE", type=pathlib.Path,
    help="load config from JSON CFG-FILE")
args = parser.parse_args()

logging.getLogger().setLevel(logging.INFO)

app = flask.Flask("coordinates")

# Serve the Vue UI.
@app.route("/", methods={"GET"})
def get_ui():
    return flask.send_file(str(DIST_DIR / "index.html"))

@app.route("/css/<path>")
def get_css(path):
    return flask.send_from_directory(str(DIST_DIR / "css"), path)

@app.route("/js/<path>")
def get_js(path):
    return flask.send_from_directory(str(DIST_DIR / "js"), path)

# Serve the REST API.
app.config.update(coordinates.config.load_config(args.config_path))
app.register_blueprint(coordinates.api.API, url_prefix="/api/v1")

# Set up the database session.
session = coordinates.model.initialize_db(args.database)
coordinates.api.SESSION = session

# Close the session when we exit.
@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

# Go.
app.run(host=args.host, port=args.port, debug=args.debug)

