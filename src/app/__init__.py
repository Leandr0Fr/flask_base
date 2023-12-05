from flask import Flask
from flask_restx import Api
from .urls import urlpatterns

api = Api()

def create_app():
    app = Flask(__name__)
    api.init_app(app)

    for ns in urlpatterns:
        api.add_namespace(ns)
     
    return app

app = create_app()