from flask import Blueprint, jsonify, request
from conexao import criar_conexao, fechar_conexao

vendas_bp = Blueprint('vendas', __name__)

@vendas_bp.route('/obterVendasCliente/<int:id_cliente>', methods=['GET'])
def obterVendasCliente(id_cliente):
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("select v.id_venda, date_format(v.data_venda, '%d/%m/%Y') as data_venda, p.titulo, p.imagem, p.preco from Vendas v inner join produtos p on v.id_produto = p.id_produto where v.id_cliente = %s order by v.id_venda desc", (id_cliente,))
    dados = cursor.fetchall()

    cursor.close()
    fechar_conexao(conexao)
    return jsonify(dados)


@vendas_bp.route('/incluirVenda', methods=['POST'])
def incluirVenda(): 
    novaVenda = request.get_json()

    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

    try:
        comando = 'insert into vendas(id_cliente, id_produto, id_usuario, data_venda) VALUES(%s, %s, %s, current_date)'
        cursor.execute(comando, (novaVenda['id_cliente'], novaVenda['id_produto'], novaVenda['id_usuario']))
        conexao.commit()
        status = {'status': 'succes', 'message' : 'Venda cadastrada com sucesso', 'code': 201}
    except Exception as e:
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}
    finally:
        cursor.close()
        fechar_conexao(conexao)

    return jsonify(status)

@vendas_bp.route('/excluirVenda/<int:id>', methods=['DELETE'])
def excluirVenda(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        comando = 'delete from vendas where id_venda = %s'
        cursor.execute(comando, (id,))

        conexao.commit()
        status = {'status': 'succes', 'message': 'Venda excluída com sucesso'}, 201

    except Exception as e:
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}

    finally:
        cursor.close()
        fechar_conexao(conexao)
        return jsonify(status)

