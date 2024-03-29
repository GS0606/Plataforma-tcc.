import sqlite3
from model import Client, Product
import datetime as datetime

class ClientStorage:
    def __init__(self, db_name='TCC.db'):
        self.db_name = db_name

    def connect_to_db(self):
        return sqlite3.connect(self.db_name)

    def create_client_table(self):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS client (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    data_nascimento TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            connection.commit()
            

    def fetch_clients(self):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM client")
            clients = cursor.fetchall()
        return [Client(id=row[0], name=row[1], surname=row[2], email=row[3], data_nascimento=row[4], created_at=row[5], updated_at=row[6]) for row in clients]

    def fetch_client_by_id(self, id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM client WHERE id=?", (id,))
            client = cursor.fetchone()
        return [Client(id=row[0], name=row[1], surname=row[2], email=row[3], data_nascimento=row[4], created_at=row[5], updated_at=row[6]) for row in client]

    def insert_client(self, new_client):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO client (name, surname, email, data_nascimento) VALUES (?, ?, ?, ?)",
                           (new_client.name, new_client.surname, new_client.email, new_client.data_nascimento))
            connection.commit()

    def edit_client(self, id, modified_client):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE client SET name=?, surname=?, email=?, data_nascimento=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                           (modified_client.name, modified_client.surname, modified_client.email, modified_client.data_nascimento, id))
            connection.commit()

    def delete_client(self, id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM client WHERE id=?", (id,))
            connection.commit()



class ProductStorage:
    def __init__(self, db_name='TCC.db'):
        self.db_name = db_name

    def connect_to_db(self):
        return sqlite3.connect(self.db_name)

    def create_product_table(self):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS product (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    destination TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            connection.commit()
    
    def fetch_products(self):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM product")
            products = cursor.fetchall()
        return [Product(id=row[0], name=row[1], destination=row[2], quantity=row[3], created_at=row[4], updated_at=row[5]) for row in products]

    def fetch_product_by_id(self, id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM product WHERE id=?", (id,))
            product = cursor.fetchone()
        return [Product(id=row[0], name=row[1], destination=row[2], quantity=row[3], created_at=row[4], updated_at=row[5]) for row in product]

    def insert_product(self, new_product):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO product (name, destination, quantity) VALUES (?, ?, ?)",
                           (new_product.name, new_product.destination, new_product.quantity))
            connection.commit()

    def edit_product(self, id, modified_product):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE product SET name=?, destination=?, quantity=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                           (modified_product.name, modified_product.destination, modified_product.quantity, id))
            connection.commit()

    def delete_product(self, id):
        with self.connect_to_db() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM product WHERE id=?", (id,))
            connection.commit()
