
import pymysql.cursors
from model.group import Group
from model.client import Client

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host=host
        self.name=name
        self.user=user
        self.password=password
        self.connection=pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)


    def get_group_list(self):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=str(id), name=name))
        finally:
            cursor.close()
        return list


    def get_client_list(self):
        list2=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, email, email2, email3, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname,lastname, home, mobile, work, email, email2, email3, phone2) = row
                list2.append(Client(id=str(id), name=firstname, lastname=lastname, home=home, mobile=mobile, work=work, email=email, email2=email2, email3=email3, phone2=phone2))
        finally:
            cursor.close()
        return list2



    def destroy(self):
        self.connection.close()