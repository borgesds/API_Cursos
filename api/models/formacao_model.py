from api import db
from .professor_model import Professor

# Criação da tabela que vai fazer a ligação entre professor e formacao
professor_formcao = db.Table('professor_formacao',
                             db.Column('professor_id', db.Integer,
                                       db.ForeignKey('professor.id'),
                                       primary_key=True, nullable=False),
                             db.Column('formacao_id', db.Integer,
                                       db.ForeignKey('formacao.id'),
                                       primary_key=True, nullable=False))


# criar tabela
class Formacao(db.Model):
    __tablename__ = 'formacao'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    professores = db.relationship(Professor,
                                  secondary='professor_formacao',  # Faz a ligação com a nova tabela
                                  back_populates='formacoes')  # Onde os dados vão ser puxados
