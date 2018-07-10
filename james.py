# -*- coding: utf-8 -*-

from pushkin import en_pushkinize, falen

style = raw_input('Verse structure (AA11BB22)-> ')
if style == '':
    style='AA11BB22'
letters = en_pushkinize(falen(), style)

print
for letter in style:
    lines = letters[letter]["lines"]
    pos   = letters[letter]["pos"]
    print lines[pos]
    letters[letter]["pos"]+=1
print
