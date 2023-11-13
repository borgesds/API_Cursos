DEBUG = True

USERNAME = 'root'
PASSWORD = 'essaeasenha'
SERVER = 'localhost'
DB = 'bdgeral'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY='aplicacao_flask'
