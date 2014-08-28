Title: The Winning Font in Court Opinions
Date: 2012-01-27T22:15:58
Tags: typography, tesseract, Python, ocr, font, CourtListener
Category: Tech


At CourtListener, we're developing a new system to convert scanned court 
documents to text. As part of our development we've analyzed more than 1,000 
court opinions to determine what fonts courts are using. 

Now that we have this information, our next step is to create training data 
for [our OCR system][1] so that it specializes in these fonts, 
but for now we've attached [a spreadsheet][ss] with our findings, 
and [a script that can be used by others][script] to extract font metadata 
from PDFs.

Unsurprisingly, the top font &mdash; drumroll please &mdash; is Times New Roman. 

<table>
    <tr>
        <th>Font</td>
        <th>Regular</td>
        <th>Bold
        <th>Italic
        <th>Bold Italic
        <th>Total
    </tr>
    <tr>
        <td>Times
        <td>1454
        <td>953
        <td>867
        <td>47
        <td>**3321**
    </tr>
    <tr>
        <td>Courier
        <td>369
        <td>333
        <td>209
        <td>131
        <td>**1042**
    </tr>
    <tr>
        <td>Arial
        <td>364
        <td>39
        <td>11
        <td>41
        <td>**455**
    </tr>
    <tr>
        <td>Symbol
        <td>212
        <td>0
        <td>0
        <td>0
        <td>**212**
    </tr>
    <tr>
        <td>Helvetica
        <td>24
        <td>161
        <td>2
        <td>2
        <td>**189**
    </tr>
    <tr>
        <td>Century Schoolbook
        <td>58
        <td>54
        <td>52
        <td>9
        <td>**173**
    </tr>
    <tr>
        <td>Garamond
        <td>44
        <td>42
        <td>41
        <td>0
        <td>**127**
    </tr>
    <tr>
        <td>Palatino Linotype
        <td>36
        <td>24
        <td>24
        <td>1
        <td>**85**
    </tr>
    <tr>
        <td>Old English
        <td>42
        <td>0
        <td>0
        <td>0
        <td>**42**
    </tr>
    <tr>
        <td>Lincoln
        <td>27
        <td>0
        <td>0
        <td>0
        <td>**27**
    </tr>
</table>

[1]: http://code.google.com/p/tesseract-ocr/
[ss]: {filename}/archive/court-font-analysis/font-analysis.ods
[script]: {filename}/archive/court-font-analysis/extract_font_metadata_from_files.py 
