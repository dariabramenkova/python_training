from model.client import Client
from model.group import Group
import random
from fixture.orm import ORMFixture

orm=ORMFixture(host="localhost", name="addressbook", user="root", password="")

def test_del_client_from_group(app, db):
    if len(db.get_group_list())==0:
        app.group.create(Group(name="test"))
    if len(db.get_client_list())==0:
        app.client.create(Client(name="test"))

    groups=db.get_group_list()
    group_index=random.randrange(len(groups))
    group_id=groups[group_index].id
    clients=db.get_client_list()

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
