
from model.group import Group

def test_edit_name_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name=" edit"))
    app.session.logout()

def test_edit_header_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header=" edit"))
    app.session.logout()