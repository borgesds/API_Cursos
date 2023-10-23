from api import db


# criar tabela
class Curso(db.Model):
    __tablename__ = 'curso'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False)
