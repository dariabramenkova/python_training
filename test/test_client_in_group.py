from model.client import Client
from model.group import Group
from random import randrange
import random
from fixture.orm import ORMFixture
import pytest

orm=ORMFixture(host="localhost", name="addressbook", user="root", password="")

def test_add_client_in_group(app, db):
    with pytest.allure.step('Given a group list and a client list'):
        clients=db.get_client_list()
        groups=db.get_group_list()
    with pytest.allure.step('Choice a group from list'):
        group = random.choice(groups)
    with pytest.allure.step('If do not find group,add him'):
        if len(db.get_group_list())==0:
            app.group.create(Group(name="test"))
    with pytest.allure.step('If do not find client,add him'):
        if len(db.get_client_list())==0:
            app.client.create(Client(name="test"))
    with pytest.allure.step('If do not find client not in group,add him'):
        if len(orm.get_clients_not_in_group(group)) == 0:
            app.client.create(Client(name="test"))

    with pytest.allure.step('Add client to group'):
        while True:
            client_index=randrange(len(clients))
            group_index=randrange(len(groups))
            client_id=clients[client_index].id
            group_id=groups[group_index].id
            if clients[client_index] not in orm.get_clients_in_group(groups[group_index]):
                break
        app.client.add_client_to_group(client_id, group_id)

        assert clients[client_index] in orm.get_clients_in_group(groups[group_index])


def test_del_client_from_group(app, db):
    with pytest.allure.step('If do not find group,add him'):
        if len(db.get_group_list())==0:
            app.group.create(Group(name="test"))
    with pytest.allure.step('If do not find client,add him'):
        if len(db.get_client_list())==0:
            app.client.create(Client(name="test"))
    with pytest.allure.step('Given a group list and a client list'):
        groups=db.get_group_list()
    with pytest.allure.step('Choice a group from list'):
        group_index=random.randrange(len(groups))
        group_id=groups[group_index].id
        clients=db.get_client_list()
    with pytest.allure.step('Del client from group'):
        if len(orm.get_clients_in_group(groups[group_index]))==0:
            client_index=random.randrange(len(clients))
            client=clients[client_index]
            client_id=client.id
            app.client.add_client_to_group(client_id, group_id)
        else:
            client=random.choice(orm.get_clients_in_group(groups[group_index]))
            client_id=client.id
        app.client.del_client_from_group(client_id, group_id)
        assert client not in orm.get_clients_in_group(groups[group_index])
