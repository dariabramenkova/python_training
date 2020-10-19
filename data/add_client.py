from model.client import Client
import string
import random



constant=[
    Client(name="name1", middlename="middlename1", lastname="lastname1", nickname="rrr", address="", home="8889999000",
           mobile="8889999003", work="8889999004", email="as@mail.ru", email2="as2@mail.ru", email3="as3@mail.ru",
           phone2="9889999002"),
    Client(name="name2", middlename="middlename2", lastname="lastname2", nickname="ddd", address="", home="8889999001",
           mobile="8889999002", work="8889999005", email="as4@mail.ru", email2="as5@mail.ru", email3="as@mail.ru6",
           phone2="9889999004")
]


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