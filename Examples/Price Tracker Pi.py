import csv
from time import localtime, strftime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import signal
import argparse

#  PARAMETERS HERE
csv_save_file = "price_tracker_me.csv"
# csv_save_file = '/home/pi/pricetracker/price_tracker.csv'
# phantom_driver = '/usr/bin/phantomjs'
phantom_driver = r"C:\Users\erics_qp7a9\Documents\phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe"


class Product(object):  # Every product we monitor is in this class

    def __init__(self, product_page, product_name, vendor_name, selector, selector_method, csv_path, extraction_method,
                 timeout=30, error_threshold=2):
        self.product_page = product_page
        self.product_name = product_name
        self.vendor_name = vendor_name
        self.selector = selector  # Expects tuple
        capabilities = dict(DesiredCapabilities.PHANTOMJS)
        capabilities["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
            "(KHTML, like Gecko) Chrome/15.0.87")
        self.driver = webdriver.PhantomJS(executable_path=phantom_driver, desired_capabilities=capabilities)
        self.driver.implicitly_wait(timeout)
        self.error_threshold = error_threshold
        self.error_count = 0
        self.csv_path = csv_path
        self.product_holder = []
        self.product_price = None
        self.extraction_method = extraction_method
        self.selector_method = selector_method

    def log_error(self):
        self.error_count += 1
        if self.error_count < self.error_threshold:
            self.run_product_checker()
        else:
            print("Error Threshold Reached")
            self.hard_exit()


    def save_results(self):
        with open(self.csv_path, "a", encoding='utf-8', newline='') as csv_file:
            writeit = csv.writer(csv_file, dialect='excel')
            scrape_time = strftime("%D", localtime())
            writeit.writerow([scrape_time, self.product_name, self.vendor_name, self.product_price])

    def hard_exit(self):
        driver.service.process.send_signal(signal.SIGTERM)  # kill the specific phantomjs child proc
        driver.quit()

    def run_product_checker(self):
        try:
            driver = self.driver
            driver.get(self.product_page)
            if self.selector_method == 'link text':
                product_element = driver.find_element_by_link_text(self.selector)
            elif self.selector_method == 'css':
                product_element = driver.find_element_by_css_selector(self.selector)
            elif self.selector_method == 'xpath':
                product_element = driver.find_element_by_xpath(self.selector)
            elif self.selector_method == 'class':
                product_element = driver.find_element_by_class_name(self.selector)
            elif self.selector_method == 'tag':
                product_element = driver.find_element_by_tag_name(self.selector)
            elif self.selector_method == 'part link text':
                product_element = driver.find_element_by_partial_link_text(self.selector)

            transform_text = self.extraction_method(product_element)
            self.product_price = transform_text
            self.save_results()
            self.hard_exit()
        except:
            self.log_error()

"""
ADD PRODUCTS HERE
                """

 # Lowe's Grass Seed

lowes_grass_page = "https://www.lowes.com/pd/Scotts-40-lb-Tall-Fescue-Southern-Gold-Seed/50076909"
lowes_grass_name = "Southern Gold"
lowes_grass_selector = "span[itemprop='price']"
lowes_grass_selector_method = 'css'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument()


def lowes_grass_method(element):
    price = element.get_attribute('content')
    return price

# Home Depot Grass Seed


hd_grass_page = "https://www.homedepot.com/p/Scotts-40-lb-Southern-Gold-Grass-Seed-19004/205524501"
hd_grass_name = "Southern Gold"
hd_grass_selector = "#ciItemPrice"
hd_grass_selector_method = 'css'

def hd_grass_method(element):
    price = element.get_attribute('value')
    return price

lowes_tracker = Product(product_page=lowes_grass_page, product_name=lowes_grass_name, vendor_name="Lowe's",
                        selector=lowes_grass_selector, selector_method=lowes_grass_selector_method, csv_path=csv_save_file, extraction_method=lowes_grass_method())

lowes_tracker.run_product_checker()