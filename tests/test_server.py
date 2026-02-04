
class TestServer:
    def test_server_starts(self, app):
        assert app is not None
        assert app.config["TESTING"] is True