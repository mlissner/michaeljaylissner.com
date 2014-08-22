Title: Adding New Fonts to Tesseract 3 OCR Engine
Date: 2012-02-11T10:53:30
Tags: tesseract, ocr, howto, font
Category: Tech


*Update:* I've turned off commenting on this article because it was just a bunch of people asking for help and never getting any. If you need help with these instructions, go to Stack Overflow and ask there. If you have corrections to the article, please send them directly to me using the Contact form.

[Tesseract][1] is a great and powerful OCR engine, but their [instructions for adding a new font][2] are incredibly long and complicated. At CourtListener we have to handle several unusual [blackletter fonts][3], so we had to go through this process a few times. Below I've explained the process so others may more easily add fonts to their system.

The process has a few major steps:

 * [Create training documents][4]
 * [Teach Tesseract about the documents][5]

### Create training documents

To create training documents, open up MS Word or LibreOffice, paste in the contents of the attached file named 'standard-training-text.txt'. This file contains the training text that is used by Tesseract for the included fonts.

Set your line spacing to at least 1.5, and space out the letters by about 1pt. using character spacing. I've attached a sample doc too, if that helps. Set the text to the font you want to use, and save it as font-name.doc.

Save the document as a PDF (call it [lang].font-name.exp0.pdf, with lang being an [ISO-639 three letter abbreviation][10] for your language), and then use the following command to convert it to a 300dpi tiff (requires imagemagick):

`convert -density 300 -depth 4 lang.font-name.exp0.pdf lang.font-name.exp0.tif`

You'll now have a good training image called lang.font-name.exp0.tif. If you're adding multiple fonts, or bold, italic or underline, repeat this process multiple times, creating one doc &rarr; pdf &rarr;  tiff per font variation.

### Train Tesseract

The next step is to run tesseract over the image(s) we just created, and to see how well it can do with the new font. After it's taken its best shot, we then give it corrections. It'll provide us with a box file, which is just a file containing x,y coordinates of each letter it found along with what letter it thinks it is. So let's see what it can do:

    tesseract lang.font-name.exp0.tiff lang.font-name.exp0 batch.nochop makebox

You'll now have a file called font-name.exp0.box, and you'll need to open it in a box-file editor. There are a bunch of these [on the Tesseract wiki][6]. The one that works for me (on Ubuntu) is [moshpytt][7], though it doesn't support multi-page tiffs. If you need to use a multi-page tiff, see [the issue on the topic][11] for tips. Once you've opened it, go through **every** letter, and make sure it was detected correctly. If a letter was skipped, add it as a row to the box file. Similarly, if two letters were detected as one, break them up into two lines.

When that's done, you feed the box file back into tesseract:

    tesseract eng.font-name.exp0.tif eng.font-name.box nobatch box.train .stderr

Next, you need to detect the Character set used in all your box files:

    unicharset_extractor *.box

When that's complete, you need to create a `font_properties` file. It should list every font you're training, one per line, and identify whether it has the following characteristics: &lt;fontname> &lt;italic&gt; &lt;bold&gt; &lt;fixed&gt; &lt;serif&gt; &lt;fraktur&gt;

So, for example, if you use the standard training data, you might end up with a file like this:
    
    :::bash
    eng.arial.box 0 0 0 0 0
    eng.arialbd.box 0 1 0 0 0
    eng.arialbi.box 1 1 0 0 0
    eng.ariali.box 1 0 0 0 0
    eng.b018012l.box 0 0 0 1 0
    eng.b018015l.box 0 1 0 1 0
    eng.b018032l.box 1 0 0 1 0
    eng.b018035l.box 1 1 0 1 0
    eng.c059013l.box 0 0 0 1 0
    eng.c059016l.box 0 1 0 1 0
    eng.c059033l.box 1 0 0 1 0
    eng.c059036l.box 1 1 0 1 0
    eng.cour.box 0 0 1 1 0
    eng.courbd.box 0 1 1 1 0
    eng.courbi.box 1 1 1 1 0
    eng.couri.box 1 0 1 1 0
    eng.georgia.box 0 0 0 1 0
    eng.georgiab.box 0 1 0 1 0
    eng.georgiai.box 1 0 0 1 0
    eng.georgiaz.box 1 1 0 1 0
    <strong>eng.lincoln.box 0 0 0 0 1</strong>
    <strong>eng.old-english.box 0 0 0 0 1</strong>
    eng.times.box 0 0 0 1 0
    eng.timesbd.box 0 1 0 1 0
    eng.timesbi.box 1 1 0 1 0
    eng.timesi.box 1 0 0 1 0
    eng.trebuc.box 0 0 0 1 0
    eng.trebucbd.box 0 1 0 1 0
    eng.trebucbi.box 1 1 0 1 0
    eng.trebucit.box 1 0 0 1 0
    eng.verdana.box 0 0 0 0 0
    eng.verdanab.box 0 1 0 0 0
    eng.verdanai.box 1 0 0 0 0
    eng.verdanaz.box 1 1 0 0 0

Note that this is the standard font_properties file that should be supplied with Tesseract and I've added the two bold rows for the blackletter fonts I'm training. You can also see which fonts are included out of the box.

We're getting near the end. Next, create the clustering data:

    :::bash
    mftraining -F font_properties -U unicharset -O lang.unicharset *.tr 
    cntraining *.tr

If you want, you can [create a wordlist][8] or a [unicharambigs file][9]. If you don't plan on doing that, the last step is to combine the various files we've created. 

To do that, rename each of the language files (normproto, Microfeat, inttemp, pffmtable) to have your lang prefix, and run (mind the dot at the end):

    combine_tessdata lang.

This will create all the data files you need, and you just need to move them to the correct place on your OS. On Ubuntu, I was able to move them to;

    sudo mv eng.traineddata /usr/local/share/tessdata/

And that, good friend, is it. Worst process for a human, ever.

[1]: http://code.google.com/p/tesseract-ocr/
[2]: http://code.google.com/p/tesseract-ocr/wiki/TrainingTesseract3
[3]: http://en.wikipedia.org/wiki/Blackletter
[4]: #create-training-docs
[5]: #train-tesseract
[6]: http://code.google.com/p/tesseract-ocr/wiki/TrainingTesseract3#Box_File_Editors
[7]: http://code.google.com/p/moshpytt/
[8]: http://code.google.com/p/tesseract-ocr/wiki/TrainingTesseract3#Dictionary_Data_(Optional)
[9]: http://code.google.com/p/tesseract-ocr/wiki/TrainingTesseract3#The_last_file_(unicharambigs)
[10]: http://www.sil.org/iso639-3/iso-639-3_Name_Index_20120203.tab
[11]: http://code.google.com/p/moshpytt/issues/detail?id=2
