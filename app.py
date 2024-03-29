from flask import Flask, request, jsonify
from service import ClientService, ProductService
from model import Client, Product
from storage import ClientStorage, ProductStorage
import json
from datetime import datetime

app = Flask(__name__)

client_storage = ClientStorage()
client_storage.create_client_table()

product_storage = ProductStorage()
product_storage.create_product_table()

client_service = ClientService()
product_service = ProductService()

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = client_service.fetch_clients()
    return jsonify(clients), 200

def serialize(obj):
    if isinstance(obj, (datetime)):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

@app.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    try:
        client = client_service.fetch_client_by_id(id)
        return jsonify(client), 200
    except ValueError as e:
        return str(e), 404

@app.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    new_client = Client(id=None, name=data['name'], surname=data['surname'], email=data['email'], data_nascimento=data['data_nascimento'], created_at=None, updated_at=None)
    client_service.insert_client(new_client)
    return 'Client created successfully', 201

@app.route('/products', methods=['GET'])
def get_products():
    products = product_service.fetch_products()
    return jsonify(products), 200

def serialize(obj):
    if isinstance(obj, (datetime)):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(id=None, name=data['name'], destination=data['destination'], quantity=data['quantity'], created_at=None, updated_at=None)
    product_service.insert_product(new_product)
    return 'Product created successfully', 201

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
