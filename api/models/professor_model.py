from api import db


# criar tabela
class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(50), nullable=True)
    formacoes = db.relationship("Formacao",  # Como foi criado a relação dentro do formacao_model, fica assim
                                secondary='professor_formacao',  # Faz a ligação com a nova tabela
                                back_populates='professores')  # Onde os dados vão ser puxados
