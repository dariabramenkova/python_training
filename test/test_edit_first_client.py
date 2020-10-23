from model.client import Client
import random
import pytest

def test_edit_first_client(app, db, check_ui):
    with pytest.allure.step('Given a client list'):
        old_clients=db.get_client_list()
    with pytest.allure.step('Choice a client from list'):
        client2=random.choice(old_clients)
    with pytest.allure.step('Edit a client from list'):
        client = Client(name="Lerry")
        old_client=app.client.get_client_list()
        indexs=old_clients.index(client2)
        index=old_client.index(client2)
        client.id = old_clients[indexs].id
    with pytest.allure.step('If do not find client,add him'):
        if app.client.count() == 0:
            app.client.create_new_client(Client(name="Daria"))
        app.client.edit_client_by_index(index, client)
    with pytest.allure.step('Then the new group list is equal to the old list with the adden group'):
        new_clients=db.get_client_list()
        assert len(old_clients) == len(new_clients)
        old_clients[indexs]=client
        assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)
    #if check_ui:
    #    assert sorted(new_clients, key=Client.id_or_max) == sorted(app.client.get_client_list(), key=Client.id_or_max)