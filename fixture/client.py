from selenium.webdriver.support.ui import Select
from model.client import Client

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
        self.client_cache = None
    def full_client_firm (self, client):
        wd = self.app.wd
        self.edit_field_value("firstname", client.name)
        self.edit_field_value("middlename", client.middlename)
        self.edit_field_value("lastname", client.lastname)
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
        if value != "-":
            wd.find_element_by_name(field_value).click()
            Select(wd.find_element_by_name(field_value)).select_by_visible_text(value)
            wd.find_element_by_name(field_value).click()

    def delete_first_group(self):
        self.delete_client_by_index(0)

    def delete_client_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_client_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.client_cache = None


    def select_first_client(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_client(self):
        self.edit_client_by_index(0)

    def edit_client_by_index(self, index, new_client_date):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_client_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.full_client_firm(new_client_date)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.client_cache=None

    def select_client_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    client_cache=None

    def get_client_list(self):
        if self.client_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.client_cache = []
            for element in wd.find_elements_by_xpath("//*[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                secoundname = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.client_cache.append(Client(id=id, name=firstname, middlename=secoundname))
        return list(self.client_cache)