import jwt
import datetime
from flask import request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("bi")

def gerar_token(usuario):
    payload = {
        "usuario": usuario,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verificar_token():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"erro": "Token não enviado"}), 401
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except:
        return jsonify({"erro": "Token inválido"}), 403
