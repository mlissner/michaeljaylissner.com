Title: Google Resonds to the Twitter Attack
Date: 2009-10-02T20:37:12
Tags: security, Twitter, gmail, secret questions, passwords
Category: Privacy and Security


A few months ago, Twitter was hacked by means of a <a href="http://www.techcrunch.com/2009/07/19/the-anatomy-of-the-twitter-attack/" target="_blank">clever, yet somewhat obvious approach</a>. Today, I saw the following alert on my Gmail account, ensuring that this security vulnerability is fixed. I'm often impressed by Gmail, but this is great to see:<blockquote>
Hey, this is important: If you ever lose access to your account, you can send password reset info to [myemailaddress@michaeljaylissner.com]. This address is correct | Update this address</blockquote>What happened in the case of Twitter was that a hacker did the following:

 - Figured out the Gmail address of a Twitter employee
 - Went to <a href="https://www.google.com/accounts/ForgotPasswd?service=mail&fpOnly=1" target="_blank">Gmail's password reminder</a>, and requested a reminder
 - This informed him that an email reminder was sent to a specific Hotmail address
 - <strong>That Hotmail address had been automatically closed due to disuse</strong>
 - He set up that email account, since it was now available
 - He then requested another password reminder, which summarily sent an email to his new Hotmail account
 - This gave him complete access to the Twitter employee's gmail account (and thus a lot of other stuff)


The new alert that Gmail is now popping up should serve the function of updating this, and, if done correctly, should fix this problem permanently. Well done Gmail.
