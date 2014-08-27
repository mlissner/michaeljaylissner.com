import json
import MySQLdb
import os
import pprint

from datetime import datetime

# Start by creating an output dir and moving to it.
os.makedirs('out')
os.chdir('out')

db = MySQLdb.connect(host='localhost', 
		     user='root',
		     passwd='theegglady',
		     db='drupal51')

cur = db.cursor()

q = """SELECT n.nid,  
            n.title,  
	    nr.body,  
	    n.created,  
	    n.status,  
	    GROUP_CONCAT( td.name SEPARATOR '|' ) AS 'tags' 
     FROM node_revisions AS nr, 
          node AS n  
     LEFT OUTER JOIN term_node AS tn ON tn.nid = n.nid  
     LEFT OUTER JOIN term_data AS td ON tn.tid = td.tid  
     WHERE (n.type = 'blog' OR n.type = 'story' OR n.type = 'article')  AND 
         n.status = 1 AND
         n.vid = nr.vid  GROUP by n.nid;"""

cur.execute(q)

for row in cur.fetchall():
    node_id = row[0]
    print "\nWorking with nid: %s" % node_id
    
    # Get the URL
    cur.execute("select dst from url_alias where src = 'node/%s'" % node_id)
    destination_url = cur.fetchall()[0][0] 
    print "  destination_url: %s" % destination_url
    try:
        directory_path, file_name = destination_url.rsplit('/', 1)
	directory_path = directory_path + '/'
        file_name = file_name + '.md'
    except ValueError:
        # No / in the directory
	directory_path = './'
	file_name = destination_url + '.md'
    print "  directory_path is: %s" % directory_path
    if not os.path.exists(directory_path):
        print "  Making new folder path of: %s" % directory_path
        os.makedirs(directory_path)
    
    print "  Creating file at: %s%s" % (directory_path, file_name)
    
    # Create the front matter
    front = {}
    if row[5]:
        front['tags'] = row[5].split('|')
	front['categories'] = row[5].split('|')

    front.update({
        'title': row[1],
	'date': datetime.fromtimestamp(row[3]).isoformat(),
    })
    
    with open(directory_path + file_name, 'w') as f:
        f.write(json.dumps(front, indent=4, sort_keys=True))
        f.write('\n\n')
	f.write(row[2])

