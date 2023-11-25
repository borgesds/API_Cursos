from flask_restful import Resource
from api import api, jwt  # <========
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services import usuario_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


class LoginList(Resource):
    # busca o usuario para saber qual a importacia dele em is_adimmin(True ou False)
    @jwt.additional_claims_loader
    def add_claims_to_acess_token(identity):
        usuario_token = usuario_service.listar_usuario_id(identity)
        if usuario_token.is_admin:
            roles = 'admin'
        else:
            roles = 'user'

        return {'roles': roles}

    # cadastrar
    def post(self):
        # validar a tipagem do input
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)

        # se tiver erro
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json["email"]
            senha = request.json["senha"]

            # verificar se existe o email
            usuario_bd = usuario_service.listar_usuario_email(email)

            if usuario_bd and usuario_bd.ver_senha(senha):
                access_token = create_access_token(
                    identity=usuario_bd.id,
                    expires_delta=timedelta(seconds=100)
                )

                # recarrega o token
                refresh_token = create_refresh_token(
                    identity=usuario_bd.id
                )

                return make_response(jsonify({
                    'access_taken': access_token,
                    'refresh_token': refresh_token,
                    'message': 'Login realizado com sucesso'
                }), 200)

            return make_response(jsonify({
                'message': 'Credenciais estão invalidas'
            }), 401)


api.add_resource(LoginList, '/login')
