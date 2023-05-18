from datetime import datetime

from . import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    memo = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    reviews = db.relationship('Review', back_populates='movie')


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    mark = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(
        db.Integer,
        db.ForeignKey('movie.id', ondelete="CASCADE")
    )
    movie = db.relationship('Movie', back_populates='reviews')
