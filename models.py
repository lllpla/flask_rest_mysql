from flask_sqlalchemy import SQLAlchemy

from apps import app
db = SQLAlchemy(app)

# model
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

    def to_json(self):
        json_person = {
            'id': self.id,
            'name':self.name
        }
        return json_person

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()