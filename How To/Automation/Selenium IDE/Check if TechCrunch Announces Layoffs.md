# Using Selenium IDE to Get TechCrunch's Layoff Announcements

### Idea from John
During our group call for [Lesson 2](https://github.com/estasney/Master_Builders/blob/master/Courses/Lesson%202%20-%20Selectors.md)
and [Lesson 2.5](https://github.com/estasney/Master_Builders/blob/master/Courses/Lesson%202.5%20-%20Selenium%20IDE.md), 
John had suggested opening [TechCrunch Layoff Announcements](https://techcrunch.com/tag/layoffs/) and checking each day if 
any layoffs had been announced.

We didn't have time to cover how to do this in Selenium IDE so I am posting a how-to here as it is a great scenario.

### The Site
Looking at the site, [TechCrunch Layoff Announcements](https://techcrunch.com/tag/layoffs/) we see that each post contains information about layoffs.
Since layoffs are (thankfully) not a normal occurence, the articles are posted irregularly.

### Using Selenium IDE and Google Forms

#### Analyze the page

Following our common theme...
1. <kbd>Right-Click</kbd> and <kbd>Inspect</kbd> the article at the top of the page
2. See if we can find a parent element that all articles fall under
3. Find the parent write a selector for it and then select it's first child element
***
![](https://thumbs.gfycat.com/FondSpectacularGosling-size_restricted.gif)
***






