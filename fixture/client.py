from selenium.webdriver.support.ui import Select
from model.client import Client
import re

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

    def delete_client_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_client_by_id(id)
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

    def edit_client_by_id(self, id, index, new_client_date):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()
        self.select_client_by_id(id)
        wd.find_element_by_xpath("edit").click()
        #row = wd.find_elements_by_name("entry")[id]
        #cell = row.find_elements_by_tag_name("td")[7]
        #cell.find_element_by_tag_name("a").click()
        self.full_client_firm(new_client_date)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.client_cache=None


    def select_client_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_client_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']"%id).click()


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
                all_phones=cells[5].text
                all_emails=cells[4].text
                self.client_cache.append(Client(id=id, name=firstname, lastname=secoundname,
                                                all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.client_cache)

    def open_client_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_client_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_client_to_edit_by_index(index)
        firstname=wd.find_element_by_name("firstname").get_attribute("value")
        lastname=wd.find_element_by_name("lastname").get_attribute("value")
        id=wd.find_element_by_name("id").get_attribute("value")
        home=wd.find_element_by_name("home").get_attribute("value")
        work=wd.find_element_by_name("work").get_attribute("value")
        mobile=wd.find_element_by_name("mobile").get_attribute("value")
        phone2=wd.find_element_by_name("phone2").get_attribute("value")
        email=wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Client(name=firstname, lastname=lastname, id=id, home=home,
                      mobile=mobile, work=work, phone2=phone2, email=email, email2=email2, email3=email3)


    def get_client_from_view_page(self, index):
        wd = self.app.wd
        self.open_client_view_by_index(index)
        text=wd.find_element_by_id("content").text
        home=re.search("H: (.*)", text).group(1)
        mobile=re.search("M: (.*)", text).group(1)
        work=re.search("W: (.*)", text).group(1)
        phone2=re.search("P: (.*)", text).group(1)
        firstname=wd.find_element_by_name("firstname").get_attribute("value")
        lastname=wd.find_element_by_name("lastname").get_attribute("value")
        email = re.search("/n: (.*)", text).group(1)
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Client(name=firstname, lastname=lastname, home=home,mobile=mobile, work=work, phone2=phone2)

