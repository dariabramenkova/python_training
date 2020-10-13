from model.client import Client


def test_edit_first_client(app):
    old_clients=app.client.get_client_list()
    if app.client.count() == 0:
        app.client.create_new_client(Client(name="Daria"))
    app.client.edit_first_client(Client(name="Masha"))
    new_clients=app.client.get_client_list()
    assert len(old_clients) == len(new_clients)
