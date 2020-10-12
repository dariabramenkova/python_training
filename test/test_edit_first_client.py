from model.client import Client


def test_edit_first_client(app):
    app.session.login(username="admin", password="secret")
    app.client.edit_first_client(Client(name="Masha"))
    app.session.logout()