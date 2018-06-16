#!/usr/bin/env python

import argparse
import flask
import logging
from   pathlib import Path
import sqlalchemy as sa
import sqlalchemy.orm as orm

import locator.api
import locator.config
import locator.model

DEFAULT_PORT = 11619

#-------------------------------------------------------------------------------

def initialize_db(app, db_path):
    """
    Creates or opens the database, and connects it to the Flask app.

    :return:
      The scoped session object.
    """
    db_path = Path(db_path).absolute()
    logging.info(f"using database: {db_path}")
    engine = sa.create_engine(f"sqlite:///{db_path}")

    session = orm.scoped_session(
        orm.sessionmaker(autocommit=False, autoflush=False, bind=engine))

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        session.remove()

    locator.model.Base.query = session.query_property()
    locator.model.Base.metadata.create_all(engine)

    return session


#-------------------------------------------------------------------------------

logging.basicConfig(
    format  ="%(asctime)s [%(levelname)-7s] %(name)s: %(message)s",
    datefmt ="%Y-%m-%dT%H:%M:%S",
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--database", metavar="PATH", default="./locator.db",
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
args = parser.parse_args()

logging.getLogger().setLevel(logging.INFO)

app = flask.Flask("locator")
app.config.update(locator.config.get_config())
app.register_blueprint(locator.api.API, url_prefix="/api/v1")
locator.api.SESSION = initialize_db(app, args.database)
app.run(host=args.host, port=args.port, debug=args.debug)

