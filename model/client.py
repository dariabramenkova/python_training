class Client:

    def __init__(self, name=None, middlename=None, lastname=None, nickname=None, title=None, address=None, home=None,
                 mobile=None, work=None, fax=None, email=None, email2=None, email3=None, bday="-", bmonth="-",
                 byear=None, aday="-", amonth="-", ayear=None, address2=None, phone2=None, id=None):
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


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.middlename)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.middlename == other.middlename
