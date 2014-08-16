{
    "categories": [
        "Walmart", 
        "Twitpic", 
        "Shutterfly", 
        "service", 
        "right to delete", 
        "privacy", 
        "Picassa", 
        "Photobucket", 
        "photo", 
        "Orkut", 
        "MySpace", 
        "google", 
        "Flickr", 
        "facebook", 
        "delete"
    ], 
    "date": "2009-11-14T16:28:44", 
    "tags": [
        "Walmart", 
        "Twitpic", 
        "Shutterfly", 
        "service", 
        "right to delete", 
        "privacy", 
        "Picassa", 
        "Photobucket", 
        "photo", 
        "Orkut", 
        "MySpace", 
        "google", 
        "Flickr", 
        "facebook", 
        "delete"
    ], 
    "title": "Testing Deletion Speed of Online Photo Sites"
}

<p>
<strong>Update, 2010-03-08:</strong>Added an image at drop.io<br>
<strong>Update, 2010-01-28:</strong> Added an image at Orkut.com<br>
<strong>Update 2, 2010-01-28:</strong> At <a href="http://www.ftc.gov/bcp/workshops/privacyroundtables/index.shtml" target="_blank">the FTC round table</a> today, Facebook's director of public policy, Tim Sparapani, claimed that information deleted from Facebook cannot be retrieved even by Facebook staff, because it is almost instantly deleted. I informed him this was not true in the case of pictures, and he said he would look into it. Will update this post when/if I hear more.</p>

<p>Imagine an embarrassing photo of you is placed online by one of your friends. You ask them to take it down, and they do. Now, imagine that your enemy had gotten a link to that photo, and had posted it to their blog. You'd hope that your friend taking the photo down would in fact delete the photo, but I'm sorry to say that isn't always the case.</p>

<p>Inspired by <a href="http://arstechnica.com/web/news/2009/07/are-those-photos-really-deleted-from-facebook-think-twice.ars" target="_blank">Jacqui Cheng's article</a>, I decided to test some of the more popular online services for photo hosting to see what happens when you "delete" a photo from their site. On <strong>November 14<sup>th</sup>, 2009</strong>, I uploaded and then deleted the following image of a black box with white text to Facebook, Flickr, Picasa, MySpace, Photobucket, Shutterfly, Twitpic and WalMart:</p>
<img src="http://michaeljaylissner.com/files/images/PostedAndDeleted.jpg">
<p>When you look below, if you can see the black box for a site, that means that it was not truly deleted and is still live. You can verify this by clicking on the image. This is checked each time this page is loaded, so the information is constantly verified. If the image has been deleted, you will see the date that it was deleted.</p>

<p>There are a number of reasons why photo services might be lazy about properly removing images from their site, but until they have proper deletion mechanisms, we should all think twice about what we upload.</p>

<p>If there's a service that is not shown here that you'd like to see, please <a href="/contact">let me know</a>. And now, without further ado, I present, the ongoing results of the test:</p>

<h4>Facebook:</h4>
<p>This file was properly deleted from their server as of at least May 27, 2010.</p>

<h4>Flickr:</h4>
<p>ED: Flickr began showing the following message approximately an hour after the image was "deleted."</p>
<?php
    $date_file = '/home/mlissner/drupal/deletedPhotosRecord.csv';
    if (@fclose(@fopen("http://farm3.static.flickr.com/2734/4103818411_886e19efaa_o.jpg", "r"))) {
        //$file_handle = fopen($date_file, 'w');
        //fwrite($file_handle, "Test");
        //fclose($file_handle);
?>
<a href="http://farm3.static.flickr.com/2734/4103818411_886e19efaa_o.jpg"><img src="http://farm3.static.flickr.com/2734/4103818411_886e19efaa_o.jpg"></a>

<?php
    } else {
        //echo "Photo not found";
        //Photo wasn't found, therefore we check the record to see if this is news
        $file_handle = fopen($date_file, 'a+');

        while (!feof($file_handle)){
            $line_of_text = fgetcsv($file_handle);
            if( $line_of_text[0] == "flickr" ) {
                //Then we have an entry in our table, print that date.
                print "<p>This file was properly deleted from their server as of at least " . $line_of_text[1] . ".</p> \n";

                $record_found = "True";
                //echo "We have an entry in our table";
                break;
            } else {
                $record_found = "False";
            }
            //echo "We are in the while loop.";
        }

        //echo $record_found;
        
        if ($record_found != "True") {
            //The file lacks an entry, we should make one, then print it.
            //echo "File lacks an entry, making one.";
            $entry = "flickr" . ", " . date("j F Y") . "\n";
            fwrite($file_handle, $entry);
            print "<p>This file was properly deleted from their server as of at least " . date("j F Y") . ".</p> \n";
        }
        fclose($file_handle);
    }
?>

<h4>Picasa:</h4>
<?php
    $date_file = '/home/mlissner/drupal/deletedPhotosRecord.csv';
    if (@fclose(@fopen("http://lh6.ggpht.com/_UOjTrSYk4Hs/Sv9QNMo-IvI/AAAAAAAAOAI/OdpZgVWXyNU/PostedAndDeleted.jpg", "r"))) {
        //$file_handle = fopen($date_file, 'w');
        //fwrite($file_handle, "Test");
        //fclose($file_handle);
?>
<a href="http://lh6.ggpht.com/_UOjTrSYk4Hs/Sv9QNMo-IvI/AAAAAAAAOAI/OdpZgVWXyNU/PostedAndDeleted.jpg"><img src="http://lh6.ggpht.com/_UOjTrSYk4Hs/Sv9QNMo-IvI/AAAAAAAAOAI/OdpZgVWXyNU/PostedAndDeleted.jpg"></a>

<?php
    } else {
        //echo "Photo not found";
        //Photo wasn't found, therefore we check the record to see if this is news
        $file_handle = fopen($date_file, 'a+');

        while (!feof($file_handle)){
            $line_of_text = fgetcsv($file_handle);
            if( $line_of_text[0] == "picasa" ) {
                //Then we have an entry in our table, print that date.
                print "<p>This file was properly deleted from their server as of at least " . $line_of_text[1] . ".</p> \n";
                $record_found = "True";
                //echo "We have an entry in our table";
                break;
            } else {
                $record_found = "False";
            }
            //echo "We are in the while loop.";
        }

        //echo $record_found;
        
        if ($record_found != "True") {
            //The file lacks an entry, we should make one, then print it.
            //echo "File lacks an entry, making one.";
            $entry = "picasa" . ", " . date("j F Y") . "\n";
            fwrite($file_handle, $entry);
            print "<p>This file was properly deleted from their server as of at least " . date("j F Y") . ".</p> \n";
        }
        fclose($file_handle);
    }
?>



<h4>MySpace:</h4>
<?php
    $date_file = '/home/mlissner/drupal/deletedPhotosRecord.csv';
    if (@fclose(@fopen("http://c3.ac-images.myspacecdn.com/images02/48/l_45a08ba940b2424a8f28f609e4c855ca.jpg", "r"))) {
        //$file_handle = fopen($date_file, 'w');
        //fwrite($file_handle, "Test");
        //fclose($file_handle);
?>
<a href="http://c3.ac-images.myspacecdn.com/images02/48/l_45a08ba940b2424a8f28f609e4c855ca.jpg"><img src="http://c3.ac-images.myspacecdn.com/images02/48/l_45a08ba940b2424a8f28f609e4c855ca.jpg"></a>

<?php
    } else {
        //echo "Photo not found";
        //Photo wasn't found, therefore we check the record to see if this is news
        $file_handle = fopen($date_file, 'a+');

        while (!feof($file_handle)){
            $line_of_text = fgetcsv($file_handle);
            if( $line_of_text[0] == "myspace" ) {
                //Then we have an entry in our table, print that date.
                print "<p>This file was properly deleted from their server as of at least " . $line_of_text[1] . ".</p> \n";
                $record_found = "True";
                //echo "We have an entry in our table";
                break;
            } else {
                $record_found = "False";
            }
            //echo "We are in the while loop.";
        }

        //echo $record_found;
        
        if ($record_found != "True") {
            //The file lacks an entry, we should make one, then print it.
            //echo "File lacks an entry, making one.";
            $entry = "myspace" . ", " . date("j F Y") . "\n";
            fwrite($file_handle, $entry);
            print "<p>This file was properly deleted from their server as of at least " . date("j F Y") . ".</p> \n";
        }
        fclose($file_handle);
    }
?>


<h4>Photobucket:</h4>
<?php
    $date_file = '/home/mlissner/drupal/deletedPhotosRecord.csv';
    if (@fclose(@fopen("http://i900.photobucket.com/albums/ac202/mlissner/PostedAndDeleted.jpg?t=1258257985", "r"))) {
        //$file_handle = fopen($date_file, 'w');
        //fwrite($file_handle, "Test");
        //fclose($file_handle);
?>
<a href="http://i900.photobucket.com/albums/ac202/mlissner/PostedAndDeleted.jpg?t=1258257985"><img src="http://i900.photobucket.com/albums/ac202/mlissner/PostedAndDeleted.jpg?t=1258257985"></a>

<?php
    } else {
        //echo "Photo not found";
        //Photo wasn't found, therefore we check the record to see if this is news
        $file_handle = fopen($date_file, 'a+');

        while (!feof($file_handle)){
            $line_of_text = fgetcsv($file_handle);
            if( $line_of_text[0] == "photobucket" ) {
                //Then we have an entry in our table, print that date.
                print "<p>This file was properly deleted from their server as of at least " . $line_of_text[1] . ".</p> \n";
                $record_found = "True";
                //echo "We have an entry in our table";
                break;
            } else {
                $record_found = "False";
            }
            //echo "We are in the while loop.";
        }

        //echo $record_found;
        
        if ($record_found != "True") {
            //The file lacks an entry, we should make one, then print it.
            //echo "File lacks an entry, making one.";
            $entry = "photobucket" . ", " . date("j F Y") . "\n";
            fwrite($file_handle, $entry);
            print "<p>This file was properly deleted from their server as of at least " . date("j F Y") . ".</p> \n";
        }
        fclose($file_handle);
    }
?>

<h4>Shutterfly:</h4>
<?php
    $date_file = '/home/mlissner/drupal/deletedPhotosRecord.csv';
    if (@fclose(@fopen("http://im1.shutterfly.com/media/47b9cf35b3127ccef8c9be9d18a800000040O00ActW7Ro4cuWQPbz4W/cC/f%3D0/ps%3D50/r%3D0/rx%3D720/ry%3D480/", "r"))) {
        //$file_handle = fopen($date_file, 'w');
        //fwrite($file_handle, "Test");
        //fclose($file_handle);
?>
<a href="http://im1.shutterfly.com/media/47b9cf35b3127ccef8c9be9d18a800000040O00ActW7Ro4cuWQPbz4W/cC/f%3D0/ps%3D50/r%3D0/rx%3D720/ry%3D480/"><img src="http://im1.shutterfly.com/media/47b9cf35b3127ccef8c9be9d18a800000040O00ActW7Ro4cuWQPbz4W/cC/f%3D0/ps%3D50/r%3D0/rx%3D720/ry%3D480/"></a>

<?php
    } else {
        //echo "Photo not found";
        //Photo wasn't found, therefore we check the record to see if this is news
        $file_handle = fopen($date_file, 'a+');

        while (!feof($file_handle)){
            $line_of_text = fgetcsv($file_handle);
            if( $line_of_text[0] == "shutterfly" ) {
                //Then we have an entry in our table, print that date.
                print "<p>This file was properly deleted from their server as of at least " . $line_of_text[1] . ".</p> \n";
                $record_found = "True";
                //echo "We have an entry in our table";
                break;
            } else {
                $record_found = "False";
            }
            //echo "We are in the while loop.";
        }

        //echo $record_found;
        
        if ($record_found != "True") {
            //The file lacks an entry, we should make one, then print it.
            //echo "File lacks an entry, making one.";
            $entry = "shutterfly" . ", " . date("j F Y") . "\n";
            fwrite($file_handle, $entry);
            print "<p>This file was properly deleted from their server as of at least " . date("j F Y") . ".</p> \n";
        }
        fclose($file_handle);
    }
?>

<h4>Twitpic:</h4>
<?php
    $date_file = '/home/mlissner/drupal/deletedPhotosRecord.csv';
    if (@fclose(@fopen("http://s3.amazonaws.com/twitpic/photos/full/42974767.jpg?AWSAccessKeyId=0ZRYP5X5F6FSMBCCSE82&Expires=1258259853&Signature=kAS%2F430H9o5nXYqfSjVGx4mRO7U%3D", "r"))) {
        //$file_handle = fopen($date_file, 'w');
        //fwrite($file_handle, "Test");
        //fclose($file_handle);
?>
<a href="http://s3.amazonaws.com/twitpic/photos/full/42974767.jpg?AWSAccessKeyId=0ZRYP5X5F6FSMBCCSE82&Expires=1258259853&Signature=kAS%2F430H9o5nXYqfSjVGx4mRO7U%3D"><img src="http://s3.amazonaws.com/twitpic/photos/full/42974767.jpg?AWSAccessKeyId=0ZRYP5X5F6FSMBCCSE82&Expires=1258259853&Signature=kAS%2F430H9o5nXYqfSjVGx4mRO7U%3D"></a>


<?php
    } else {
        //echo "Photo not found";
        //Photo wasn't found, therefore we check the record to see if this is news
        $file_handle = fopen($date_file, 'a+');

        while (!feof($file_handle)){
            $line_of_text = fgetcsv($file_handle);
            if( $line_of_text[0] == "twitpic" ) {
                //Then we have an entry in our table, print that date.
                print "<p>This file was properly deleted from their server as of at least " . $line_of_text[1] . ".</p> \n";
                $record_found = "True";
                //echo "We have an entry in our table";
                break;
            } else {
                $record_found = "False";
            }
            //echo "We are in the while loop.";
        }

        //echo $record_found;
        
        if ($record_found != "True") {
            //The file lacks an entry, we should make one, then print it.
            //echo "File lacks an entry, making one.";
            $entry = "twitpic" . ", " . date("j F Y") . "\n";
            fwrite($file_handle, $entry);
            print "<p>This file was properly deleted from their server as of at least " . date("j F Y") . ".</p> \n";
        }
        fclose($file_handle);
    }
?>


<h4>Walmart:</h4>
<?php
    $date_file = '/home/mlissner/drupal/deletedPhotosRecord.csv';
    if (@fclose(@fopen("http://images.photos1.walmart.com/232323232%7Ffp432%3B4%3Enu%3D3%3A%3A2%3E%3A8%3A%3E238%3EWSNRCG%3D326634885%3B329nu0mrj", "r"))) {
        //$file_handle = fopen($date_file, 'w');
        //fwrite($file_handle, "Test");
        //fclose($file_handle);
?>
<a href="http://images.photos1.walmart.com/232323232%7Ffp432%3B4%3Enu%3D3%3A%3A2%3E%3A8%3A%3E238%3EWSNRCG%3D326634885%3B329nu0mrj"><img src="http://images.photos1.walmart.com/232323232%7Ffp432%3B4%3Enu%3D3%3A%3A2%3E%3A8%3A%3E238%3EWSNRCG%3D326634885%3B329nu0mrj"></a>


<?php
    } else {
        //echo "Photo not found";
        //Photo wasn't found, therefore we check the record to see if this is news
        $file_handle = fopen($date_file, 'a+');

        while (!feof($file_handle)){
            $line_of_text = fgetcsv($file_handle);
            if( $line_of_text[0] == "walmart" ) {
                //Then we have an entry in our table, print that date.
                print "<p>This file was properly deleted from their server as of at least " . $line_of_text[1] . ".</p> \n";
                $record_found = "True";
                //echo "We have an entry in our table";
                break;
            } else {
                $record_found = "False";
            }
            //echo "We are in the while loop.";
        }

        //echo $record_found;
        
        if ($record_found != "True") {
            //The file lacks an entry, we should make one, then print it.
            //echo "File lacks an entry, making one.";
            $entry = "walmart" . ", " . date("j F Y") . "\n";
            fwrite($file_handle, $entry);
            print "<p>This file was properly deleted from their server as of at least " . date("j F Y") . ".</p> \n";
        }
        fclose($file_handle);
    }
?>

<h4>Google Orkut (added 2010-01-28 - disregard the date in the image itself)</h4>
<?php
    $date_file = '/home/mlissner/drupal/deletedPhotosRecord.csv';
    if (@fclose(@fopen("http://images.orkut.com/orkut/photos/NwAAAA40TqrVmtf2vIA1oouDdb9vUTcjWDAQqVo_mBa45mvjdqMPiHhSaHxekFNT596b5sVYh593XRK-5Nquk0_WOQMAm1T1UJmPN1ZDUab24PgUE8b4ZMm09Mjj.jpg", "r"))) {
        //$file_handle = fopen($date_file, 'w');
        //fwrite($file_handle, "Test");
        //fclose($file_handle);
?>
<a href="http://images.orkut.com/orkut/photos/NwAAAA40TqrVmtf2vIA1oouDdb9vUTcjWDAQqVo_mBa45mvjdqMPiHhSaHxekFNT596b5sVYh593XRK-5Nquk0_WOQMAm1T1UJmPN1ZDUab24PgUE8b4ZMm09Mjj.jpg"><img src="http://images.orkut.com/orkut/photos/NwAAAA40TqrVmtf2vIA1oouDdb9vUTcjWDAQqVo_mBa45mvjdqMPiHhSaHxekFNT596b5sVYh593XRK-5Nquk0_WOQMAm1T1UJmPN1ZDUab24PgUE8b4ZMm09Mjj.jpg"></a>

<?php
    } else {
        //echo "Photo not found";
        //Photo wasn't found, therefore we check the record to see if this is news
        $file_handle = fopen($date_file, 'a+');

        while (!feof($file_handle)){
            $line_of_text = fgetcsv($file_handle);
            if( $line_of_text[0] == "orkut" ) {
                //Then we have an entry in our table, print that date.
                print "<p>This file was properly deleted from their server as of at least " . $line_of_text[1] . ".</p> \n";
                $record_found = "True";
                //echo "We have an entry in our table";
                break;
            } else {
                $record_found = "False";
            }
            //echo "We are in the while loop.";
        }

        //echo $record_found;
        
        if ($record_found != "True") {
            //The file lacks an entry, we should make one, then print it.
            $entry = "orkut" . ", " . date("j F Y") . "\n";
            fwrite($file_handle, $entry);
            print "<p>This file was properly deleted from their server as of at least " . date("j F Y") . ".</p> \n";
        }
        fclose($file_handle);
    }
?>


<h4>Drop.io (added 08 March 2010)</h4>
<?php
    $date_file = '/home/mlissner/drupal/deletedPhotosRecord.csv';
    if (@fclose(@fopen("http://stlth.s3.amazonaws.com/assets/production/f449e7e0-ed92-012b-5667-fd14949c244a/bf4e59f0-0d07-012d-28da-f1a36935425c/PostedAndDeleted_large.jpg?Signature=Ud3VvGCtqoJHKRlHRd14S17GC6E%3D&Expires=1268071274&AWSAccessKeyId=1DHMN2J6JW2RM0N4PC82", "r"))) {
        //$file_handle = fopen($date_file, 'w');
        //fwrite($file_handle, "Test");
        //fclose($file_handle);
?>
<a href="http://stlth.s3.amazonaws.com/assets/production/f449e7e0-ed92-012b-5667-fd14949c244a/bf4e59f0-0d07-012d-28da-f1a36935425c/PostedAndDeleted_large.jpg?Signature=Ud3VvGCtqoJHKRlHRd14S17GC6E%3D&Expires=1268071274&AWSAccessKeyId=1DHMN2J6JW2RM0N4PC82"><img src="http://stlth.s3.amazonaws.com/assets/production/f449e7e0-ed92-012b-5667-fd14949c244a/bf4e59f0-0d07-012d-28da-f1a36935425c/PostedAndDeleted_large.jpg?Signature=Ud3VvGCtqoJHKRlHRd14S17GC6E%3D&Expires=1268071274&AWSAccessKeyId=1DHMN2J6JW2RM0N4PC82"></a>

<?php
    } else {
        //echo "Photo not found";
        //Photo wasn't found, therefore we check the record to see if this is news
        $file_handle = fopen($date_file, 'a+');

        while (!feof($file_handle)){
            $line_of_text = fgetcsv($file_handle);
            if( $line_of_text[0] == "drop" ) {
                //Then we have an entry in our table, print that date.
                print "<p>This file was properly deleted from their server as of at least " . $line_of_text[1] . ".</p> \n";
                $record_found = "True";
                //echo "We have an entry in our table";
                break;
            } else {
                $record_found = "False";
            }
            //echo "We are in the while loop.";
        }

        //echo $record_found;
        
        if ($record_found != "True") {
            //The file lacks an entry, we should make one, then print it.
            $entry = "drop" . ", " . date("j F Y") . "\n";
            fwrite($file_handle, $entry);
            print "<p>This file was properly deleted from their server as of at least " . date("j F Y") . ".</p> \n";
        }
        fclose($file_handle);
    }
?>