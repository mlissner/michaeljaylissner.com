"""
Hugo uses a slightly different format for its posts and so we need to take
those posts and convert them into markdown that Pelican can understand.

In particular, HUGO uses a JSON string at the beginning of all files to hold
the meta data, and Pelican uses markdown. So, this:

    {
        "categories": [
            "charity",
            "donations",
            "software",
            "good causes"
        ],
        "date": "2010-01-12T16:28:02",
        "tags": [
            "charity",
            "donations",
            "software",
            "good causes"
        ],
        "title": "2010 Donations"
    }

Gets converted to:

    Title: 2010 Donations
    Date: 2010-01-12T16:28:02
    Tags: charity, donations, software, good causes

Other meta data that could be used includes: "Modified", "Category", "Slug",
"Authors" and "Summary".
"""
import fnmatch
import os
import re
import io
import json

matches = []
for root, dirnames, filenames in os.walk('../content'):
    for filename in fnmatch.filter(filenames, '*.md'):
        matches.append(os.path.join(root, filename))

for post in matches:
    # Iterate and convert!
    print("Now processing input file: {post}".format(post=ascii(post)))
    s = io.StringIO()
    good_lines = ''
    with open(post, 'r') as f:
        finished_json = False
        for line in f:
            if not finished_json:
                if line.strip() == "}":
                    finished_json = True
                s.write(line)
            else:
                good_lines += line

    # We should have the JSON data. Work through it and write it to
    # files. Once complete, write the rest of the content too.
    data = json.loads(s.getvalue())
    with open(re.sub('/content/', '/content_new/', post), 'w') as out:
        out.write('Title: {title}\n'.format(title=data['title']))
        out.write('Date: {date}\n'.format(date=data['date']))
        out.write('Tags: {tags}\n\n'.format(tags=', '.join(data['tags'])))
        out.write(good_lines)



