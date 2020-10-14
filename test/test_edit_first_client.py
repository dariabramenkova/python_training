from model.client import Client
from random import randrange


def test_edit_first_client(app):
    old_clients=app.client.get_client_list()
    index = randrange(len(old_clients))
    client = Client(name="Masha")
    client.id = old_clients[index].id
    client.middlename = old_clients[index].middlename
    if app.client.count() == 0:
        app.client.create_new_client(Client(name="Daria"))
    app.client.edit_client_by_index(index, client)
    new_clients=app.client.get_client_list()
    assert len(old_clients) == len(new_clients)
    old_clients[index]=client
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
