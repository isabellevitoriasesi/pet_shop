from flask import Flask, jsonify, request
from produtos import produtos_bp
from auth import gerar_token
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

# Rota para login e receber token
@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    usuario = dados.get('usuario')
    senha = dados.get('senha')

    if usuario == 'admin' and senha == '123':
        token = gerar_token(usuario)
        return jsonify({"token": token})
    else:
        return jsonify({"erro": "Usuário ou senha inválidos"}), 401

# Registra as rotas dos produtos
app.register_blueprint(produtos_bp)

if __name__ == '__main__':
    app.run()


