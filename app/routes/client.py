from flask_smorest import Blueprint, abort
from flask.views import MethodView

from app.schemas.client import ClientSchema
from app.services.client import ClientService

client_service = ClientService()

blp = Blueprint("Clients", __name__, url_prefix="/clients", description="Operations on clients")

@blp.route("/")
class Client(MethodView):

    @blp.arguments(ClientSchema)
    @blp.response(201, ClientSchema)
    def post(self, client_data):
        client = client_service.create_client(client_data)
        return client
    
    @blp.response(200, ClientSchema(many=True))
    def get(self):
        return client_service.get_all_clients()

@blp.route("/<int:client_id>")
class ClientResource(MethodView):
    @blp.response(200)
    def delete(self, client_id):
        is_deleted = client_service.delete_client(client_id)
        if not is_deleted:
            abort(404, message="Client not found")

        return {"status": "deleted"}

    @blp.arguments(ClientSchema)
    @blp.response(200, ClientSchema)
    def put(self, client_data, client_id):
        client = client_service.update_client(client_id, client_data)
        if not client:
            abort(404, message="Client not found")
        return client

