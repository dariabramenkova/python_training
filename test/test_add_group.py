# -*- coding: utf-8 -*-


from model.group import Group
from sys import maxsize

def test_add_group(app):
    old_groups=app.group.get_group_list()
    group=Group(name="gruppa", header="druppa", footer="druppa2")
    app.group.create(group)
    new_groups=app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_group_empty(app):
    old_groups=app.group.get_group_list()
    group=Group(name="", header="", footer="")
    app.group.create(group)
    new_groups=app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
