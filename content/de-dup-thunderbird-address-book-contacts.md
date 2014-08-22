Title: Fix Duplicate Thunderbird Address Book Contacts
Date: 2009-10-09T17:14:40
Tags: thunderbird, de-dup
Category: Tech


For the longest time, I've been annoyed with Thunderbird because it doesn't catch duplicate contacts as you enter them into your address book. This seems like a standard thing to check for, but even in the <a href="http://www.mozillamessaging.com/en-US/thunderbird/3.0b4/" target="_blank">latest release</a>, this still hasn't <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=129393" target="_blank">been</a> <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=45946" target="_blank">fixed</a>.

This was really starting to get out of control for me, so I did some thinking today about how to fix it, and finally came up with an answer. There is <a href="https://addons.mozilla.org/en-US/thunderbird/addon/2505" target="_blank">an add-on</a> that's supposed to do this, but it hasn't been updated in years, and doesn't work on the latest version. 

So here's the process that worked for me:

 - Open your address book, and select the address book that you wish to de-duplicate
 - Go to Tools > Export, and export the address book as a CSV file.
 - Open that file in OpenOffice Spreadsheet, and sort it by the column called "Display Name"
 - Insert a column to the left (or right, whatever) of the "Display Name" 
 column, and fill it with entries such as `=if(C2=C3, "Duplicate", 
 "OK")` Where C corresponds with the column in which you're looking for 
 duplicates. Fill the entire column with such entries all the way to the bottom.
 - Next, visually look for duplicates and delete them. Once that's done, do the same thing for the email address column, and you should be able to eliminate all the duplicates.
 - To get them back into Thunderbird, go to Tools > Import, and import the file. This will create a new address book by the name of the file.
 - From there, simply delete your old address book, and rename the new one to something useful.

All done!
