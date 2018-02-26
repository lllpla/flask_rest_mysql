from flask_restful import reqparse, Resource, abort

from models import Person, db

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
        person = {'id': person.id,
                  'name': person.name}
        return person

class PersonListView(Resource):

    def get(self):
        person_list = Person.query.order_by(Person.id.desc()).all()
        person_view_list = []
        for person in person_list:
            person_view_list.append({'id': person.id,
                  'name': person.name})
        return person_view_list, 201

    def post(self):
        args = parser.parse_args()
        db_person = Person(args['id'], args['name'])
        db.session.add(db_person)
        db.session.commit()
        person = {'id': db_person.id,
                  'name': db_person.name}
        return person, 201