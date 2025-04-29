
from flask import Flask, jsonify, request
from produtos import products
from auth import gerar_token, verificar_token

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    if dados['usuario'] == 'admin' and dados['senha'] == '123':
        token = gerar_token(dados['usuario'])
        return jsonify({"token": token})
    return jsonify({"erro": "Credenciais inválidas"}), 401

@app.route('/products', methods=['GET'])
def listar_produtos():
    resultado = verificar_token()
    if resultado:
        return resultado

    preco_asc = request.args.get('preco_asc')
    preco_desc = request.args.get('preco_desc')
    descricao = request.args.get('description_part')

    produtos_filtrados = products

    if preco_asc:
        produtos_filtrados = sorted(products, key=lambda x: x['product_price'])
    elif preco_desc:
        produtos_filtrados = sorted(products, key=lambda x: x['product_price'], reverse=True)
    elif descricao:
        produtos_filtrados = [p for p in products if descricao.lower() in p['product_description'].lower()]

    return jsonify(produtos_filtrados)

@app.route('/products/<int:id>', methods=['GET'])
def produto_por_id(id):
    resultado = verificar_token()
    if resultado:
        return resultado

    for produto in products:
        if produto['id'] == id:
            return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)

