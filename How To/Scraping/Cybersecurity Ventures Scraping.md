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

