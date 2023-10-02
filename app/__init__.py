from flask import Flask
from app.views.api import api

def create_app():
    #Create a Flask app object
    app = Flask(__name__)
    #unnecessary config here just to show off 
    app.config["DOMAIN_NAME"] = "http://localhost:8000"
    app.config['SECRET_KEY'] = "6a900693bc86211512315111254096asd156aw1156125631256da61bc7a8"
    #register the API blueprint to have the route start with "/" in our server
    app.register_blueprint(api, url_prefix="/")

    return app

app = create_app()