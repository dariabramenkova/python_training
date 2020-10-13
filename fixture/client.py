from selenium.webdriver.support.ui import Select

class ClientHelper:

    def __init__(self, app):
        self.app=app

    def open_new_add_pages(self):
        # open add new page and init new client
        wd = self.app.wd
        if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("add next")) >0 :
            wd.find_element_by_link_text("add next").click()
        wd.find_element_by_link_text("add new").click()


    def create_new_client(self, client):
        # fill client form
        wd = self.app.wd
        self.open_new_add_pages()
        self.full_client_firm(client)
        # submit new client
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def full_client_firm (self, client):
        wd = self.app.wd
        self.edit_field_value("firstname", client.name)
        self.edit_field_value("middlename", client.middlename)
        self.edit_field_value("title", client.title)
        self.edit_field_value("address", client.address)
        self.edit_field_value("home", client.home)
        self.edit_field_value("mobile", client.mobile)
        self.edit_field_value("work", client.work)
        self.edit_field_value("fax", client.fax)
        self.edit_field_value("email", client.email)
        self.edit_field_value("email2", client.email2)
        self.edit_field_value("email3", client.email3)
        self.edit_date_value("bday", client.bday)
        self.edit_date_value("bmonth", client.bmonth)
        self.edit_field_value("byear", client.byear)
        self.edit_date_value("aday", client.aday)
        self.edit_date_value("amonth", client.amonth)
        self.edit_field_value("ayear", client.ayear)
        self.edit_field_value("address2", client.address2)
        self.edit_field_value("phone2", client.phone2)



    def edit_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_date_value(self, field_value, value):
        wd = self.app.wd
        if value is not "-":
            wd.find_element_by_name(field_value).click()
            Select(wd.find_element_by_name(field_value)).select_by_visible_text(value)
            wd.find_element_by_name(field_value).click()


    def delete_first_client(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_client()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def select_first_client(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_client(self, new_client_date):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_client()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.full_client_firm(new_client_date)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()


    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))