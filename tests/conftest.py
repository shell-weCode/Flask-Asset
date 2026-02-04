import pytest
from app import create_app
from app.extensions import db

@pytest.fixture(scope="class")
def app():
    flask_app = create_app()
    flask_app.config["TESTING"] = True
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    flask_app.config["PROPAGATE_EXCEPTIONS"] = True 

    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope="class")
def client(app):
    return app.test_client()