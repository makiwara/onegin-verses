# -*- coding: utf-8 -*-

from pushkin import ru_pushkinize, onegin

style = raw_input('Verse structure (AA11BB22)-> ')
if style == '':
    style='AA11BB22'
letters = ru_pushkinize(onegin(), style)
print
for letter in style:
    print letters[letter]["lines"][ letters[letter]["pos"] ]
    letters[letter]["pos"]+=1
print
