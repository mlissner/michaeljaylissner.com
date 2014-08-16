Title: Change the Default Print to File To PDF in Ubuntu Hardy Heron
Date: 2008-10-19T23:13:25
Tags: ubuntu, print, pdf


In Ubuntu Hardy Heron there is a new printer driver that will print a webpage as a PDF file. It's pretty useful, but unfortunately it's set to print the page as post script format by default. While I appreciate post script, it's not that compatible for other people, so I usually want to make PDF documents instead.

To change that setting to PDF, navigate in Firefox to about:config, and search for the setting called "print.print_to_filename". Double click on it, and change the value to a more useful name than mozilla.ps, and change the extension to .pdf. I changed the setting to "Printed Page.pdf"

From there you should be all set.

Now, if anybody can figure out how to make the title of the webpage populate for the name of the saved file, we'll be all set.