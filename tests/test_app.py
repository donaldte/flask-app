from app import app  # Importe l'application Flask

def test_hello():
    client = app.test_client()  # Simule un client HTTP
    response = client.get("/hello")  # Envoie une requête GET
    assert response.status_code == 200  # Vérifie le code HTTP