# Scraping a Cybersecurity Measures

1. [The Site](https://cybersecurityventures.com/cybersecurity-500-list/#home/?view_1_per_page=500&view_1_page=1)


### Data Structure

Number | Company | Cybersecurity Sector | Corporate HQ | Info
 --- |--- | --- | --- | ---
[Herjavec Group](http://www.herjavecgroup.com/) | Information Security Services | Toronto, Canada | [View](https://cybersecurityventures.com/cybersecurity-500-list/#home/viewdetails/54c916122239d0df404c9988?ref=view_1_per_page%3D500%26view_1_page%3D1)


#### Analyze The Page Structure

We always start by analyzing the page structure to see how it is laid out
![](https://thumbs.gfycat.com/BothHardClam-size_restricted.gif)
***

We see that all rows are direct children of ```<tbody>```.

Each row is a ```<tr>``` element.

Each column in a row is a ```<td>``` element.

Number | Company | Cybersecurity Sector | Corporate HQ | Info
--- | --- | --- | --- | ---
td[1] | td[2] | td[3] | td[4] | td[5]

#### Choose a strategy

There are multiple ways to go about this. Perhaps the fastest would be to use JavaScript.

For demonstration purposes we will use Selenium (with Python). Since we will want to save the data it makes sense to use this method.

***


#### Getting Our Scraper Prepared
```Python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

site_url = "https://cybersecurityventures.com/cybersecurity-500-list/#home/?view_1_per_page=500&view_1_page=1"
path_to_chrome = r"C:\Users\erics_qp7a9\PycharmProjects\Scraping\chromedriver.exe"  # Where chromedriver was saved to. Best to specify this. "r" is used for telling Python to treat the file path as a string literal.
driver = webdriver.Chrome(executable_path=path_to_chrome)  # We choose driver as the variable name for our scraper
```

#### Now, Scrape It!
##### Company Names
```Python
company_names_elements = driver.find_elements_by_xpath("//tbody/tr/td[2]//a")
company_names = []
for i in range(500):
    company_name = company_names_elements[i].get_attribute("textContent").strip()  # Strip is needed as some rows include "\n" which is computer speak for "create a new line". We don't want that.
    company_names.append(company_name)

company_links = []  # We don't need to get a new list of elements again here as we are still working with the same list, just getting the links instead of the text out of them.
for i in range(500):
    company_link = company_names_elements[i].get_attribute("href")
    company_links.append(company_link)
```

##### This is somewhat repetitive
```Python
sector_elements = driver.find_elements_by_xpath("//tbody/tr/td[3]/span")

sectors = []
for i in range(500):
    sector_row = sector_elements[i].get_attribute("textContent").strip()
    sectors.append(sector_row)
hq_elements = driver.find_elements_by_xpath("//tbody/tr/td[4]/span")

hq_list = []
for i in range(500):
    hq_row = hq_elements[i].get_attribute("textContent").strip()
    hq_list.append(hq_row)

info_link_elements = driver.find_elements_by_xpath("//tbody/tr/td[5]//a")

info_list = []
for i in range(500):
    info_row = info_link_elements[i].get_attribute("href")
    info_list.append(info_row)
```

##### Now we just need to save it to a CSV spreadsheet.
**Note**: You may not have seen the ```zip()``` command. It's used and useful when working with multiple lists like we have here. So we can create a ```for``` loop that iterates through each of the lists within the ```zip()``` command
```Python
path_out = # Put your save location here
with open(path_out, "w+", encoding='utf-8', newline='') as csv_file:
    outputwriter = csv.writer(csv_file, dialect='excel')
    for company_name, company_link, sector, hq_location, info_link in zip(company_names, company_links, sectors, hq_list, info_list):
        outputwriter.writerow([company_name, company_link, sector, hq_location, info_link])
```

##### And Done!