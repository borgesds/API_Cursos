from ..models import usuario_model
from api import db


def cadatrar_usuario(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome,
                                       email=usuario.email,
                                       senha=usuario.senha)
    # codificar a senha
    usuario_bd.encriptar_senha()

    db.session.add(usuario_bd)
    db.session.commit()
    return usuario_bd
