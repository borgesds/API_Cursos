from api import ma
from ..models import curso_model
from marshmallow import fields


class CursoSchema(ma.SQLAlchemyAutoSchema):
    model = curso_model.Curso
    load_instance = True
    filds = ('id', 'nome', 'descricao', 'data_publicacao')

    nome = filds.String(required=True)
    descricao = filds.String(required=True)
    data_publicacao = filds.Date(required=True)
