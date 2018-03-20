from flask_restful import  Api
from src.apps import app
from src.views import PersonView, PersonListView
from werkzeug.contrib.fixers import ProxyFix

from src.apps import app, DEV_FLAG
api = Api(app)
api.add_resource(PersonView, '/person/<person_id>')
api.add_resource(PersonListView, '/person')

# Start the flask loop
if __name__ == '__main__':
    if DEV_FLAG:
        app.run()
    else:
        app.wsgi_app = ProxyFix(app.wsgi_app)
        app.run(host='0.0.0.0',port="1111")