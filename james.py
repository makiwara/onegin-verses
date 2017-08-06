# -*- coding: utf-8 -*-

from pushkin import en_pushkinize, falen, en_tail

style = raw_input('Verse structure (AA11BB22)-> ')
if style == '':
    style='AA11BB22'
letters = en_pushkinize(falen(), style)

print
for letter in style:
    print letters[letter]["lines"][ letters[letter]["pos"] ]["line"]
    letters[letter]["pos"]+=1
print
