from model.client import Client


def test_edit_first_client(app):
    old_clients=app.client.get_client_list()
    client = Client(name="Masha")
    client.id = old_clients[0].id
    #if app.client.count() == 0:
    #    app.client.create_new_client(Client(name="Daria"))
    app.client.edit_first_client(client)
    new_clients=app.client.get_client_list()
    assert len(old_clients) == len(new_clients)
    old_clients[0]=client
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
