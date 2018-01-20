from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A person who wants to workout toward a vacation."""

    __tablename__ = "users"


class Team(db.Model):
    """A group of people working togethe toward a vacation."""

    __tablename__ = "teams"


class Workout(db.Model):
    """A single workout that a user has done."""

    __tablename__ = "workouts"


class Event(db.Model):
    """An event where a users can work out on a specific day."""

    __tablename__ = "events"


class UserTeam(db.Model):
    """An association between a user and a team."""

    __tablename__ = "userteams"


class UserEvent(db.Model):
    """An association between a user and an event they plan to do."""

    __tablename__ = "userevents"


class State(db.Model):
    """A state. To be associated with events and users."""

    __tablename__ = "states"

    state_code = db.Column(db.String(2), primary_key=True)
    name = db.Column(db.String(30))



