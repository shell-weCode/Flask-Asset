
class TestClient:
    def test_post_client(self, client):
        """POST /clients/"""
        data = {"name": "Saul", "phone": "3318894560"}
        response = client.post("/clients/", json=data)
        assert response.status_code == 201

    def test_get_clients(self, client):
        """GET /clients/"""
        response = client.get("/clients/")
        assert response.status_code == 200

    def test_put_client(self, client):
        """PUT /clients/<id>"""
        client_id = 1
        updated_data = {"name": "Saul Updated", "phone": "12345678"}
        response = client.put(f"/clients/{client_id}", json=updated_data)
        assert response.status_code == 200

    def test_delete_client(self, client):
        """DELETE /clients/<id>"""
        client_id = 1
        resp = client.delete(f"/clients/{client_id}")
        assert resp.status_code == 200
        assert resp.get_json() == {"status": "deleted"}