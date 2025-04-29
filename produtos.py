from flask import Blueprint, jsonify, request
from auth import token_obrigatorio
from data import products

produtos_bp = Blueprint('produtos', __name__)

@produtos_bp.route('/products')
@token_obrigatorio
def listar_produtos():
    preco_asc = request.args.get('preco_asc')
    preco_desc = request.args.get('preco_desc')
    descricao = request.args.get('description_part')

    lista = produtos

    if descricao:
        lista = [p for p in lista if descricao.lower() in p["product_description"].lower()]

    if preco_asc:
        lista = sorted(lista, key=lambda x: x["product_price"])

    if preco_desc:
        lista = sorted(lista, key=lambda x: x["product_price"], reverse=True)

    return jsonify(lista)

@produtos_bp.route('/products/<int:id>')
@token_obrigatorio
def produto_por_id(id):
    for p in produtos:
        if p["id"] == id:
            return jsonify(p)
    return jsonify({"erro": "Produto não encontrado"}), 404
