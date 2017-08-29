import csv
from time import localtime, strftime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#  We want to regularly check the prices of a few items online.

#  Since we will be scheduling this task, it would be nice to not see it run in case it's distracting.

#  We use phantom.js. A browser that runs without being visible

"""
PARAMETERS HERE

"""
csv_save_file = r"C:\Users\estasney\Google Drive\Cisco\Extracts\Price Tracker\price_tracker.csv"
phantom_path = r"C:\Users\estasney\Documents\ChromeDriver\phantomjs-2.1.1-windows\bin\phantomjs.exe"
chrome_path = r"C:\Users\estasney\Documents\ChromeDriver\chromedriver.exe"

# We want phantom.js to masquerade as a real browser

capabilities = dict(DesiredCapabilities.PHANTOMJS)
capabilities["phantomjs.page.settings.userAgent"] = (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
                "(KHTML, like Gecko) Chrome/15.0.87")
"""
PRODUCTS TO TRACK GO HERE

"""

# Grass Seed

product_pages = ["https://www.lowes.com/pd/Scotts-40-lb-Tall-Fescue-Southern-Gold-Seed/50076909"]
product_names = ["Southern Gold, 40 Lbs"]
vendor_names = ["Lowes"]

"""
WRITING A FUNCTION SO WE KNOW THE DAY AND TIME IT RAN
"""

def get_the_time():
    the_time = strftime("%D %I:%M %p", localtime())
    return the_time


"""
BEGIN SCRIPT
"""

driver = webdriver.PhantomJS(desired_capabilities=capabilities, executable_path=phantom_path, service_log_path=r"C:\Users\estasney\Google Drive\Cisco\Extracts\Price Tracker\tracker_log.log")

# Load Page
driver.get(product_pages[0])

# The price is not conveniently on the page as text. However it is in the content attribute of a nearby <span> element
price_element = driver.find_element_by_xpath("//span[@itemprop='price']")
price_text = price_element.get_attribute("content")

# Save it to CSV
with open(csv_save_file, "a+", encoding="utf-8", newline='') as csv_file:
    write_to_csv = csv.writer(csv_file, dialect='excel')
    the_time = get_the_time()
    write_to_csv.writerow([the_time, product_names[0], vendor_names[0], price_text])







