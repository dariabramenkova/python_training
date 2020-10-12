from model.client import Client


def test_edit_first_client(app):
    app.client.edit_first_client(Client(name="Masha"))
