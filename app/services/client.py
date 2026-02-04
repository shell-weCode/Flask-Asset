from app.models import Client
from app.extensions import db

class ClientService():
    def create_client(self, client_data):
        client = Client(**client_data)
        db.session.add(client)
        db.session.commit()
        return client
    
    def get_all_clients(self):
        return Client.query.all()
    
    def delete_client(self, client_id):
        client = Client.query.get(client_id)
        if not client:
            return None

        db.session.delete(client)
        db.session.commit()
        return True
    
    def update_client(self, client_id, client_data):
        client = Client.query.get(client_id)
        if not client:
            return None

        for key, value in client_data.items():
            setattr(client, key, value)

        db.session.commit()

        return client

