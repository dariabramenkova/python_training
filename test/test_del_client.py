
from model.client import Client

def test_delete_first_client(app):
    if app.client.count() == 0:
        app.client.create_new_client(Client(name="Daria"))
    app.client.delete_first_client()
