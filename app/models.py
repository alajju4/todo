from app import db, app
from datetime import datetime
from time import time



class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectname = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Project {}>'.format(self.name)


class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(50))
	priority = db.Column(db.String(6))
	category = db.Column(db.String(6))
	status = db.Column(db.String(5))
	day_id = db.Column(db.Integer, db.ForeignKey('project.id'))

	def __repr__(self):
		return '<Task {}>'.format(self.name)