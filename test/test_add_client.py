# -*- coding: utf-8 -*-

from model.client import Client


def test_add_client(app):
    app.client.create_new_client(Client(name="Daria", middlename="Yuryevna", lastname="Familia", nickname="daria",
                            title="Title",address="Spb", home="Pskov", mobile="+79808887755", work="Company",
                            fax="+77000222", email="email@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru",
                            bday="10",bmonth="August", byear="1999", aday="15", amonth="April", ayear="2020",
                            address2="Spb2", phone2="+79808887756"))

def test_add_client_new(app):
    app.client.create_new_client(Client(name="Lena", middlename="Yuryevna", lastname="Familia", nickname="lena",
                            title="Title",address="Spb", home="Pskov", mobile="+79808887755", work="Company",
                            fax="+77000222", email="email@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru",
                            bday="10",bmonth="August", byear="1999", aday="15", amonth="April", ayear="2020",
                            address2="Spb2", phone2="+79808887756"))
