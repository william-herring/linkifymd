"""
This script will link every single letter and digit in a
Markdown file to the corresponding Wikipedia page.

I have no clue why I chose to do this, but I'm certain
it will be of great use to the world.
"""

import string

path = 'sample.md'

with open(path, 'r+') as f:
    linked = ''
    t = f.read()
    f.seek(0)
    n = 0
    for c in t:
        if c == 'n' and t[n - 1] == '\\':
            linked += 'n'
            pass
        if c in string.digits or c in string.ascii_letters:
            linked += f'[{c}](https://en.wikipedia.org/wiki/{c} )'
        else:
            linked += c
        n += 1
    f.write(linked)
    f.truncate()
