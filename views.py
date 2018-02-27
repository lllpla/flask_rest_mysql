from flask_restful import reqparse, Resource, abort
from sqlalchemy.exc import IntegrityError

from models import Person

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')

# modelView
class PersonView(Resource):

    def get(self,person_id):
        person = None
        try:
            person = Person.query.filter(Person.id == person_id).one()
        except Exception as e:
            abort(404, message="person {} doesn't exist".format(person_id))
        return person.to_json()

class PersonListView(Resource):

    def get(self):
        person_list = Person.query.order_by(Person.id.desc()).all()
        person_view_list = []
        for person in person_list:
            person_view_list.append(person.to_json())
        return person_view_list, 201

    def post(self):
        args = parser.parse_args()
        person = Person(args['id'], args['name'])
        try:
            person.save()
        except IntegrityError as e:
            abort(500, error="{}".format(e.args[0]),code=500)
        return person.to_json(), 201