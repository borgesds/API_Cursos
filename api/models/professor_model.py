from api import db


# criar tabela
class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.integer, nullable=False)
    titulo = db.Column(db.String(50), nullable=True)
