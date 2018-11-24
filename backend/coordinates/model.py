import logging
from   pathlib import Path
import sqlalchemy as sa
from   sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as orm

#-------------------------------------------------------------------------------

Base = declarative_base()

class Event(Base):

    __tablename__ = "events"

    event_id    = sa.Column(sa.Integer,     primary_key=True)
    deleted     = sa.Column(sa.Boolean(),   nullable=False)
    user_id     = sa.Column(sa.String(),    nullable=False)
    start_date  = sa.Column(sa.Date(),      nullable=False)
    end_date    = sa.Column(sa.Date(),      nullable=False)
    status      = sa.Column(sa.String(),    nullable=False)
    notes       = sa.Column(sa.String(),    nullable=True)

    def __repr__(self):
        return (
            self.__class__.__name__
            + "("
            + ", ".join( 
                f"{n}={getattr(self, n)!r}" 
                for n in (
                    "event_id",
                    "deleted",
                    "user_id",
                    "start_date",
                    "end_date",
                    "status",
                    "notes",
                )
            )
            + ")"
        )



#-------------------------------------------------------------------------------

def initialize_db(db_path):
    """
    Creates or opens the database, and sets up the model's global ORM engine.

    :return:
      The scoped session object.
    """
    db_path = Path(db_path).absolute()
    logging.info(f"using database: {db_path}")
    engine = sa.create_engine(f"sqlite:///{db_path}")

    session = orm.scoped_session(
        orm.sessionmaker(autocommit=False, autoflush=False, bind=engine))

    Base.query = session.query_property()
    Base.metadata.create_all(engine)

    return session


