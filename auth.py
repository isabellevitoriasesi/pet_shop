import jwt
from flask import request, jsonify

SECRET_KEY = 'minha_chave_secreta'


def gerar_token(usuario):
    token = jwt.encode({"usuario": usuario}, SECRET_KEY, algorithm="HS256")
    return token


def token_obrigatorio(funcao):
    def verificar(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"erro": "Token não encontrado!"}), 401

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"erro": "Token expirado!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"erro": "Token inválido!"}), 401

        return funcao(*args, **kwargs)

    verificar.__name__ = funcao.__name__
    return verificar
