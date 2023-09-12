
from flask import Flask, jsonify

app = Flask(__name__)

ordem_pedidos = [
    {   
        'ID': 1,
        'Descrição': 'Pedido de compra 1',
        'Items': [
            {
                'Id': 1,
                'Descrição': 'Item do pedido 1',
                'Preço': 20.99
            }
        ]
    }
]

@app.route('/')        #decorator para acessar pasta raiz
def home():
    return "Hello World! alterado"

@app.route('/ordem_pedidos')    #decorator para acessar ordem_pedidos (dentro da pasta raiz)
def get_ordem_pedidos():
    return jsonify(ordem_pedidos)


@app.route('/odem_pedidos/<int:id>')
def get_odem_pedidos_by_id(id):
    for op in ordem_pedidos:
        if op['id'] == id:
            return jsonify(op)
    return jsonify({'message': 'Pedido {} não encontrado'.format(id)})

app.run(port=5000)


