Title: How to Recover a Broken Drupal Install Resulting from a Full Hard Drive
Date: 2010-04-26T11:26:38
Tags: mysql, hard drive, drupal


This is amazingly, the second time I've filled my server's hard drive, and the results are becoming predictable. One moment, things are working fine, the next, cron alerts you with something like this:
<code>Table [tablename] is marked as crashed and last (automatic?) repair failed query</code>

This is a bad warning to get, and running df on the server confirms that indeed my hard drive is full. Fixing this is a matter of doing some minor MySQL hacking to clean up all the tables:
<code>mysql -u'drupalusername' -p
> use drupal_DB_name;
> check table tablename;
> repair table tablename;
</code>

Then, simply iterate this for each broken table reported by cron.php, and you will soon have a repaired DB. Whew.