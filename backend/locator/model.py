import sqlalchemy as sa
from   sqlalchemy.ext.declarative import declarative_base

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



