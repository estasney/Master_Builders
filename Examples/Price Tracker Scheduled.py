from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv
from time import localtime, strftime
#  We want to regularly check the prices of a few items online.

#  Since we will be scheduling this task, it would be nice to not see it run in case it's distracting.

#  PARAMETERS HERE
csv_save_file = r"C:\Users\estasney\Google Drive\Cisco\Extracts\Price Tracker"
phantom_driver = r"C:\Users\estasney\Documents\ChromeDriver\phantomjs-2.1.1-windows\bin\phantomjs.exe"


capabilities = dict(DesiredCapabilities.PHANTOMJS)
capabilities["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87")

driver = webdriver.PhantomJS(desired_capabilities=capabilities, executable_path=phantom_driver)
driver.implicitly_wait(20)

class Product(object):  # Every product we monitor is in this class

    def __init__(self, product_page, product_name, selector):
        self.product_page = product_page
        self.product_name = product_name
        self.selector = selector  # Expects tuple



class PriceTracker(object):

    def __init__(self, save_location):
        self.product_dict = {}  # Expects a list of Product objects
        self.save_location = save_location


    def add_Product(self, product):
        self.product_dict[product] = product

    def track_Product(self, product):
        active_product = self.product_dict[product]
        url_of_product = active_product.product_page
        name_of_product = active_product.product_name
        selector_of_product = active_product.product_name
        driver.get(url_of_product)
        tracked_timestamp = strftime("%D", localtime())
        if selector_of_product[0] == 'XPATH':
            product_price = driver.find_element_by_xpath(selector_of_product[1])
        elif selector_of_product[0] == 'CSS':
            product_price = driver.find_element_by_xpath(selector_of_product[1])
        else:
            print("Invalid Selector Type")
            print("Expects tuple of format (CSS|XPATH, Selector)")
            return False
        with open(self.save_location, "a+", encoding='utf-8', newline='') as csv_file:
            outputwriter = csv.writer(csv_file, dialect='excel')
            outputwriter.writerow([tracked_timestamp, name_of_product, product_price])
        return True

