
from sys import maxsize


class Client:

    def __init__(self, name=None, middlename=None, lastname=None, nickname=None, title=None, address=None, home=None,
                 mobile=None, work=None, fax=None, email=None, email2=None, email3=None, bday="-", bmonth="-",
                 byear=None, aday="-", amonth="-", ayear=None, address2=None, phone2=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.name=name
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.address=address
        self.home=home
        self.mobile=mobile
        self.work=work
        self.fax=fax
        self.email=email
        self.email2=email2
        self.email3=email3
        self.bday=bday
        self.bmonth=bmonth
        self.byear=byear
        self.aday=aday
        self.amonth=amonth
        self.ayear=ayear
        self.address2=address2
        self.phone2=phone2
        self.id=id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.middlename)

    def __eq__(self, other2):
        return self.id is None or other2.id is None or self.id == other2.id and self.name == other2.name and \
               self.middlename==other2.middlename

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
