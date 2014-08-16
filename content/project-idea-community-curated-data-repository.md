{
    "categories": [
        "recovery", 
        "Project idea", 
        "debian", 
        "data", 
        "curation"
    ], 
    "date": "2010-08-02T13:02:42", 
    "tags": [
        "recovery", 
        "Project idea", 
        "debian", 
        "data", 
        "curation"
    ], 
    "title": "Project Idea: \"Community-Curated Data Repository\""
}

There's an interesting problem that I've run into a number of times that goes like this: You want to start a new project studying <strong>X</strong> dump of data, and you have a great idea of how to do <strong>Y</strong> with it. You go download the data, but then you spend hours (days and weeks) manipulating it, manicuring it, and stuffing it neatly into a database. The problem is that the data is in <em>their</em> format, and they probably haven't told you much about it, much less put it into a useful format for other people. You have no option but to figure it out, optimize it, make it queryable, etc, when really, what you wish you were doing was simply <em>working with it</em>.

In other words, the data format and quality keeps you from working with the data itself. I've run into this a number of times, most notably when trying to work with the <a href="http://www.recovery.gov/FAQ/Pages/DownLoadCenter.aspx" target="_blank">Recovery Data</a>. I've also had fun working with <a href="http://census.gov" target="_blank">census data</a>, geographic data, and the list goes on. There are any number of useful data sources that are provided by non-profits and government bodies, such as population, economic, health, and agricultural data.

The solution to this problem is simple. A community needs to be built around curating the data and providing it in useful formats, and a repository of some sort needs to be made so people can download <em>and install</em> the data. Similar ideas have come up a few times in various formats. Most notably, Google has taken a stab at solving this with their <a href="http://www.google.com/publicdata/home" target="_blank">public data sets</a>, and back around the turn of the millennium, Debian <a href="http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=38902" target="_blank">considered making a repository</a> for the data.

Neither of these solutions are good enough though. In Google's case, they're providing a one-way street: They choose the data source, they tune-up the data, and they provide the data. If there's a source you don't like, or if it's in a format you don't like, well, too bad. In the case of Debian, they decided not to go for it, but they should have. They had the right idea, but weren't prepared to give the idea its due.

The right solution will be one in which the community can suggest and debate data sources, and which treats the data with the respect it deserves. I think we'll see a data source like this eventually, but I fear that until we do, researchers around the world will be stuck doing unnecessary data transformations.