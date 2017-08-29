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

## Enough Analogies Already

Take a look at this example [Indeed Page](https://www.indeed.com/resumes?q=software+engineer&l=Morrisville%2C+PA&cb=jt)

Now you can see how navigating and writing robust CSS and XPATH Selectors is important!

To demonstrate the concept of Children and Ancestors, I made this [explorable graph](http://jsfiddle.net/estasney/ytz5hh1x/3/embedded/result/) that might help you better understand the structure of a page.

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
- [ ]Make a Price Tracker. Every day get a price and log it to a spreadsheet.


### Group Call
- [ ] - CSS
- [ ] - XPATH
- [ ] - Tools for Finding Selectors
- [ ] - Demo
