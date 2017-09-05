from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pandas as pd
import csv
import easygui
import time
import sys

"""

PARAMETERS HERE

"""
path_in = easygui.fileopenbox("Open the file you wish to check for duplicates")
path_out = easygui.filesavebox("Choose where to save the results of the DupCheck")
path_in_encoding = 'windows-1252'
path_to_chrome = r"C:\Users\estasney\Documents\ChromeDriver\chromedriver.exe"
patience_in_seconds = 5  # How many seconds you are willing to wait for a page to load
all_people_list_url = "https://cisco.avature.net/#People/Id:2266/Filters:{\"entityTypeId\":2,\"id\":396094,\"set\":null,\"timeZone\":\"America*/New_York\"}"

"""

CHANGE HEADER NAMES AS NEEDED HERE

"""
dup_check_data = pd.read_csv(path_in, encoding=path_in_encoding)

fname_col = dup_check_data['First Name']
lname_col = dup_check_data['Last Name']
hemail_col = dup_check_data['Home Email']
wemail_col = dup_check_data['Work Email']
aemail_col = dup_check_data['Additional Email']
li_url_col = dup_check_data['LinkedIn Profile']
rec_url_col = dup_check_data['Linkedin Recruiter URL']

"""

END PARAMETERS

"""

def dup_check_avature(dupcheck_key):
    add_filter_menu = avature_driver.find_element_by_xpath("//div[3]/div/span/span")
    add_filter_menu_hover = ActionChains(avature_driver).move_to_element(add_filter_menu)
    add_filter_menu_hover.perform()
    add_filter_menu.click()
    keyword_filter = avature_driver.find_element_by_css_selector("div.FloatingMenuButton:nth-child(7) > span:nth-child(1) > span:nth-child(2)")
    keyword_filter.click()
    filter_textbox = avature_driver.find_element_by_xpath("//textarea")
    filter_textbox.send_keys(dupcheck_key)
    filter_textbox.send_keys(u'\ue007')
    filter_apply_button = avature_driver.find_element_by_xpath("//button")
    time.sleep(2)
    filter_apply_button.click()
    time.sleep(3)
    try:
        dup_results = avature_driver.find_element_by_css_selector(".uicore_list_NoResultsMessage")
        dup_results_test = False
    except:
        dup_results_test = True
    # Clear the filter search
    filter_hyperlink = avature_driver.find_element_by_css_selector("a.list_conditionsviewer_ItemValuePopupLink_Link")
    filter_hyperlink_hover = ActionChains(avature_driver).move_to_element(filter_hyperlink)
    filter_hyperlink_hover.perform()
    filter_hyperlink.click()
    filter_hyperlink_remove = avature_driver.find_element_by_link_text("Remove filter")
    filter_hyperlink_remove_hover = ActionChains(avature_driver).move_to_element(filter_hyperlink_remove)
    filter_hyperlink_remove_hover.perform()
    filter_hyperlink_remove.click()
    time.sleep(5)
    return dup_results_test


class LeadPerson(object):

    def __init__(self, fname, lname, hemail, wemail, aemail, li_url, rec_url):
        self.fname = self.blank_test(fname)
        self.lname = self.blank_test(lname)
        self.hemail = self.blank_test(hemail)
        self.wemail = self.blank_test(wemail)
        self.aemail = self.blank_test(aemail)
        self.li_url = self.blank_test(li_url)
        self.rec_url = self.blank_test(rec_url)
        self.dupcheckkey = self.dup_key()

    def blank_test(self, value_passed):  # Pandas treats blank cells as "NaN" This will set "NaN" to ""
        if str(value_passed).lower() == 'nan':
            return ""
        else:
            return str(value_passed)

    def dup_key(self):
        try:
            li_key = self.li_url.split("/in/")[1]
        except IndexError:
            li_key = ""
        try:
            rec_key = self.rec_url.split("/profile/")[1].split("?")[0]
        except IndexError:
            rec_key = ""

        if li_key and rec_key:
            url_key = li_key + " OR " + rec_key
        elif li_key:
            url_key = li_key
        elif rec_key:
            url_key = rec_key
        else:
            url_key = ""

        h_key = self.hemail
        w_key = self.wemail
        a_key = self.aemail

        email_key = ""

        if h_key:
            email_key = email_key + h_key
        if w_key:
            email_key = email_key + " OR " + w_key
        if a_key:
            email_key = email_key + " OR " + a_key

        return url_key + " OR " + email_key


lead_person_holder = []  # This will hold the LeadPerson objects as we create them

for fname, lname, hemail, wemail, aemail, li_url, rec_url in zip(fname_col, lname_col, hemail_col, wemail_col,
                                                                 aemail_col, li_url_col, rec_url_col):
    created_lead = LeadPerson(fname, lname, hemail, wemail, aemail, li_url, rec_url)
    lead_person_holder.append(created_lead)

"""

DATA IS LOADED INTO OBJECTS, START BROWSER AUTOMATION

"""

avature_driver = webdriver.Chrome(executable_path=path_to_chrome)
avature_driver.implicitly_wait(patience_in_seconds)
avature_driver.get("https://cisco.avature.net")
await_avature_login = easygui.ccbox("Are You Logged In to Avature?")
if await_avature_login:
    pass
else:
    easygui.msgbox("Quitting Program")
    avature_driver.quit()
    sys.exit()

avature_driver.get(all_people_list_url)

# Start Checking

for lead in lead_person_holder:
    dup_check_test = dup_check_avature(lead.dupcheckkey)
    fname = lead.fname
    lname = lead.lname
    hemail = lead.hemail
    wemail = lead.wemail
    aemail = lead.aemail
    li_url = lead.li_url
    rec_url = lead.rec_url
    dup_key_ran = lead.dupcheckkey
    try:
        with open(path_out, "a+", encoding='utf-8', newline='') as csv_file:
            outputwriter = csv.writer(csv_file, dialect='excel')
            if dup_check_test is True:
                dup_status = "POSSIBLE DUPLICATE"
                outputwriter.writerow([dup_status, fname, lname, hemail, wemail, aemail, li_url, rec_url, dup_key_ran])
            elif dup_check_test is False:
                dup_status = "NO DUPLICATES FOUND"
                outputwriter.writerow([dup_status, fname, lname, hemail, wemail, aemail, li_url, rec_url, dup_key_ran])
    except:
        with open(path_out, "a+", encoding='utf-8', newline='') as csv_file:
            outputwriter = csv.writer(csv_file, dialect='excel')
            dup_status = "ERROR CHECKING PROFILE"
            outputwriter.writerow([dup_status, fname, lname, hemail, wemail, aemail, li_url, rec_url, dup_key_ran])



