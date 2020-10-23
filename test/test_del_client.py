
from model.client import Client
import random
import pytest

def test_delete_first_client(app, db, check_ui):
    with pytest.allure.step('Given a client list'):
        old_clients=db.get_client_list()
    with pytest.allure.step('Choice a client from list'):
        client=random.choice(old_clients)
    with pytest.allure.step('If do not find client,add him'):
        if app.client.count() == 0:
            app.client.create_new_client(Client(name="Daria"))
    with pytest.allure.step('Delete client'):
        app.client.delete_client_by_id(client.id)
    with pytest.allure.step('Then the new group list is equal to the old list with the adden group'):
        new_clients=db.get_client_list()
        assert len(old_clients)-1 == len(new_clients)
        old_clients.remove(client)
    #old_clients[index:index+1] = []
        assert old_clients == new_clients
    #if check_ui:
    #    assert sorted(new_clients, key=Client.id_or_max) == sorted(app.client.get_client_list(), key=Client.id_or_max)