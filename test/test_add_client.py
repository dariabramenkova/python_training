# -*- coding: utf-8 -*-

from model.client import Client
import pytest

from data.add_client import constant as testdata


@pytest.mark.parametrize("client", testdata, ids=[repr(x) for x in testdata])
def test_add_client(app, client):
    old_clients=app.client.get_client_list()
    app.client.create_new_client(client)
    assert len(old_clients)+1 == app.client.count()
    new_clients=app.client.get_client_list()
    old_clients.append(client)
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)


