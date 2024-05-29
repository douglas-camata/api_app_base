from flask import Blueprint, jsonify, request
from conexao import criar_conexao, fechar_conexao

produtos_bp = Blueprint('produtos', __name__)


#rota ou endpoint obterprodutos
@produtos_bp.route('/obterProdutos', methods=['GET'])
def obterTodosProdutos():
    #criar conexão e um cursor
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute('SELECT * FROM produtos where titulo <> "" order by titulo')
    produtos = cursor.fetchall()

    cursor.close()
    fechar_conexao(conexao)
    return jsonify(produtos)

@produtos_bp.route('/obterProdutos/<string:pesquisa>', methods=['GET'])
def obterProdutos(pesquisa):
    #criar conexão e um cursor
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

#Executa a consulta SQL para obter produtos
    cursor.execute('SELECT * FROM produtos where titulo like %s', (f'%{pesquisa}%',))
    produtos = cursor.fetchall()

    cursor.close()
    fechar_conexao(conexao)
    return jsonify(produtos)


@produtos_bp.route('/incluirProduto', methods=['POST'])
def incluirProduto():
    #recupera dados do Produto 
    novoProduto = request.get_json()

    #validação de dados 
    #verificacao se os campos 'titulo' e 'autor' estão no objetivo
    if 'imagem' not in novoProduto or 'preco' not in novoProduto or 'titulo' not in novoProduto:
        return jsonify({'status': 'error', 'message':'Dados Incompletos'}), 400
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        comando = 'INSERT INTO produtos(imagem, preco, titulo) VALUES(%s, %s, %s)'
        cursor.execute(comando, (novoProduto['imagem'], novoProduto['preco'], novoProduto['titulo']))
        conexao.commit()

        #retorna um json com status 
        status = {'status': 'succes', 'message' : 'Produto cadastrado com sucesso', 'code': 201}
    except Exception as e:
        #em caso de erro, desfaz as alterações e retornar o erro 
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}

    finally:
        cursor.close()
        fechar_conexao(conexao)

    return jsonify(status)


@produtos_bp.route ('/alterarProduto/<int:id>', methods=['PUT'])
def alterarProduto(id):
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

    dados = request.get_json()

    try:
       #lista de campo a ser atualizadas e lista de campos correspondentes
       campos_para_atualizar =[]
       valores_para_atualizar = []
       if 'titulo' in dados :
           campos_para_atualizar.append('titulo = %s')
           valores_para_atualizar.append(dados['titulo'])
       if 'preco' in dados :
           campos_para_atualizar.append('preco = %s')
           valores_para_atualizar.append(dados['preco'])
       if 'imagem' in dados :
           campos_para_atualizar.append('imagem = %s')
           valores_para_atualizar.append(dados['imagem'])
       if not campos_para_atualizar:
           return jsonify({"status": 'error', 'message': 'nenhum campo fornecido'}), 400
        #constroi uma consulta de atualização
       comando = "UPDATE produtos SET " + ", ".join(campos_para_atualizar) + ' WHERE ID_produto = %s'
       valores = valores_para_atualizar + [id]

       #executar a consulta de atualizações
       cursor.execute(comando, valores)
       conexao.commit()
       status = {'status': 'success', 'message':'Produto alterado com sucesso', 'comando' : comando, 'valores' : valores}
       return jsonify(status),201


    except Exception as e:
        #em caso de erro, desfaz as alterações e retornar o erro 
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}
        return jsonify(status)
    finally:
        cursor.close()
        fechar_conexao(conexao)

@produtos_bp.route('/excluirProduto/<int:id>', methods=['DELETE'])
def excluirProduto(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    livro_existe = cursor.execute('SELECT COUNT(*) FROM produtos WHERE ID_produto = %s', (id,))
    #consumir o resultado
    cursor.fetchone()

    if livro_existe == 0:
        return jsonify({'status':'error', 'message':'Produto não não encotrado'}), 404
    try:
        #delete o livro com o id especifico
        comando = 'DELETE FROM produtos WHERE ID_produto = %s'
        cursor.execute(comando, (id,))

        conexao.commit()
        status = {'status': 'succes', 'message': 'Produto excluído com sucesso'}, 201

    except Exception as e:
        #em caso de erro, desfaz as alterações e retornar o erro 
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}

    finally:
        cursor.close()
        fechar_conexao(conexao)
        return jsonify(status)

