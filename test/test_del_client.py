

def test_delete_first_client(app):
    app.session.login(username="admin", password="secret")
    app.client.delete_first_client()
    app.session.logout()