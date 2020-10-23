# -*- coding: utf-8 -*-

from model.client import Client
import pytest

def test_add_client(app,  db, json_clients, check_ui):
    client=json_clients
    with pytest.allure.step('Given a client list'):
        old_clients=db.get_client_list()
    with pytest.allure.step('When I add a client %s to the list' % client):
        app.client.create_new_client(client)
    with pytest.allure.step('Then the new client list is equal to the old list with the adden client'):
        new_clients=db.get_client_list()
        old_clients.append(client)
        assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
    #if check_ui:
    #    assert sorted(new_clients, key=Client.id_or_max) == sorted(app.client.get_client_list(), key=Client.id_or_max)

