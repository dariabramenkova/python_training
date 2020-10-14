# -*- coding: utf-8 -*-


from model.group import Group
from sys import maxsize

def test_add_group(app):
    old_groups=app.group.get_group_list()
    group=Group(name="gruppa", header="druppa", footer="druppa2")
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups=app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_add_group_empty(app):
    old_groups=app.group.get_group_list()
    group=Group(name="", header="", footer="")
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups=app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
