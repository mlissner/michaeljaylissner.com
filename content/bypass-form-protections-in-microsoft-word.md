Title: Bypass Form Protection in MS Word
Date: 2008-04-18T10:13:22
Tags: microsoft, msword, hacking
Category: Privacy and Security


I recently had the occasion to need to get around the form protection in an MS Word file. Turns out it�s a pretty easy exploit, but the directions I found elsewhere on the internet didn�t quite do the job. 

Here�s the trick:
<ol> - Open the protected document, and save it as an .html file.
 - Close the .doc file, and open the .html file in a text editor such as notepad or GVIM
 - In the .html file, find a tag that says something like: "&lt;w:UnprotectPassword&gt;ABCDEF01&lt;/w:UnprotectPassword&gt;"
 - Replace each of the characters in the tag with zeroes so it reads: "&lt;w:UnprotectPassword&gt;00000000&lt;/w:UnprotectPassword&gt;"
 - Open the .html file in Word, and save it as a .doc. Go to Tools > Unprotect Document</ol>

That should do it. I�d love to hear any evidence to the contrary. 
