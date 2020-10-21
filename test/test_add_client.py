# -*- coding: utf-8 -*-

from model.client import Client


def test_add_client(app,  db, json_clients, check_ui):
    client=json_clients
    old_clients=db.get_client_list()
    app.client.create_new_client(client)
    #assert len(old_clients)+1 == app.client.count()
    new_clients=db.get_client_list()
    old_clients.append(client)
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
    if check_ui:
        assert sorted(new_clients, key=Client.id_or_max) == sorted(app.client.get_client_list(), key=Client.id_or_max)

