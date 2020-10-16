import re
from random import randrange


def test_phones_on_home_page(app):
    clients=app.client.get_client_list()
    index = randrange(len(clients))
    contact_from_home_page = app.client.get_client_list()[index]
    contact_from_edit_page = app.client.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

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
