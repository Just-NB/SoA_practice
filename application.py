import os
import logging

from flask import Flask, render_template, request
from flask_restful import Api

from database import base
from database.base import User
from views.menus import news_blueprint
from views.auth import auth_blueprint, kakao_oauth
from rest_server.resource_check import resource_blueprint
from rest_server.resource import TemperatureResource, TemperatureCreationResource, TemperatureByLocationResource
from flask_login import current_user, LoginManager

application = Flask(__name__)
application.register_blueprint(news_blueprint, url_prefix='/news')
application.register_blueprint(auth_blueprint, url_prefix='/auth')
application.register_blueprint(resource_blueprint, url_prefix='/resource')
logging.basicConfig(filename='test.log', level=logging.DEBUG)

api = Api(application)
api.add_resource(TemperatureResource, "/resource/<sensor_id>")
api.add_resource(TemperatureCreationResource, "/resource_creation")
api.add_resource(TemperatureByLocationResource, "/resource_location/<location>")

application.config['WTF_CSRF_SECRET_KEY'] = os.urandom(24)
application.config['SECRET_KEY'] = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(application)

logging.basicConfig(
    filename='test.log',
    level=logging.DEBUG
)


@login_manager.user_loader
def load_user(user_id):
    q = base.db_session.query(User).filter(User.id == user_id)
    user = q.first()
    if user is not None:
        user._authenticated = True
    return user


# @app.route('/')
# def hello_world():
#     logging.error("Root log test")
#     return "<h3>Hello 111  </h3>"
@application.route('/')
def hello_html():
    return render_template(
        'index.html',
        nav_menu='home',
        current_user=current_user
    )


@application.route('/login', methods=['POST', 'GET'])
def success():
    if request.method == 'POST':
        myName = request.form['myName']
    else:
        myName = request.args.get('myName')
    # myName = request.args.get('myName')
    return 'welcome {0}'.format(myName)


@application.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>", 404


if __name__ == '__main__' :
    logging.info('Flask Web Server Started.')
    application.debug = True
    application.run(host='localhost', port ='8080')