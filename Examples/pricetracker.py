import csv
from time import localtime, strftime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class Product(object):  # Every product we monitor is in this class

    def __init__(self, product_page, product_name, vendor_name, selector):
        self.product_page = product_page
        self.product_name = product_name
        self.vendor_name = vendor_name
        self.selector = selector  # Expects tuple


class PriceTracker(object):

    def __init__(self, save_location, visibility, chrome_path, phantom_path):
        self.product_dict = {}  # Expects a list of Product objects
        self.save_location = save_location
        self.error_count = 0
        self.chrome_path = chrome_path
        self.phantom_path = phantom_path
        self.driver = self.load_driver(visibility)


    def load_driver(self, visibility):
        if visibility == 1:
            driver = webdriver.Chrome(executable_path=self.chrome_path)

        elif visibility == 0:
            capabilities = dict(DesiredCapabilities.PHANTOMJS)
            capabilities["phantomjs.page.settings.userAgent"] = (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
                "(KHTML, like Gecko) Chrome/15.0.87")
            driver = webdriver.PhantomJS(desired_capabilities=capabilities, executable_path=self.phantom_path)

        driver.implicitly_wait(20)
        return driver

    def add_Product(self, product):

        self.product_dict[product] = product


    def track_Product(self, product):
        active_product = self.product_dict[product]
        url_of_product = active_product.product_page
        name_of_product = active_product.product_name
        vendor_of_product = active_product.vendor_name
        selector_of_product = active_product.selector
        self.driver.get(url_of_product)
        tracked_timestamp = strftime("%D", localtime())
        if selector_of_product[0] == 'XPATH':
            try:
                product_price = self.driver.find_element_by_xpath(selector_of_product[1])
            except:
                product_price = "Error Getting Product"
        elif selector_of_product[0] == 'CSS':
            try:
                product_price = self.driver.find_element_by_css_selector(selector_of_product[1])
            except:
                product_price = "Error Getting Product"
        else:
            print("Invalid Selector Type")
            print("Expects tuple of format (CSS|XPATH, Selector)")
            return False
        with open(self.save_location, "a+", encoding='utf-8', newline='') as csv_file:
            outputwriter = csv.writer(csv_file, dialect='excel')
            outputwriter.writerow([tracked_timestamp, name_of_product, product_price, vendor_of_product])
        return True

    def track_All(self):
        for product in self.product_dict.values():
            run_track_case = self.track_Product(product)
            if run_track_case is True:
                continue
            elif run_track_case is False:
                self.error_count = self.error_count + 1
        self.driver.quit()
        print("Tracking Complete!")
