from flask import Blueprint, jsonify, request
from conexao import criar_conexao, fechar_conexao

notificacoes_bp = Blueprint('notificacoes', __name__)

@notificacoes_bp.route('/obterNotificacoes/<int:id_usuario>', methods=['GET'])
def obterNotificacoes(id_usuario):
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("select * from Notificacoes where id_usuario = %s order by id_notificacao desc", (id_usuario,))
    dados = cursor.fetchall()

    cursor.close()
    fechar_conexao(conexao)
    return jsonify(dados)
