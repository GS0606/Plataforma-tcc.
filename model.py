import datetime

class Client:
    def __init__(self, id, name, surname, email, data_nascimento, created_at: datetime , Updated_at: datetime):
        
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.data_nascimento = data_nascimento
        self.created_at: datetime= created_at
        self.Updated_at: datetime= Updated_at
        

class Product:
    def __init__(self, id, name, destination, quantity, created_at: datetime , updated_at: datetime):
        self.id = id
        self.name = name
        self.destination = destination
        self.quantity = quantity
        self.created_at = created_at
        self.updated_at = updated_at
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'destination': self.destination,
            'quantity': self.quantity,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

