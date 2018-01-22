from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A person who wants to workout toward a vacation."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    fname = db.Column(db.String(64), nullable=False)
    lname = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(16),  nullable=False)
    street = db.Column(db.String(64))
    city = db.Column(db.String(64))
    zipcode = db.Column(db.String(5))
    state_code = db.Column(db.String(2), db.ForeignKey("states.state_code"))

    state = db.Relationship("State", backref=db.backref("users"))


class Team(db.Model):
    """A group of people working together toward a vacation."""

    __tablename__ = "teams"

    team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    administrator = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )


class Workout(db.Model):
    """A single workout that a user has done."""

    __tablename__ = "workouts"

    wk_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    evt_id = db.Column(
        db.Integer,
        db.ForeignKey("events.evt_id"),
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    # In meters
    distance = db.Column(db.Float, nullable=False)

    date = db.Column(db.DateTime, nullable=False)

    # In seconds
    duration = db.Column(db.Integer, nullable=False)

    calories = db.Column(db.Integer)
    activity = db.Column(
        db.String(3),
        db.ForeignKey("activities.act_code"),
        nullable=False
    )


class Event(db.Model):
    """An event where a users can work out on a specific day."""

    __tablename__ = "events"

    evt_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    street = db.Column(db.String(64))
    city = db.Column(db.String(64))
    zipcode = db.Column(db.String(5))
    date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text)
    state_code = db.Column(db.String(2), db.ForeignKey("states.state_code"))

    state = db.Relationship("State", backref=db.backref("events"))


class UserTeam(db.Model):
    """An association between a user and a team."""

    __tablename__ = "userteams"

    ut_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    team_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.team_id"),
        nullable=False
    )


class UserEvent(db.Model):
    """An association between a user and an event they plan to do."""

    __tablename__ = "userevents"

    ue_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    # In km
    distance = db.Column(db.Integer)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    evt_id = db.Column(
        db.Integer,
        db.ForeignKey("events.evt_id"),
        nullable=False
    )


class State(db.Model):
    """A state. To be associated with events and users."""

    __tablename__ = "states"

    state_code = db.Column(db.String(2), primary_key=True)
    name = db.Column(db.String(30))


class Activity(db.Model):
    """A category of exercise. To be associated with workouts."""

    __tablename__ = "activities"

    act_code = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    icon = db.Column(db.String(128))
