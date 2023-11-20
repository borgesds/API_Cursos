from flask_restful import Resource
from api import api
from ..schemas import professor_schema
from flask import request, make_response, jsonify
from ..entidades import professor
from ..services import professor_service
from ..paginate import paginate
from ..models.professor_model import Professor
from flask_jwt_extended import jwt_required


class ProfessorList(Resource):
    @jwt_required()
    def get(self):
        # professores = professor_service.listar_professores()
        ps = professor_schema.ProfessorSchema(many=True)
        # return make_response(ps.jsonify(professores), 200)
        return paginate(Professor, ps)

    # cadastrar
    @jwt_required()
    def post(self):
        # validar a tipagem do input
        ps = professor_schema.ProfessorSchema()
        validate = ps.validate(request.json)

        # se tiver erro
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]
            titulo = request.json["titulo"]

            novo_professor = professor.Professor(nome=nome,
                                                 idade=idade,
                                                 titulo=titulo)
            resultado = professor_service.cadatrar_professor(novo_professor)
            x = ps.jsonify(resultado)

            return make_response(x, 201)


class ProfessorDetail(Resource):
    @jwt_required()
    def get(self, id):
        professor = professor_service.listar_professor_id(id)

        if professor is None:
            return make_response(jsonify("Professor não foi encontrado"), 404)

        ps = professor_schema.ProfessorSchema()

        return make_response(ps.jsonify(professor), 200)

    @jwt_required()
    def put(self, id):
        professor_bd = professor_service.listar_professor_id(id)

        if professor_bd is None:
            return make_response(jsonify("Professor não foi encontrado"), 404)

        ps = professor_schema.ProfessorSchema()
        validate = ps.validate(request.json)  # validar os dados

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]
            titulo = request.json["titulo"]

            novo_professor = professor.Professor(nome=nome,
                                                 idade=idade,
                                                 titulo=titulo)

            professor_service.atualiza_professor(professor_bd, novo_professor)
            professor_atualizado = professor_service.listar_professor_id(id)

            return make_response(ps.jsonify(professor_atualizado), 200)

    @jwt_required()
    def delete(self, id):
        professor_bd = professor_service.listar_professor_id(id)

        if professor_bd is None:
            return make_response(jsonify("Professor não foi encontrado"), 404)

        professor_service.remove_professor(professor_bd)

        return make_response(jsonify("Professor excluido com sucesso"), 204)


api.add_resource(ProfessorList, '/professores')
api.add_resource(ProfessorDetail, '/professor/<int:id>')
