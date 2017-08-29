# Price Tracker
## A Practical Use for XPATH and CSS Selectors
Once you've gotten the hang of XPATH and/or CSS Selectors in [Lesson 2](https://github.com/estasney/Master_Builders/blob/master/Courses/Lesson%202%20-%20Selectors.md), it's time to put your knowledge to use!

If you're skipping around, we'll be using Selenium IDE with Firefox. If you have it successfully installed, great otherwise see this [Guide](https://github.com/estasney/Master_Builders/blob/master/Resources/Installing%20Selenium%20IDE.md) on installing it.

## Some Quick Prep Work

Selenium IDE isn't intended for data-driven uses like our price tracker will require. However, if we remember that as master builders, we specialize in the *unintended* we can craft a solution.

You'll notice that there is not direct support for saving our prices to our PC's. Which is obviously a necessity if we want to track anything over time.

### The Google Forms Solution
I came upon this genius solution in a random post on Stackoverflow so I can't take credit for it, but I *can* highly recommend it as an effective workaround.

I'll assume you have a Google account.

What we want to do is to create a Google Form that our Price Tracker can visit and enter the price it found for the day and then click submit.

#### Create the Form

![](https://thumbs.gfycat.com/TenderAbleFlycatcher-size_restricted.gif)

#### Edit a few things

- [ ] - Name it something
- [ ] - Give Question 1 a Title
- [ ] - Set Answer Type as Short Answer
- [ ] - Keep the URL Handy

![](https://thumbs.gfycat.com/RewardingCanineDoe-size_restricted.gif)

## Let's Start Automating!

Before we get started, you may see that some GIFs are from Chrome. That is because I prefer the speed and layout of Chrome's developer tools.
Feel free to use Firefox's if it is to your liking.

- [ ] - Open Firefox and Selenium IDE
- [ ] - Add a shortcut to Selenium IDE

![](https://thumbs.gfycat.com/GlossyCourageousIsabellinewheatear-size_restricted.gif)


- [ ] - Disable Record On Open

![](https://thumbs.gfycat.com/InfamousPettyCheetah-size_restricted.gif)


For this example, we'll be tracking the price of the *DoughXpress D-TXE-2-18 Stainless Steel Commercial Electromechanical Dual-Heated Press* for our *Pizza Palace Empire*

Here's the page we'll use [Pizza Maker](https://www.amazon.com/DoughXpress-D-TXE-2-18-Commercial-Electromechanical-Dual-Heated/dp/B004JPB5CE)


- [ ] - Get The Selector for the Price


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
 
 



