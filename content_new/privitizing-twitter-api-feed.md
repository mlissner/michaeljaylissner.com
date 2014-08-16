Title: Privatizing the Twitter API Feed
Date: 2009-03-20T12:34:31
Tags: blog, Twitter


UPDATE: Check the comments for a version with caching.

A friend of mine recently had a rather unfortunate event involving her twitter public timeline, so I thought the time had come to make mine private, more or less.

As a result, I needed to update the code that pulls my most recent Twitter posts into the left hand column so that it would authenticate using the Twitter API. Here's the new code - it ain't pretty, but it works:<code lang="php"><?php

// Your twitter username & password.
$username = "YOUR_USERNAME";
$password = "YOUR_TWITTER_PASSWORD";

//Concatenate the username and password
$userpass = $username . ":" . $password;

//Make up the feed URL
$feed = "http://twitter.com/statuses/user_timeline.atom?count=1";

//A function to parse the atom feed and pull out the useful info.
function parse_feed($feed, $username) {
  $stepOne = explode("<content type=\"html\">", $feed);
  $stepTwo = explode("</content>", $stepOne[1]);

  $tweet = $stepTwo[0];
  $tweet = str_replace("&lt;", "<", $tweet);
  $tweet = str_replace("&gt;", ">", $tweet);
  $tweet = str_replace($username . ":", "", $tweet); 
  return $tweet;
}

//Create a curl object, give it the feed and authentication
$curl_handle=curl_init();
curl_setopt($curl_handle,CURLOPT_URL, $feed);
curl_setopt($curl_handle,CURLOPT_USERPWD, $userpass);

//Return the result, don't print it.
curl_setopt($curl_handle,CURLOPT_RETURNTRANSFER, 1); 

//Make the connection, set the variable, close the connection.
$twitterFeed = curl_exec($curl_handle);
curl_close($curl_handle);

//Echo the parsed feed. Done.
echo parse_feed($twitterFeed, $username);

?></code>


One dependency is the php-curl library, and after you install that, apache2 will want a restart. 