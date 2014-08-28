Title: How to Protect Your Open Source Code from Theft and a Mercurial Hook to Help
Date: 2010-01-15T10:27:18
Tags: mercurial, hook, Final Project, DMCA, copyright, Affero GPLv3, CourtListener
Category: Tech


**Updated, 2010-01-24:** Some edits regarding the Affero license (thanks to
Brian at [http://cyberlawcases.com][1] for the corrections).

I've finally begun doing some of the actual coding for [my final 
project][2] so the time has come to set up [a mercurial repository][3] to 
hold the code.

Once we complete our project, we will have built a free product that 
competes with some of the core functionality of both LexisNexis and 
Westlaw, so something we wanted to do was make sure they couldn't steal our
code, enhance their product and thus moot ours.

To achieve this, we're using the [GNU Affero General Public License 
v3][4], which allows people to take our code for free, but requires that they 
publicly share any modifications that they make to the code. The normal GNU 
General Public License allows the code to be used at no cost, 
but only requires that changes to the code be shared with the public if one
distributes the changed version to the public. With a server-based 
project, like ours, one could operate modified versions of the code 
without ever having a need to distribute any of the software to the public. 
This loophole is closed by the Affero license.

In order to license our work, we must be its copyright holder. This is easy
enough, since we get copyright instantly in the U.S., but, 
as has been demonstrated in [Jacobsen v. Katzer][5], in order to seek remedies 
for copyright violations, we would have to register everything we made with 
the copyright office. This [costs $35][6] per registration, 
and with open source software, it's not clear whether each and every 
version needs to be registered or just major releases, or what. 

Since this is too onerous to be practical, an additional approach to 
protecting our works is useful, and in the DMCA ([17 U.S.C. § 506(d)][8]), 
remedies are provided for the "fraudulent removal of copyright notice." 
Although these do not (in any way) match the protections provided by normal
copyright registration, they are a useful place to begin. Thus, 
if we place a copyright notice into each file of our code, 
those using our code must either risk violating the DMCA by removing these
notices, or leave our copyright information intact. (Placing such notices
in each file is also [the recommendation][7] of the Free Software 
Foundation.)

To place our information into each and every file of code that we upload 
publicly, I wrote [a short mercurial hook][hook] that  adds copyright and 
licensing information it to the top of every file that is modified or added 
to the repository. To use the script, simply make it executable, 
place it in the .hg directory of your project, and add the following lines
to .hg/hgrc:

    :::text
    [hooks]
    pretxncommit = .hg/checklicense.py

A couple of things I should note about this script is that it currently 
only checks for java and python files, and that it requires files called 
java_license.txt and python_license.txt to be in the root of your 
repository. It should be fairly easy to modify though to fit your own needs.

[1]: http://cyberlawcases.com/
[2]: http://www.ischool.berkeley.edu/programs/masters/projects/2010/judicialnlp
[3]: https://github.com/freelawproject/courtlistener
[4]: http://www.gnu.org/licenses/agpl.html
[5]: http://en.wikipedia.org/wiki/Jacobsen_v._Katzer
[6]: http://www.copyright.gov/docs/fees.html
[7]: http://www.fsf.org/licensing/licenses/gpl-howto.html
[8]: http://www.copyright.gov/title17/92chap5.html#506
[hook]: {filename}/archive/checklicense.py
