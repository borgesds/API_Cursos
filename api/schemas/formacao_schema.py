from api import ma
from ..models import formacao_model
from marshmallow import fields
from ..schemas import curso_schema, professor_schema


class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    professores = ma.Nested(professor_schema.ProfessorSchema, many=True)  # Retorna os dados de professores

    class Meta:
        model = formacao_model.Formacao
        load_instance = True
        fields = ('id', 'nome', 'descricao', 'cursos', 'professores')

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    # Aqui vamo pegar todos os cursos e listar eles só pelo id e nome
    cursos = fields.List(fields.Nested(curso_schema.CursoSchema, only=('id', 'nome')))
