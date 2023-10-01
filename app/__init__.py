from flask import Flask, render_template, request, session
from app.views.api import api

def create_app():
    app = Flask(__name__)
    
    app.config["DOMAIN_NAME"] = "http://localhost:8000"
    app.config['SECRET_KEY'] = "6a900693bc86211512315111254096asd156aw1156125631256da61bc7a8"

    app.register_blueprint(api, url_prefix="/")

    return app

app = create_app()