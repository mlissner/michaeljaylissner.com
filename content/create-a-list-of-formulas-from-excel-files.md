{
    "categories": [
        "microsoft", 
        "excel"
    ], 
    "date": "2008-05-22T12:16:59", 
    "tags": [
        "microsoft", 
        "excel"
    ], 
    "title": "Create a List of Formulas from Excel Files"
}

I have begun training a replacement at work, and I need to teach him all of the excel formulas that we use in our department documents. I started making a list of all the formulas, but my mind quickly went blank, and I decided I needed a way to automate it. 

Here's the technique I figured out. Open each of the files that you believe has useful formulas in it, and go to File > Save as... Save each document into an empty directory as xml spreadsheets (.xml). If you open one of these documents in a text editor, you are likely to see a line something like the following: <code lang="xml">
<Cell ss:Formula="=SUM(C:C[1])"><Data ss:Type="Number">0</Data></Cell></code>
The key is that each row in your new xml documents that contains a formula will have the formula keyword, so to isolate these, run the following on a Unix computer in the directory where you saved all the xml documents.<code lang="bash">
grep 'Formula=' *.xml | sort | uniq > uniqLinesWithFormulas.txt</code>

That will create a file called uniqLinesWithFormulas.txt that will contain each line from all of your .xml files that contains a formula. From there, you can skim them visually for useful formulas, or put the file into Excel again and play with it there. This was as far as I needed to go in my analysis. Once I had this done, it was pretty easy to see the 30 or so formulas I regularly use.<!--break-->