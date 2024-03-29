from storage import ClientStorage, ProductStorage

class ClientService:
    def __init__(self):
        self.model = ClientStorage()

    def fetch_clients(self):
        return self.model.fetch_clients()

    def fetch_client_by_id(self, id):
        client = self.model.fetch_client_by_id(id)
        if client:
            return client
        else:
            raise ValueError("Client not found")

    def insert_client(self, new_client):
        self.model.insert_client(new_client)

    def edit_client(self, id, modified_client):
        self.model.edit_client(id, modified_client)

    def delete_client(self, id):
        self.model.delete_client(id)

class ProductService:
    def __init__(self):
        self.model = ProductStorage()

    def fetch_products(self):
        return self.model.fetch_products()

    def fetch_product_by_id(self, id):
        product = self.model.fetch_product_by_id(id)
        if product:
            return product
        else:
            raise ValueError("Product not found")

    def insert_product(self, new_product):
        self.model.insert_product(new_product)

    def edit_product(self, id, modified_product):
        self.model.edit_product(id, modified_product)

    def delete_product(self, id):
        self.model.delete_product(id)
