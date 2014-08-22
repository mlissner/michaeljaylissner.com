Title: Delete Original Images from F-Spot and Rotate Using Exif Information
Date: 2008-09-15T23:33:48
Tags: script, f-spot, awk, grep
Category: Tech


Over the past couple weeks, my girlfriend and I spent a lot of time working on the photos from our Peru trip. Since we used F-Spot to do our photo editing, when we were done we had a couple of problems when it came to transferring the photos back to her computer which is running Vista. 

The first problem was that when we rotated images with F-Spot, it simply changed the exif information for the photo, and didn't change the pixels of the photo themselves. This was fine when viewed in F-Spot because it is aware of exif information, and displays the photos correctly. However, when we transferred the files to her computer, we discovered that Vista does not take exif information into account on the OS level, nor does Picassa. As a result, we needed to somehow rotate the images that had exif information indicating a non-normal rotation.

The second problem we encountered is that in F-Spot when you edit a photo, it creates a second file with the edited photo, and leaves the original unchanged. So, if you edit file dsc00343.jpg, you get a second photo called dsc00343 (Modified).jpg. This is OK when in F-Spot, however, when we went to her computer, it was very hard for her to have ONLY the modified version of those photos, and to delete the originals (since the edited versions are better than the originals).

To solve the first problem, I used a couple of tricks. The first thing I did was to make a copy of the photos in case all went south.

    :::bash
    mkdir backupPhotos
    cp *.jpg *.jpeg backupPhotos
    cd backupPhotos

Once that is done, we can begin rotating images. For this, we will need the jhead program.

    :::bash
    sudo aptitude install jhead

Once that's installed, we rotate:
    
    :::bash
    jhead -autorot  *.jpg *.jpeg
    
This will rotate all of the files that have unusual information in the exif orientation field. 

Problem number one solved.

For problem two, we will need to isolate all of the photos that have been modified, and delete the originals. To do this, we will capitalize on the fact that the renamed images use the original pictures name in their name. 

To begin with, we create a list of the photos that have been modified:

    :::bash
    ls *.jpg *.jpeg | grep -i modified > modifiedImages.txt

Using awk, we can separate out the original name of the photos. The following 
commands will convert the ')' to '(' and will use the two '(' as a delimiters, 
returning the name of the file as the first field, and the .jpg or .jpeg as 
the third field. After that, it will remove any spaces from the file name, and 
will create a new file with a list of the modified pictures. It sounds 
complicated, but the final result should work:

    :::bash
    tr ')' '(' &lt; modifiedImages.txt > modifiedImages2.txt
    cat modifiedImages2.txt | awk -F'(' '{print $1,$3;}' | sed 's/  //g' &gt; modifiedImages3.txt

You should now have a file called modifiedImages3.txt that contains the name of all of the original photos. To delete the pictures in this list from the collection - permanently - run:

    :::bash
    rm `cat modifiedImages3.txt`

You should now be able to transfer this entire directory of photos to another computer without rotation issues or duplicated photos.
