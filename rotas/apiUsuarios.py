from flask import Blueprint, jsonify, request
from conexao import criar_conexao, fechar_conexao

usuarios_bp = Blueprint('usuarios', __name__)

#rota ou endpoint obterusuarios
@usuarios_bp.route('/obterUsuarios', methods=['GET'])
def obterUsuarios():
    #criar conexão e um cursor
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

#Executa a consulta SQL para obter usuarios
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    cursor.close()
    fechar_conexao(conexao)
    return jsonify(usuarios)

@usuarios_bp.route('/login', methods=['POST'])
def login():
    usuario = request.get_json()
    
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute('SELECT * FROM usuarios where nome_usuario = %s and senha = %s and tipo_usuario = %s', (usuario['usuario'],usuario['senha'], usuario['tipo_usuario']))
    usuario = cursor.fetchall()

    cursor.close()
    fechar_conexao(conexao)
    return jsonify(usuario)


@usuarios_bp.route('/incluirUsuario', methods=['POST'])
def incluirUsuario():
    #recupera dados do Usuario 
    novoUsuario = request.get_json()

    #validação de dados 
    if 'nome' not in novoUsuario and 'nome_usuario' not in novoUsuario and 'senha' not in novoUsuario and 'tipo_usuario' not in novoUsuario:
        return jsonify({'status': 'error', 'message':'Dados Incompletos envie (nome, nome_usuario, senha, tipo_usuario)'}), 400
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try:
        comando = 'INSERT INTO usuarios(nome, nome_usuario, senha, tipo_usuario) VALUES(%s, %s, %s, %s)'
        cursor.execute(comando, (novoUsuario['nome'], novoUsuario['nome_usuario'], novoUsuario['senha'], novoUsuario['tipo_usuario']))
        conexao.commit()

        #retorna um json com status 
        status = {'status': 'succes', 'message' : 'Usuário cadastrado com sucesso', 'code': 201}
    except Exception as e:
        #em caso de erro, desfaz as alterações e retornar o erro 
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}

    finally:
        cursor.close()
        fechar_conexao(conexao)

    return jsonify(status)


@usuarios_bp.route ('/alterarUsuario/<int:id>', methods=['PUT'])
def alterarUsuario(id):
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

    dados = request.get_json()

    try:
       #lista de campo a ser atualizadas e lista de campos correspondentes
       campos_para_atualizar =[]
       valores_para_atualizar = []
       if 'nome' in dados :
           campos_para_atualizar.append('nome = %s')
           valores_para_atualizar.append(dados['nome'])
       if 'nome_usuario' in dados :
           campos_para_atualizar.append('nome_usuario = %s')
           valores_para_atualizar.append(dados['nome_usuario'])
       if 'senha' in dados :
           campos_para_atualizar.append('senha = %s')
           valores_para_atualizar.append(dados['senha'])
       if 'tipo_usuario' in dados :
           campos_para_atualizar.append('tipo_usuario = %s')
           valores_para_atualizar.append(dados['tipo_usuario'])
       if not campos_para_atualizar:
           return jsonify({"status": 'error', 'message': 'nenhum campo fornecido'}), 400
        #constroi uma consulta de atualização
       comando = "UPDATE usuarios SET " + ", ".join(campos_para_atualizar) + ' WHERE id_Usuario = %s'
       valores = valores_para_atualizar + [id]

       #executar a consulta de atualizações
       cursor.execute(comando, valores)
       conexao.commit()
       status = {'status': 'success', 'message':'Usuario alterado com sucesso'}
       return jsonify(status),201


    except Exception as e:
        #em caso de erro, desfaz as alterações e retornar o erro 
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}
        return jsonify(status)
    finally:
        cursor.close()
        fechar_conexao(conexao)

@usuarios_bp.route('/excluirUsuario/<int:id>', methods=['DELETE'])
def excluirUsuario(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    livro_existe = cursor.execute('SELECT COUNT(*) FROM usuarios WHERE ID_Usuario = %s', (id,))
    #consumir o resultado
    cursor.fetchone()

    if livro_existe == 0:
        return jsonify({'status':'error', 'message':'Usuário não encotrado'}), 404
    try:
        #delete o livro com o id especifico
        comando = 'DELETE FROM usuarios WHERE ID_Usuario = %s'
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

