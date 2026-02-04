from .client import blp as ClientBlueprint

def register_blueprints(api):
    api.register_blueprint(ClientBlueprint)
