from flask import Blueprint, jsonify, request
from conexao import criar_conexao, fechar_conexao

clientes_bp = Blueprint('clientes', __name__)

#rota ou endpoint obterclientes
@clientes_bp.route('/teste', methods=['GET'])
def teste():
    return jsonify({'led': 500})

#rota ou endpoint obterclientes
@clientes_bp.route('/obterClientes', methods=['GET'])
def obterTodosClientes():
    #criar conexão e um cursor
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

#Executa a consulta SQL para obter clientes
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()

    cursor.close()
    fechar_conexao(conexao)
    return jsonify(clientes)

@clientes_bp.route('/obterClientes/<string:pesquisa>', methods=['GET'])
def obterclientes(pesquisa):
    #criar conexão e um cursor
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

#Executa a consulta SQL para obter clientes
    cursor.execute('SELECT * FROM clientes where nome like %s', (f'%{pesquisa}%',))
    clientes = cursor.fetchall()

    cursor.close()
    fechar_conexao(conexao)
    return jsonify(clientes)


@clientes_bp.route('/incluirCliente', methods=['POST'])
def incluirCliente():
    #recupera dados do cliente 
    novocliente = request.get_json()

    #validação de dados 
    if 'nome' not in novocliente and 'cidade' not in novocliente and 'telefone' not in novocliente and 'cep' not in novocliente and 'endereco' not in novocliente and 'numero' not in novocliente and 'bairro' not in novocliente :
        return jsonify({'status': 'error', 'message':'Dados Incompletos envie (nome, cidade, telefone, cep)'}), 400
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        comando = 'INSERT INTO clientes(nome, cidade, telefone, cep, endereco, numero, bairro) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(comando, (novocliente['nome'], novocliente['cidade'], novocliente['telefone'], novocliente['cep'], novocliente['endereco'], novocliente['numero'], novocliente['bairro']))
        conexao.commit()

        #retorna um json com status 
        status = {'status': 'succes', 'message' : 'Cliente cadastrado com sucesso', 'code': 201}
    except Exception as e:
        #em caso de erro, desfaz as alterações e retornar o erro 
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}

    finally:
        cursor.close()
        fechar_conexao(conexao)

    return jsonify(status)


@clientes_bp.route ('/alterarCliente/<int:id>', methods=['PUT'])
def alterarCliente(id):
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

    dados = request.get_json()

    try:
       #lista de campo a ser atualizadas e lista de campos correspondentes
       campos_para_atualizar = []
       valores_para_atualizar = []
       if 'nome' in dados :
           campos_para_atualizar.append('nome = %s')
           valores_para_atualizar.append(dados['nome'])
       if 'cidade' in dados :
           campos_para_atualizar.append('cidade = %s')
           valores_para_atualizar.append(dados['cidade'])
       if 'endereco' in dados :
           campos_para_atualizar.append('endereco = %s')
           valores_para_atualizar.append(dados['endereco'])
       if 'telefone' in dados :
           campos_para_atualizar.append('telefone = %s')
           valores_para_atualizar.append(dados['telefone'])
       if 'cep' in dados :
           campos_para_atualizar.append('cep = %s')
           valores_para_atualizar.append(dados['cep'])
       if 'numero' in dados :
           campos_para_atualizar.append('numero = %s')
           valores_para_atualizar.append(dados['numero'])
       if 'bairro' in dados :
           campos_para_atualizar.append('bairro = %s')
           valores_para_atualizar.append(dados['bairro'])
       if not campos_para_atualizar:
           return jsonify({"status": 'error', 'message': 'nenhum campo fornecido'}), 400
        #constroi uma consulta de atualização
       comando = "UPDATE clientes SET " + ", ".join(campos_para_atualizar) + ' WHERE id_cliente = %s'
       valores = valores_para_atualizar + [id]

       #executar a consulta de atualizações
       cursor.execute(comando, valores)
       conexao.commit()
       status = {'status': 'success', 'message':'cliente alterado com sucesso'}
       return jsonify(status),201


    except Exception as e:
        #em caso de erro, desfaz as alterações e retornar o erro 
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}
        return jsonify(status)
    finally:
        cursor.close()
        fechar_conexao(conexao)

@clientes_bp.route('/excluirCliente/<int:id>', methods=['DELETE'])
def excluirCliente(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    livro_existe = cursor.execute('SELECT COUNT(*) FROM clientes WHERE ID_cliente = %s', (id,))
    #consumir o resultado
    cursor.fetchone()

    if livro_existe == 0:
        return jsonify({'status':'error', 'message':'Usuário não encotrado'}), 404
    try:
        #delete o livro com o id especifico
        comando = 'DELETE FROM clientes WHERE ID_cliente = %s'
        cursor.execute(comando, (id,))

        conexao.commit()
        status = {'status': 'succes', 'message': 'Usuário excluído com sucesso'}, 201

    except Exception as e:
        #em caso de erro, desfaz as alterações e retornar o erro 
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}

    finally:
        cursor.close()
        fechar_conexao(conexao)
        return jsonify(status)

