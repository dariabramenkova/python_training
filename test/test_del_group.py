
from model.group import Group
import random
import pytest

def test_delete_some_group(app, db, check_ui):
    with pytest.allure.step('If do not find group,add him'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
    with pytest.allure.step('Given a group list'):
        old_groups=db.get_group_list()
    with pytest.allure.step('Choice a group from list'):
        group=random.choice(old_groups)
    #index = randrange(len(old_groups))
    with pytest.allure.step('Choice a group from list'):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Then the new group list is equal to the old list with the adden group'):
        new_groups=db.get_group_list()
        assert len(old_groups)-1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
    #if check_ui:
    #    assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)