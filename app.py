from flask import Flask
from rotas.apiProdutos import produtos_bp
from rotas.apiUsuarios import usuarios_bp
from rotas.apiClientes import clientes_bp
from rotas.apiVendas import vendas_bp
from rotas.apiNotificacoes import notificacoes_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#registrar as rotas dos produtos
app.register_blueprint(produtos_bp, url_prefix='/produtos')
app.register_blueprint(clientes_bp, url_prefix='/clientes')
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
app.register_blueprint(vendas_bp, url_prefix='/vendas')
app.register_blueprint(notificacoes_bp, url_prefix='/notificacoes')

#inicializando o servidor flask
if __name__ == '__main__' :
    app.run( )
    #app.run( port=5000, host='192.168.0.237', debug=True )