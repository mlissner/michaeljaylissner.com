Title: How to Protect Your Open Source Code from Theft and a Mercurial Hook to Help
Date: 2010-01-15T10:27:18
Tags: mercurial, hook, Final Project, DMCA, copyright, Affero GPLv3, courtlistener.com


<strong>Updated, 2010-01-24:</strong> Some edits regarding the Affero license (thanks to Brian at <a href="http://cyberlawcases.com/" target="_blank">http://cyberlawcases.com</a> for the corrections).

I've finally begun doing some of the actual coding for <a href="http://www.ischool.berkeley.edu/programs/masters/projects/2010/judicialnlp" target="_blank">my final project</a> so the time has come to set up <a href="http://bitbucket.org/mlissner/legal-current-awareness/" target="_blank">a mercurial repository</a> to hold the code.

Once we complete our project, we will have built a free product that competes with some of the core functionality of both LexisNexis and Westlaw, so something we wanted to do was make sure they couldn't steal our code, enhance their product and thus moot ours.

To achieve this, we're using the <a href="http://www.gnu.org/licenses/agpl.html" target="_blank">GNU Affero General Public License v3</a>, which allows people to take our code for free, but requires that they publicly share any modifications that they make to the code. The normal GNU General Public License allows the code to be used at no cost, but only requires that changes to the code be shared with the public if one distributes the changed version to the public. With a server-based project, like ours, one could operate modified versions of the code without ever having a need to distribute any of the software to the public. This loophole is closed by the Affero license.

In order to license our work, we must be its copyright holder. This is easy enough, since we get copyright instantly in the U.S., but, as has been demonstrated in <a href="http://en.wikipedia.org/wiki/Jacobsen_v._Katzer" target="_blank">Jacobsen v. Katzer</a>, in order to seek remedies for copyright violations, we would have to register everything we made with the copyright office. This <a href="http://www.copyright.gov/docs/fees.html" target="_blank">costs $35</a> per registration, and with open source software, it's not clear whether each and every version needs to be registered or just major releases, or what. 

Since this is too onerous to be practical, an additional approach to protecting our works is useful, and in the DMCA (<a href="http://www.copyright.gov/title17/92chap5.html#506" target="_blank">17 U.S.C. � 506(d)</a>), remedies are provided for the "fraudulent removal of copyright notice." Although these do not (in any way) match the protections provided by normal copyright registration, they are a useful place to begin. Thus, if we place a copyright notice into each file of our code, those using our code must either risk violating the DMCA by removing these notices, or leave our copyright information intact. (Placing such notices in each file is also <a href="http://www.fsf.org/licensing/licenses/gpl-howto.html" target="_blank">the recommendation</a> of the Free Software Foundation.)

To place our information into each and every file of code that we upload publicly, I wrote a short mercurial hook that  adds copyright and licensing information it to the top of every file that is modified or added to the repository. To use the script, simply make it executable, place it in the .hg directory of your project, and add the following lines to .hg/hgrc:
<code lang="text">
[hooks]
pretxncommit = .hg/checklicense.py
</code>

A couple of things I should note about this script is that it currently only checks for java and python files, and that it requires files called java_license.txt and python_license.txt to be in the root of your repository. It should be fairly easy to modify though to fit your own needs.
