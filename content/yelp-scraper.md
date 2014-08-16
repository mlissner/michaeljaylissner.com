{
    "categories": [
        "Python", 
        "yelp", 
        "programming", 
        "scrape"
    ], 
    "date": "2008-12-21T16:41:13", 
    "tags": [
        "Python", 
        "yelp", 
        "programming", 
        "scrape"
    ], 
    "title": "Yelp Scraper to Get Business Info in a Geographic Area"
}

I spent the past couple days on one of my first Python projects - using the <a href="http://www.yelp.com/developers" target="_blank">Yelp API</a> to compile a list of restaurants in a defined geographic area.

It's been a good project. Because of some limitations of the API, I had to do some interesting tricks to make it work. One problem with the API is that it only allows 20 hits per query, so if you want to do a big query, you have to divide it up into tiny queries that have fewer than 20 hits each. 

To accomplish that, if a query gets 20 hits within those two points, it will divide the longer dimension of the rectangle created by the points in half, and perform a query on each of those two new rectangles. For each of those, if there are 20 hits, it will again divide it in two and perform two new queries, and so forth until less than 20 hits are found for the rectangle. Once less than 20 hits are found, the data is entered into a database. Once all the points have been added to the database, a comma separated file is created, and the program ends. 

It was pretty incredible switching to Python for this project from my usual Java, and also using an official API for the first time. This project ended up being about 200 lines (half of which are comments). I can't imagine how long it would be with Java, since I used some rather powerful Python modules to accomplish this (namely, csv, urllib & json).

If anybody is interested in seeing/using the code, let me know. It should be useful if you need a list of restaurants or other businesses in a certain area. Worthy causes only please!<!--break-->