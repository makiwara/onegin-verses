# -*- coding: utf-8 -*-
import re
from pprint import pprint
import random
import codecs

from pyrhyme import rhyme

ONEGIN_STRUCTURE = "A1A1BB22C33CDD"

def reverse_line(strs):
    return u''.join([strs[i] for i in xrange(len(strs)-1, -1, -1)])
def canonise_line(line):
    return (re.sub(ur'(\s|[,;\.!?\-:\'\"\(\)—])+', u' ', line.lower())).strip()

def tail(line):
    cline = canonise_line(line)
    words = cline.split(" ")
    return words[-1]


# to get raw falen source
def falen():
    f = open("falen.txt", 'r')
    s = [line.decode('utf-8') for line in f]
    return s

def en_simplify_line(line):
    line = " "+line.strip(",.;\"\n\r")+" "
    return line.strip()

def get_chapters(s):
    chapters = dict()
    c = v = None
    preface = []
    for line in s:
        simple_line = en_simplify_line(line)
        pretty_line = re.sub(r'#62038;\s*\n?', 'O ', line.strip())
        m = re.match(r'^chapter\s+([0-9]+).*', simple_line, flags=re.I)
        if m:
            c = int(m.group(1))
            chapters[c] = dict()
            v = None
        if c is not None:
            m = re.match(r'^\s*(\([0-9\-]+\))?\s*([0-9]+).*', simple_line, flags=re.I)
            if m:
                v = int(m.group(2))
                chapters[c][v] = []
            m = re.match(r'([^a-z]*[A-Z]{3,}[^a-z]*)\s*', simple_line)
            if m:
                v = m.group(1)
                chapters[c][v] = []
        if c is not None and v is not None:
            if len(line.strip()) > 0:
                chapters[c][v] += [pretty_line]
        if c is None and v is None:
            preface += [pretty_line]
    print "Chapters read."
    return preface, chapters

def get_verses(s):
    preface, chapters = get_chapters(s)
    verses = []
    for chapter in chapters.values():
        verses += chapter.values()
    print "Verses read."
    return [v for v in verses if len(v) > 0]

def get_lines(s):
    verses = get_verses(s)
    result = []
    for v in verses:
        result += v[1:]
    print "Lines read."
    return result

def get_tailed_lines(s):
    lines = get_lines(s)
    tails = dict()
    for line in lines:
        t = tail(line)
        rhymes = rhyme.rhymes_with(t)
        rhymes += t
        rhymes.sort()
        if len(rhymes) > 0:
            tail_key = rhymes[0]
            if tail_key not in tails:
                print "New rhyme (%s): %s" % (tail_key, line)
                tails[tail_key] = []
            tails[tail_key] += [line]
    return tails

def get_tailed_lines_cached(s):
    name = "falen_rhymes.txt"
    try:
        with open(name, "r") as fi:
            input_lines = fi.readlines()
        tailed_lines = dict()
        for line in input_lines:
            line = line.decode("utf-8").strip()
            words = line.split(" ")
            tail = words[0]
            full_line = " ".join(words[1:])
            if tail not in tailed_lines:
                tailed_lines[tail] = []
            tailed_lines[tail] += [full_line]
    except:
        tailed_lines = get_tailed_lines(s)
        with open(name, "w") as fo:
            for tail, lines in tailed_lines.items():
                for line in lines:
                    output = "%s %s\n" % (tail, line)
                    fo.write(output.encode("utf-8"))
        print "Cached tailed lines."
    return tailed_lines

def get_tailed_mapped(s):
    tailed_lines = get_tailed_lines_cached(s)
    for k,v in tailed_lines.items():
        enriched = dict()
        for vv in v:
            t = tail(vv)
            if t not in enriched:
                enriched[t] = []
            enriched[t] += [vv]
        tailed_lines[k] = dict(lines=enriched.values())
    return tailed_lines.values()



# to run through the english source and eventually compose
def en_pushkinize(s, style):
    # 1. Prep lines arranged by rhymed tails
    mapped = get_tailed_mapped(s)

    # 2. Arrange the most frequent rhymes to be accounted first
    letters = dict()
    for letter in style:
        if letter in letters:
            letters[letter]['count'] += 1
        else:
            letters[letter] = dict(letter=letter, count=1, pos=0)
    letterslist = [v for v in letters.values()]
    letterslist.sort(key = lambda a: -a["count"])

    # 4. Build up the verse
    letters = dict()
    for item in letterslist:
        sequence = [g for g in mapped if len(g["lines"]) >= item["count"] and not "is_used" in g]
        sample = random.sample(sequence, 1)
        hit = sample[0]
        hit["is_used"] = True
        sub_lines = random.sample(hit["lines"], item["count"])
        item["lines"] = [ random.sample(s, 1)[0].strip(",;. ") for s in sub_lines ]
        letters[ item["letter"] ] = item
    return letters

# ================================================================================
# ================================================================================
# ================================================================================
