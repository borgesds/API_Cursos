from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object('config')  # puchando o arquivo config.py

# banco de dados
db = SQLAlchemy(app)
ma = Marshmallow(app)
# config do db
migrate = Migrate(app, db)

api = Api(app)

jwt = JWTManager(app)

from .views import curso_views, formacao_views, professor_views, usuario_views, login_views
from .models import curso_model, formacao_model, professor_model, usuario_model
