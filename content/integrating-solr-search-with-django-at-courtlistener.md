Title: Integrating Solr Search with Django at CourtListener
Date: 2011-12-02T09:37:39
Tags: Sunburnt, Solr, Haystack, django, courtlistener.com
Category: Tech

Over the past few weeks, I've been hard at work on the new version of <a href="http://courtlistener.com">CourtListener</a>. Unfortunately, progress has been slower than I'd like due to the limitations of the Solr frameworks I've been using. There are a number of competing frameworks available, each with its own strengths and pitfalls.

So far, I've tried two of the popular ones, <a href="http://haystacksearch.org/">Haystack</a> and <a href="http://opensource.timetric.com/sunburnt/index.html">Sunburnt</a>. I'm pretty impressed by both, but today's blog post is to outline the problems I'm having with these frameworks so that others that are faced with choosing one might be better informed. The difference between these frameworks is vast. Haystack aims to solve all of your integration needs, while Sunburnt is a fairly lightweight wrapper around Solr.

<h3>CourtListener's needs</h3>
<p>At CourtListener, we have some big goals for the new search version. At its core, it's essentially a search-powered site, so we have some big needs:</p>



 - <a href="http://www.uxmatters.com/mt/archives/2009/09/best-practices-for-designing-faceted-search-filters.php">Parallel Faceted Search</a>
 - Highlighting
 - Complex boolean searches supported by Solr's eDisMax syntax
 - Snippets below search results and in emails
 - Standard search stuff: field-level boosting, result and facet counts, field-level searching, result pagination, performance, etc.



We're currently using <a href="http://sphinxsearch.com">Sphinx Search</a> with <a href="http://github.com/dcramer/django-sphinx">django-sphinx</a>, which does a fine job, but it has some problems:



 - django-sphinx hasn't been maintained in years, and requires patching
 - django-sphinx doesn't support snippets
 - Sphinx doesn't (yet) support real time indexing (though it's in beta, I believe)
 - Sphinx doesn't have the community and features that Solr does
 - Unfamiliar syntax for users



In general, these problems aren't too difficult, but in combination, they make for a poor user experience. The last point is a real deal breaker, since most users are accustomed to making queries like [ site:google.com ], which works for Solr and Google, but not for Sphinx. In Sphinx, your query is [ @site(google.com) ]. While we could do post processing of the user's query to convert it to Google/Solr-style syntax, it's unreliable and prone to failing in corner cases. Parsing queries is hard. More on this in a moment. 

<h3>Let's try Haystack</h3>
In switching from Sphinx, I first tried Haystack as a solution, since it has excellent documentation and seems to be the most popular solution. I spent about two weeks learning about it and getting it in place, but ultimately, I gave up on it because I found that I was subclassing it everywhere. Haystack is a good solution, to be sure, but I found that I was:



 - Subclassing the FacetView so it could support parallel facet counts
 - Subclassing the FacetForm for another feature I needed
 - Subclassing the Solr backend so it could support Solr's highlighting syntax
 - Further subclassing the Solr backend so it can support additional Solr parameters that aren't built in
 - ...etc...


I worked on that third point for the better part of a day before deciding that Haystack wasn't for me. Rather than spending my time working on the search needs of CourtListener, I was spending most of it hacking on Haystack, and trying to understand the way it fits together. It's not unreasonably complex, but there is a LOT of documentation, and a lot of complexity that I don't need (such as the ability to switch search backends). Instead of a big solution that allows me to subclass whatever I need (which is good), I needed a lighter-weight solution that was more nimble, and which allowed me to interact with Solr in a more direct way.

<h3>Enter Sunburnt</h3>
Sunburnt is a lightweight solution that is everything that Haystack isn't. From the moment it's installed, you can start making queries without configuring Django to use it, and without really knowing much else. Its documentation is a single page, which is actually a big relief after coming from Haystack. But Sunburnt has a major problem in its design: It doesn't support just sending queries to Solr. The expectation in Sunburnt is that each system using it does post-processing on the user's query, and then submits the query to Sunburnt in stages. 

So, if a user searches for "foo bar", rather than just passing that to Sunburnt, you have to split on the white space, then pass: 
    
    :::python
    si.query('foo').query('bar')

At first you think, "OK, I can do that - just split on white space, no big deal." Then you start thinking about the <a href="http://lucene.apache.org/java/3_4_0/queryparsersyntax.html#Escaping%20Special%20Characters">other syntax</a> that Solr supports, and you realize that you have a real problem if you have to split up queries appropriately. Trust me when I say that you don't want to be thinking about how to send a query like this one to Sunburnt: [ foo bar "jakarta apache"~10 ]. 

The author of Sunburnt will point out that there's a workaround for this problem. You can use 
    
    :::python
    si.search(q='"jakarta apache"~10')

 That works, to a point, but that syntax isn't supported on facets, so your facet counts won't have the same counts as your results. And so, Sunburnt, though powerful and lightweight, fails.

<h3>What now?</h3>
Good question.
