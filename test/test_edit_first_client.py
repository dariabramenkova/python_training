from model.client import Client


def test_edit_first_client(app):
    app.session.login(username="admin", password="secret")
    app.client.edit_first_client(Client(name="Masha", middlename="", lastname="", nickname="",
                            title="",address="", home="", mobile="", work="",
                            fax="", email="", email2="", email3="",
                            bday="",bmonth="", byear="", aday="", amonth="", ayear="",
                            address2="", phone2=""))
    app.session.logout()