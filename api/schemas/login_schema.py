from api import ma
from ..models import usuario_model
from marshmallow import fields


class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario
        load_instance = True
        fields = ('id', 'nome', 'email', 'senha')

    nome = fields.String(required=False)  # Nome não vai ser obrigatorio
    email = fields.String(required=True)
    senha = fields.String(required=True)
