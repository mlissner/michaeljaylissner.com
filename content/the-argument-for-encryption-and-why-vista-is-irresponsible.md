Title: The Argument for Encryption, and Why Vista Is Irresponsible
Date: 2008-09-26T20:34:31
Tags: microsoft, security, vista, pidgin
Category: Policy and Politics

We all agree that security is necessary for our data, but we all fall down when it comes to implementation. An example that I keep returning to is the need for encryption. I posted a few days ago about how Yahoo! doesn't encrypt their email, allowing a sophisticated hacker to intercept any message to or from your account. 

Today, I encountered my password in plain text in a configuration file that is easily accessible to anybody that gains physical access to my computer. The guilty program is the Pidgin IM client (<a href="http://developer.pidgin.im/ticket/5872" target="_blank">bug filed here</a>), which stores login and password information in an XML file in your home directory. I've seen files of this sort a number of times, and for some reason programmers keep using this technique.

Most people believe that if they have confidential information in their computers, and if they use a password on their computer, they'll be OK. Nobody will be able to get past the password. While that isn't entirely true (most passwords are easily broken), the thing to remember is that once a hard drive is removed from a computer, any of the data on it can be accessed &#8212; without the password. So, so long as programmers keep using this technique, sensitive data will still be out there.

The easiest solution to this problem is to encrypt your entire hard disk at all times. That way, even if your hard disk is removed from your computer, all the data is jumbled anyway. Ubuntu released this feature back in April, and Microsoft released this feature with the release of Vista. Unfortunately though, to receive encryption on your Vista installation, you have to buy Vista Ultimate, which costs $120 more than the Home version (<a href="http://www.microsoft.com/windows/windows-vista/compare-editions/default.aspx" target="_blank">at a cool $320!</a>).

As we trust more and more data on our computers, is this irresponsible product engineering? Absolutely. It costs Microsoft no more money to put encryption on all versions. Unfortunately though, they make more money by charging for it. 
