
from model.client import Client
import random


def test_delete_first_client(app, db, check_ui):
    old_clients=db.get_client_list()
    client=random.choice(old_clients)
    if app.client.count() == 0:
        app.client.create_new_client(Client(name="Daria"))
    app.client.delete_client_by_id(client.id)
    new_clients=db.get_client_list()
    assert len(old_clients)-1 == len(new_clients)
    old_clients.remove(client)
    #old_clients[index:index+1] = []
    assert old_clients == new_clients
    if check_ui:
        assert sorted(new_clients, key=Client.id_or_max) == sorted(app.client.get_client_list(), key=Client.id_or_max)