Title: URL Hacking at REI.com
Date: 2012-07-31T19:19:00
Tags: responsible disclosure, rei, hacking
Category: Privacy & Security

I'm about two hours away from heading on vacation to Montreal, but I wanted to post a quick update about a vulnerability I found on REI.com last night.

The vulnerability was a simple one. A few days ago, to get a 15% off coupon, I signed up for their Gear Mail newsletter. It eventually came, and at the bottom it had a link to unsubscribe, which I clicked (I was only after the 15% sign-up coupon). 

The link led to:

http://email.rei.com/cgi-bin12/DM/t/nCT4n0N3xbv0ESo05DPf0Et&EmailAddr=mlissner@michaeljaylissner.com

Which redirects to:

https://preferences.rei.com/rei/rei_PrefCtr.asp?EmailAddr=mlissner@michaeljaylissner.com

I immediately noticed the badness in these URLs, and at a whim, I tried modifying the URL to use a friend's email address. Sure enough it worked, and I could look up the full name and zip code of anybody who had an email address that was in REI's system.

Around midnight last night, I sent REI an email informing them of the problem, giving them a month to fix it, and I posted on Twitter that I had found a vulnerability on REI.com. Naively, I thought that if I didn't post the link on Twitter, nobody would be able to figure it out, but of course, by morning a friend of mine (a security/privacy researcher, sigh) had found the link and posted it. Not only that, but for fun, he had tried his address book against the link, and turned up 30 of his friend's names and zip codes out of a sample of about 200.

I sent another note to REI to make sure that they knew about the link now being in the open, and that the month I promised them had been curtailed by my own mistake. 

It's now 7:15pm, about 19 hours after I first informed them of the problem, and it's fixed. It still seems to be possible for me to update your email subscriptions, but at least I can't look up information about you.
