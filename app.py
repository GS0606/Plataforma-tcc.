from flask import Flask, request, jsonify
from service import ClientService, ProductService
from model import Client, Product

app = Flask(__name__)

client_service = ClientService()
product_service = ProductService()

# Rotas para Clients

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = client_service.fetch_clients()
    return jsonify(clients), 200

@app.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    client = client_service.fetch_client_by_id(id)
    if client:
        return jsonify(client), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@app.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    new_client = Client(id=None, name=data['name'], surname=data['surname'], email=data['email'], data_nascimento=data['data_nascimento'])
    client_service.insert_client(new_client)
    return 'Client created successfully', 201

@app.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    data = request.json
    modified_client = Client(id=id, name=data['name'], surname=data['surname'], email=data['email'], data_nascimento=data['data_nascimento'])
    client_service.edit_client(id, modified_client)
    return 'Client updated successfully', 200

@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    client_service.delete_client(id)
    return 'Client deleted successfully', 200


# Rotas para Products

@app.route('/products', methods=['GET'])
def get_products():
    products = product_service.fetch_products()
    return jsonify(products), 200

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = product_service.fetch_product_by_id(id)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(id=None, name=data['name'], destination=data['destination'], quantity=data['quantity'])
    product_service.insert_product(new_product)
    return 'Product created successfully', 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    modified_product = Product(id=id, name=data['name'], destination=data['destination'], quantity=data['quantity'])
    product_service.edit_product(id, modified_product)
    return 'Product updated successfully', 200

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product_service.delete_product(id)
    return 'Product deleted successfully', 200


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
