# Selectors

## Why Selectors
In [Lesson 1](https://github.com/estasney/Master_Builders/blob/master/Courses/Lesson%201%20-%20HTML.md) we explored the basic building blocks of the web, HTML. 

Now think of a web page as a city and each HTML block as a building in the city.

As with every city, each building will have its own address. As you'll soon find out, there are quite a few ways to navigate our city!

## Selectors Are GPS for your Browser
Let's imagine we want to get across town to *Talent Hub's Pizza Palace*. Oh and now it's a food truck.

We could:
1. Google the Address and drive directly to it. (**A Direct Approach**)
2. Ask for directions (**An Indirect Approach**)

### Direct Approaches
*Target Acquired!*

##### Monday
You have provided the exact GPS coordinates for *Pizza Palace*. You get some delicious pizza.

##### Friday
You use the same GPS coordinates for *Pizza Palace*. Unfortunately for you, *Pizza Palace* is a food truck and will always be on the move!
While it was easy to Google the coordinates on Monday, you now find yourself having to Google the coordinates every time
you want some delicious pizza.

Now imagine that each time you open a page, the day of the week changes. You will then understand why **Direct Approaches**
can be **fragile**.

### Indirect Approaches
*Using the Force!*

##### Monday
You have the GPS coordinates for *Pizza Palace* but this time you ask a few locals where you can find it. Since it's a food truck, that's a smart move.


Person 1: Look for a "Red" truck

Person 2: *Pizza Palace* sells their pizza to employees in the Business District.

Person 3: The *Pizza Palace* truck is the only one to play music in the Business District.

##### How do we make sense of these directions?
If we asked just one person, the directions they gave us would certainly not be enough to find our food truck.

Now let's visualize the city as HTML and populate it with some food trucks:

```HTML
<city>
<suburbs>
    <food_truck color="blue" music="Classic Rock">Ribs Are Good</food_truck>
</suburbs>
<downtown>
    <food_truck color="red" music="Sourcing Disco">Pizza Palace</food_truck>
    <business_district>
        <food_truck color="red" music="Sourcing Disco">Talent Hub's Pizza Palace</food_truck>
        <food_truck color="red" music="Classic Rock">Ribs Is Good!</food_truck>
    </business_district>
</downtown>
</city>

```

Did you spot the imposter food truck? Yes, it appears another food truck is trying to copy everything about *Talent Hub's Pizza Palace*!

As you can see, a **Direct Approach** would have failed because of the imposter.

However, if "navigate" to the business district first, and then look for the foodtruck playing "Sourcing Disco", we would succeed!

### Homework
- [ ] Install [Selenium IDE](https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/)
**Note** If you see a message saying the add-on is not compatible, use this [Guide](https://github.com/estasney/Master_Builders/blob/master/Resources/Installing%20Selenium%20IDE.md)
- [ ] Using Selenium IDE, try to automate something!
- [ ] Automate something using Selenium IDE's Record Feature (enabled by default)
- [ ] Try changing one parameter and see if it still works. (Example: searching for a different product on Amazon)
- [ ] When it breaks, take notes on the website you were on and what you were trying to do. We'll share these on the call.

#### Word About XPATH vs CSS
There are two methods for navigating a web page. When you are first starting, I would recommend choosing one that you feel most comfortable with and mastering it.

They both have similar capabilities, their major difference is syntax. What do you find easiest to read and write?

XPATH: ```//*[@id="readme"]/article/h1```

CSS : ```#readme > article > h1```

#### Learning Resources
1. W3Schools [CSS Selector Demo](https://www.w3schools.com/cssref/trysel.asp)
2. W3Schools [XPATH Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)
3. W3Schools [CSS Selector](https://www.w3schools.com/cssref/css_selectors.asp)

### Extra Credit
- [ ] - Make a Price Tracker. Every day get a price and log it to a spreadsheet.

***

### Enough Analogies Already

***

Take a look at this example [Indeed Page](https://www.indeed.com/resumes?q=software+engineer&l=Morrisville%2C+PA&cb=jt)

Let's try to write a CSS Selector To Select the 3rd Element. Start by pressing <kbd>F12</kbd>. This will open Chrome Developer Tools.

We will use the handy "Copy Selector" feature.

![](https://thumbs.gfycat.com/GentleHelplessChihuahua-size_restricted.gif)

***

While we got a working selector for the first page, from the above animation, we see that it does not work if we go to the next page.

Here's the selector we got:

```#\38 4deb8b2982b75be > div > div.sre-content > div.app_name > a```

Remember that with CSS Selectors a ">" indicates a direct path. So let's break it down by <kbd>></kbd>:

```#\38 4deb8b2982b75be > div > div.sre-content > div.app_name > a```

Right off the bat, we see this as our first selector:

```#\38 4deb8b2982b75be```

OK we see the <kbd>#</kbd> sign which indicates that we are looking at an **ID** attribute. If we look at some other results on the page
we see that each result has a unique **ID**. So Chrome will steer us wrong if we use the copy selector/xpath feature.

In case you wanted to see what it gives for XPATH...

```//*[@id="9038ee8495cec959"]/div/div[2]/div[1]/a```

Here it is more clear that we are looking for elements based on their **ID** attribute.

***

Get ready this will be your first exercise in thinking like a programmer. We want to select the 3rd result on every page, so how can we
translate that for a computer to understand?

We know that on every page, there will be no more than 50 results. It really doesn't matter how many there are, so long as there are at least 3.

We see that the element

```<ol id="results" class="resultsList" data-tn-section="resume-search-results">```

Is the direct ancestor or parent of each result on the page. If we can write a selector that uses the ```<ol>``` element as a reference point
we can then point it towards the 3rd of its 50 (more or less) children. These children will have different **IDs**, but will be able to select them by position.

We begin by selecting the ```<ol>``` element.

```html
<ol id="results" class="resultsList" data-tn-section="resume-search-results">
```

It looks like there are a few hopefully unique attributes of ```<ol>``` that we can use. 

XPATH | CSS | Notes | Results | Why
--- | --- | --- | --- | ---
//ol | ol | Start with ol tag found anywhere on page | PASS | There is only one ```<ol>```
//ol[@id='results'] | ol#results | Select an ol tag with an id of "results" | PASS | Any selection with ```<ol>``` will pass
//ol[@class='resultsList] | ol.resultsList | Select on class attribute | PASS | See above
//*[@id='results] | #results | Wildcards | PASS | 'results' is a unique ID


![](https://thumbs.gfycat.com/KeyEnormousErin-size_restricted.gif)

***

You've see how we can locate the ```<ol>``` element using a number of different methods with XPATH and CSS.

Now it's a simple matter of selecting the "3rd child" of the ```<ol>``` element.

XPATH | CSS | Notes | Results | Why
--- | --- | --- | --- | ---
//ol//li[3] | ol li:nth-of-type(3) | We select the "3rd element" and allow for any hierachies between ```<ol>``` and ```<li>``` | PASS |
//*//li[3] |  li:nth-of-type(3) | We use a wildcard for ```<ol>``` | FAIL | We get 6 results. The side menu has a ```<ul>``` element as parent of ```<li>``` elements
//ol/li[3] | ol > li:nth-of-type(3) | We select immediate ```<li>``` children of ```<ol>``` only | PASS |

![](https://thumbs.gfycat.com/LeafyGrandGemsbok-size_restricted.gif)






### Group Call
- [ ] - CSS
- [ ] - XPATH
- [ ] - Tools for Finding Selectors
- [ ] - Demo Selenium IDE Price Tracker
- [ ] - Demo Python Price Tracker
- [ ] - Demo Windows Task Scheduler
