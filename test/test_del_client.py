
from model.client import Client
from random import randrange


def test_delete_first_client(app):
    old_clients=app.client.get_client_list()
    index = randrange(len(old_clients))
    if app.client.count() == 0:
        app.client.create_new_client(Client(name="Daria"))
    app.client.delete_client_by_index(index)
    new_clients=app.client.get_client_list()
    assert len(old_clients)-1 == len(new_clients)
    old_clients[index:index+1] = []
    assert old_clients == new_clients