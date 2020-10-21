
from model.group import Group
import random
from random import randrange

def test_edit_name_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups=db.get_group_list()
    group_id=random.choice(old_groups)
    group = Group(name="edit2")
    group.id = old_groups[old_groups.index(group_id)].id
    app.group.edit_group_by_id(group_id.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[old_groups.index(group_id)]=group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
