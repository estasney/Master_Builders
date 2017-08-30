# Price Tracker
## Table of Contents
1. [How Selectors are Used](https://github.com/estasney/Master_Builders/blob/master/Courses/Lesson%202.5%20-%20Selenium%20IDE.md#a-practical-use-for-xpath-and-css-selectors)
2. [Prep Work](https://github.com/estasney/Master_Builders/blob/master/Courses/Lesson%202.5%20-%20Selenium%20IDE.md#the-google-forms-solution)
3. [Making a Price Tracker](https://github.com/estasney/Master_Builders/blob/master/Courses/Lesson%202.5%20-%20Selenium%20IDE.md#lets-start-automating)
## A Practical Use for XPATH and CSS Selectors
Once you've gotten the hang of XPATH and/or CSS Selectors in [Lesson 2](https://github.com/estasney/Master_Builders/blob/master/Courses/Lesson%202%20-%20Selectors.md), it's time to put your knowledge to use!

If you're skipping around, we'll be using Selenium IDE with Firefox. If you have it successfully installed, great. Otherwise see this [Guide](https://github.com/estasney/Master_Builders/blob/master/Resources/Installing%20Selenium%20IDE.md) on installing it.

## Some Quick Prep Work

Selenium IDE isn't intended for data-driven uses like our price tracker will require. However, if we remember that as Master Builders, we specialize in the *unintended* we can craft a solution.

You'll notice that there is not direct support for saving our prices to our PC's. Which is obviously a necessity if we want to track anything over time.

### The Google Forms Solution
I came upon this genius solution in a random post on Stack Overflow so I can't take credit for it, but I *can* highly recommend it as an effective workaround.

I'll assume you have a Google account.

What we want to do is to create a Google Form that our Price Tracker can visit and enter the price it found for the day and then click the Submit button.

#### Create the Form

I recommend *not* using a Randstad Google account as pictured. This is because the sharing settings for forms are overly restrictive.
***
![](https://thumbs.gfycat.com/TenderAbleFlycatcher-size_restricted.gif)
***
***
#### Edit a few things
***
- [ ] - Name it something
- [ ] - Give Question 1 a Title
- [ ] - Set Answer Type as Short Answer
- [ ] - Keep the URL Handy
***
![](https://thumbs.gfycat.com/RewardingCanineDoe-size_restricted.gif)
***
***
## Let's Start Automating!
***
Before we get started, you may see that some GIFs are from Chrome. That is because I prefer the speed and layout of Chrome's developer tools.
Feel free to use Firefox's if it is to your liking.

- [ ] - Open Firefox and Selenium IDE
- [ ] - Add a shortcut to Selenium IDE
***
![](https://thumbs.gfycat.com/GlossyCourageousIsabellinewheatear-size_restricted.gif)
***

- [ ] - Disable Record On Open
***
![](https://thumbs.gfycat.com/InfamousPettyCheetah-size_restricted.gif)
***

For this example, we'll be tracking the price of the *DoughXpress D-TXE-2-18 Stainless Steel Commercial Electromechanical Dual-Heated Press* for our *Pizza Palace Empire*

Here's the page we'll use [Pizza Maker](https://www.amazon.com/DoughXpress-D-TXE-2-18-Commercial-Electromechanical-Dual-Heated/dp/B004JPB5CE)


- [ ] - Get The Selector for the Price

***

Use your XPATH and CSS Knowledge to Determine the selector for the price. Remember you can right-click on an element to find it directly in Developer Tools.

Here's the element the price exists in:

```HTML
<span id="priceblock_ourprice" class="a-size-medium a-color-price">$6,890.00</span>
```

OK can you think of a few XPATH and/or CSS Selectors that would work here? Let's set up a table:

Strategy | XPATH | CSS | Results
 --- |--- | --- | ---
 Find a ```<span>``` element anywhere on page | //span | span | FAIL - 973 Results, Too Broad
 Find a ```<span>``` element anywhere on page with id=priceblock_ourprice| //span[@id='priceblock_ourprice'] | span#priceblock_ourprice | PASS
 Find a ```<span>``` element by class | //span[@class='a-size-medium a-color-price'] | span.a-size-medium.a-color-price | PASS (See Note)
 

Note From Table: With CSS Selectors, when an attribute contains a space, you treat it as an additional atrtibute. So in this example we write it with two class attributes.

We have to two selectors that we can use! But the id and class names look as if they could change. We should try to find another selector that is more robust. Websites change so it's important to be able to handle those changes.

If we look higher up in the HTML Hierarchies, we come across ```<div id="price_feature_div" class="feature" data-feature-name="price">```
This looks like more solid ground. We could use this as a landmark to the price without relying on the ```<span>``` tag's id and class names
***
##### Another Table
***
Strategy | XPATH | CSS | Results
 --- |--- | --- | ---
Use the ```<div>``` data-feature-name, jump to ```<span>```| //div[@data-feature-name='price']//span | div[data-feature-name='price'] span | FAIL, 4 Results
Use the ```<div>``` data-feature-name, jump to the first```<span>``` | //div[@data-feature-name='price']//span[1] | Use the ```<div>``` data-feature-name, jump to ```<span>```| FAIL, 2 Results


Let's see what's happening with our second row, it's a great opportunity to learn!
***
![](https://thumbs.gfycat.com/FittingEsteemedArieltoucan-size_restricted.gif)
***

Our selector is *nearly* there we just need to make sure we don't include the second ```<span>``` element. We can use filters of XPATH and CSS that select for elements with direct parents that are ```<td>``` elements.

I didn't know the syntax to do this off-hand so here's what I Googled. I hope this shows how the right searches can make a world of difference for finding answers:

**xpath direct ancestor is element**

We see from this [post](https://stackoverflow.com/questions/3005370/xpath-to-find-nearest-ancestor-element-that-contains-an-element-that-has-an-attr) on Stackoverflow how to write this

```root/foo/bar[ancestor::foo[bar[@attr="val"]]```

Since the other ```<span>``` element also has the same ancestor we should use parent vs ancestor. Our selector is now:

```//div[@data-feature-name='price']//span[1][parent::td]```

We test it and it works!


*** 

The process of finding the right selector is 95% of the process of automation. But now that we have one for the price, we can integrate this with Selenium IDE.

**Commands Learned** - storeText


***
![](https://thumbs.gfycat.com/ViciousTangibleHuman-size_restricted.gif)
***

Now that the price has been saved, we want to now visit the Google Form that we created earlier.

**Commands Learned** - open
***
![](https://thumbs.gfycat.com/ShadyDevotedIncatern-size_restricted.gif)
***

Now that we have loaded the Google Forms page, we just need to find the XPATH or CSS Selectors for:
1. The input field for price
2. The submit button

I'll save you some time and tell you that on Google Forms, every input field has a unique name attribute. So in this case:

XPATH | CSS |
--- | ---
//*[@name='entry.809504561'] | input[name='entry.809504561']


That just leaves the Submit button. Now is a good time to show you the "Select" button on Selenium. It's not as good as you will be, but it can save some time *and* offers alternatives:
***
**Features Learned** - "Select Button"

![](https://thumbs.gfycat.com/SecondhandFirmEagle-size_restricted.gif)
***

Selectors are done, now we need to enter the price value and click the submit button

The selector for the button was ```//div[3]/div/div/div/content```
***
**Commands Learned** - sendKeys, click

![](https://thumbs.gfycat.com/ElectricTanConey-size_restricted.gif)
***

Now that you have successfully created your first Price Tracker, make sure you save it!

![](https://thumbs.gfycat.com/DearCapitalFugu-size_restricted.gif)






