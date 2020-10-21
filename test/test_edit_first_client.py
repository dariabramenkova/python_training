from model.client import Client
import random


def test_edit_first_client(app, db, check_ui):
    old_clients=db.get_client_list()
    client2=random.choice(old_clients)
    client = Client(name="Lerry")
    old_client=app.client.get_client_list()
    indexs=old_clients.index(client2)
    index=old_client.index(client2)
    client.id = old_clients[indexs].id
    if app.client.count() == 0:
        app.client.create_new_client(Client(name="Daria"))
    app.client.edit_client_by_index(index, client)
    new_clients=db.get_client_list()
    assert len(old_clients) == len(new_clients)
    old_clients[indexs]=client
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
    if check_ui:
        assert sorted(new_clients, key=Client.id_or_max) == sorted(app.client.get_client_list(), key=Client.id_or_max)