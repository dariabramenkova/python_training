import re
from model.client import Client
import pytest

def test_phones_on_home_page(app, db):
    contact_from_home_page = sorted(app.client.get_client_list(), key=Client.id_or_max)
    contact_from_db_page = sorted(db.get_client_list(), key=Client.id_or_max)
    for number in range(len(db.get_client_list())):
        assert contact_from_home_page[number].name ==contact_from_db_page[number].name
        assert contact_from_home_page[number].lastname == contact_from_db_page[number].lastname
        assert contact_from_home_page[number].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db_page[number])
        assert contact_from_home_page[number].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db_page[number])

#def test_phones_on_client_view_page(app):
   # contact_from_view_page = app.client.get_client_from_view_page(0)
    #contact_from_edit_page = app.client.get_contact_info_from_edit_page(0)
    #assert contact_from_view_page.home == contact_from_edit_page.home
    #assert contact_from_view_page.work == contact_from_edit_page.work
    #assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    #assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[()-]","", s)

def merge_phones_like_on_home_page(client):
    return "\n".join(filter(lambda x: x != "",
                        map(lambda x: clear(x),filter
                            (lambda x: x is not None,
                                [client.home, client.mobile, client.work, client.phone2]))))

def merge_emails_like_on_home_page(client):
    return "\n".join(filter(lambda x: x != "",
                        map(lambda x: clear(x),filter
                            (lambda x: x is not None,
                                [client.email, client.email2, client.email3]))))
