from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service
from flask_jwt_extended import jwt_required


class UsuarioList(Resource):
    # cadastrar
    def post(self):
        # validar a tipagem do input
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)

        # se tiver erro
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]
            is_admin = request.json["is_admin"]

            novo_usuario = usuario.Usuario(nome=nome,
                                           email=email,
                                           senha=senha,
                                           is_admin=is_admin)

            resultado = usuario_service.cadatrar_usuario(novo_usuario)
            x = us.jsonify(resultado)

            return make_response(x, 201)


api.add_resource(UsuarioList, '/usuario')
