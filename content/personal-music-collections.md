Title: Personal Music Collections
Date: 2008-02-02T20:02:59
Tags: Linux, music
Category: Music

I was curious which artists of mine had the most songs, so I ran:<code lang="bash">
du Music/ | sort -nr | head -11</code>

Now we know that my top ten artists are:<code lang="bash">
% du Music/ | sort -nr | head -11
17582796        Music/
490928  Music/Radiohead
378148  Music/Daft Punk
315856  Music/Red Hot Chili Peppers
313032  Music/Massive Attack
306228  Music/Kanye West
305796  Music/Outkast
289288  Music/Nirvana
276416  Music/Beck
258544  Music/Nine Inch Nails
248608  Music/Beatles, The
</code>
