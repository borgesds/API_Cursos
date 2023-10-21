from flask_restful import Resource
from api import api
from ..schemas import formacao_schema
from flask import request, make_response, jsonify
from ..entidades import formacao
from ..services import formacao_service


class FormacaoList(Resource):
    def get(self):
        formacoes = formacao_service.listar_formacoes()
        fs = formacao_schema.FormacaoSchema(many=True)
        return make_response(fs.jsonify(formacoes), 200)

    # cadastrar
    def post(self):
        # validar a tipagem do input
        fs = formacao_schema.FormacaoSchema()
        validate = fs.validate(request.json)

        # se tiver erro
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]

            nova_formacao = formacao.Formacao(nome=nome,
                                              descricao=descricao)
            resultado = formacao_service.cadatrar_formacao(nova_formacao)
            x = fs.jsonify(resultado)

            return make_response(x, 201)


class FormacaoDetail(Resource):
    def get(self, id):
        formacao = formacao_service.listar_formacao_id(id)

        if formacao is None:
            return make_response(jsonify("Formação não foi encontrado"), 404)

        cs = formacao_schema.FormacaoSchema()

        return make_response(cs.jsonify(formacao), 200)

    def put(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)

        if formacao_bd is None:
            return make_response(jsonify("Formação não foi encontrado"), 404)

        fs = formacao_schema.FormacaoSchema()
        validate = fs.validate(request.json)  # validar os dados

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]

            nova_formacao = formacao.Formacao(nome=nome,
                                              descricao=descricao)

            formacao_service.atualiza_formacao(formacao_bd, nova_formacao)
            formacao_atualizado = formacao_service.listar_formacao_id(id)

            return make_response(fs.jsonify(formacao_atualizado), 200)

    def delete(self, id):
        formacao_bd = formacao_service.listar_curso_id(id)

        if formacao_bd is None:
            return make_response(jsonify("Formação não foi encontrado"), 404)

        formacao_service.remove_formacao(formacao_bd)

        return make_response(jsonify("Formação excluido com sucesso"), 204)


api.add_resource(FormacaoList, '/formacoes')
api.add_resource(FormacaoDetail, '/formacoes/<int:id>')
