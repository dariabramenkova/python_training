
from model.client import Client

def test_delete_first_client(app):
    old_clients=app.client.get_client_list()
    if app.client.count() == 0:
        app.client.create_new_client(Client(name="Daria"))
    app.client.delete_first_client()
    new_clients=app.client.get_client_list()
    assert len(old_clients)-1 == len(new_clients)
    old_clients[0:1] = []
    assert old_clients == new_clients