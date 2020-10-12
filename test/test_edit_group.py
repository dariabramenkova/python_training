
from model.group import Group

def test_edit_name_group(app):
    app.group.edit_first_group(Group(name=" edit"))

def test_edit_header_group(app):
    app.group.edit_first_group(Group(header=" edit"))
