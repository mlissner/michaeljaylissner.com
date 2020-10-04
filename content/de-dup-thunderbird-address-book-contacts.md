Title: Fix Duplicate Thunderbird Address Book Contacts
Date: 2009-10-09T17:14:40
Tags: thunderbird, de-dup
Category: Tech


For the longest time, I've been annoyed with Thunderbird because it doesn't catch duplicate contacts as you enter them into your address book. This seems like a standard thing to check for, but even in the <a href="http://www.mozillamessaging.com/en-US/thunderbird/3.0b4/">latest release</a>, this still hasn't <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=129393">been</a> <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=45946">fixed</a>.

You have two options:

1. There is an <a href="https://addons.thunderbird.net/en-us/thunderbird/addon/duplicate-contacts-manager/">addon</a> that can easily do this for you! Install the addon, then from your address book, choose Tools > Find and manage duplicates...

2. If you want to do this the old-fasioned way:
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

Either way works great!
