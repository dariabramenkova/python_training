from model.client import Client
import string
import random
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:],"n:f:", ["number of clients", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f= "data/clients.json"

for o, a in opts:
    if o =="-n":
        n=int(a)
    elif o == "-f":
        f=a


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
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))