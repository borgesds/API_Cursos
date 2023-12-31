from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..entidades import curso
from ..services import curso_service, formacao_service
from ..paginate import paginate
from ..models.curso_model import Curso
from flask_jwt_extended import jwt_required, get_jwt
from ..decorator import admin_required, api_key_required


class CursoList(Resource):
    @jwt_required()
    # @api_key_required
    def get(self):
        # cursos = curso_service.listar_cursos()
        cs = curso_schema.CursoSchema(many=True)
        # return make_response(cs.jsonify(cursos), 200)
        return paginate(Curso, cs)

    # cadastrar
    # agora chamaos o decorator que nos criasmo para fazer auteticação
    # @jwt_required()
    @admin_required
    def post(self):
        """
        # verificar se o usuario é um admin para ter acesso a esse metodo
        claims = get_jwt()
        if claims['roles'] != 'admin':
            return make_response(
                jsonify(mensagem='Não é permitido esse recurso, só admin!'),
                403
            )
        """

        # validar a tipagem do input
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)

        # se tiver erro
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_publicacao = request.json["data_publicacao"]
            formacao = request.json["formacao"]  # Puxando do curso.py (entidade)

            # Para listar a formação vamos chamar o id que retorna em formacao
            formacao_curso = formacao_service.listar_formacao_id(formacao)

            if formacao_curso is None:
                return make_response(jsonify("Formação não encontrada!!!"), 404)

            novo_curso = curso.Curso(nome=nome,
                                     descricao=descricao,
                                     data_publicacao=data_publicacao,
                                     formacao=formacao_curso)  # Add formacao=formacao_curso
            resultado = curso_service.cadatrar_curso(novo_curso)
            x = cs.jsonify(resultado)

            return make_response(x, 201)


class CursoDetail(Resource):
    @jwt_required()
    def get(self, id):
        curso = curso_service.listar_curso_id(id)

        if curso is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)

        cs = curso_schema.CursoSchema()

        return make_response(cs.jsonify(curso), 200)

    # agora chamaos o decorator que nos criasmo para fazer auteticação
    # @jwt_required()
    @admin_required
    def put(self, id):
        curso_bd = curso_service.listar_curso_id(id)

        if curso_bd is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)

        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)  # validar os dados

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_publicacao = request.json["data_publicacao"]

            formacao = request.json["formacao"]  # Puxando do curso.py (entidade)

            # Para listar a formação vamos chamar o id que retorna em formacao
            formacao_curso = formacao_service.listar_formacao_id(formacao)

            if formacao_curso is None:
                return make_response(jsonify("Formação não encontrada!!!"), 404)

            novo_curso = curso.Curso(nome=nome,
                                     descricao=descricao,
                                     data_publicacao=data_publicacao,
                                     formacao=formacao_curso)  # Add formacao=formacao_curso

            curso_service.atualiza_curso(curso_bd, novo_curso)
            curso_atualizado = curso_service.listar_curso_id(id)

            return make_response(cs.jsonify(curso_atualizado), 200)

    # agora chamaos o decorator que nos criasmo para fazer auteticação
    # @jwt_required()
    @admin_required
    def delete(self, id):
        curso_bd = curso_service.listar_curso_id(id)

        if curso_bd is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)

        curso_service.remove_curso(curso_bd)

        return make_response(jsonify("Curso excluido com sucesso"), 204)


api.add_resource(CursoList, '/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')
