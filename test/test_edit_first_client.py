from model.client import Client
import random


def test_edit_first_client(app, db):
    old_clients=db.get_client_list()
    client2=random.choice(old_clients)
    client = Client(name="Masha")
    client.id = old_clients[0].id
    client.middlename = old_clients[1].middlename
    if app.client.count() == 0:
        app.client.create_new_client(Client(name="Daria"))
    app.client.edit_client_by_id(client2.id, client)
    new_clients=db.get_client_list()
    assert len(old_clients) == len(new_clients)
    old_clients[0]=client
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
