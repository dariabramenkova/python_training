# -*- coding: utf-8 -*-

from model.client import Client
import pytest
import string
import random

def random_string(prefix, maxlen):
    symbols=string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
def random_only_digital(prefix, maxlen):
    symbols=string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Client (name="", middlename="", lastname="", nickname="", address="", home="", mobile="", work="",
                   email="", email2="", email3="", phone2="") ] + [
    Client(name=random_string("name",5), middlename=random_string("middlename", 10),
           lastname=random_string("lastname",20), nickname=random_string("nickname",20),
           address=random_string("address",20), home=random_only_digital("home", 11),
           mobile=random_only_digital("mobile",11), work=random_only_digital("work",11),
           email="email@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru",
           phone2=random_only_digital("phone2",11)
           )
    for i in range(5)
]

#client = Client(name="Daria", middlename="Yuryevna", lastname="Familia", nickname="daria",
#                title="Title", address="Spb", home="79999999999", mobile="79808887755", work="79999999999",
#                fax="+77000222", email="email@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru",
#                bday="10", bmonth="August", byear="1999", aday="15", amonth="April", ayear="2020",
#                address2="Spb2", phone2="79808887756")

@pytest.mark.parametrize("client", testdata, ids=[repr(x) for x in testdata])
def test_add_client(app, client):
    old_clients=app.client.get_client_list()
    app.client.create_new_client(client)
    assert len(old_clients)+1 == app.client.count()
    new_clients=app.client.get_client_list()
    old_clients.append(client)
    assert sorted(old_clients, key=Client.id_or_max) == sorted(new_clients, key=Client.id_or_max)


