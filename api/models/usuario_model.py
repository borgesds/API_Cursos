from api import db
from passlib.hash import pbkdf2_sha256


# criar tabela
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(255), nullable=True)
    is_admin = db.Column(db.Boolean)
    api_key = db.Column(db.String(100), nullable=True)

    # vamos criptografar a senha para enviar ao banco
    def encriptar_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    # verificar qual o formato da senha criptografada
    def ver_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)
