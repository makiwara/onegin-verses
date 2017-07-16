import sys; reload(sys); sys.setdefaultencoding('utf-8'); import sys
import os
import re
import codecs


def en_simplify_line(line):
    line = " "+line.strip(",.;\"\n\r")+" "
    return line.strip()



def get_chapters(from_name):
    chapters = dict()
    c = v = None
    preface = []
    with codecs.open("%s.txt" % from_name, "r", encoding='utf-8') as fr:
        for line in fr.readlines():
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
            if c is not None and v is not None:
                if len(line.strip()) > 0:
                    chapters[c][v] += [pretty_line]
            if c is None and v is None:
                preface += [pretty_line]
    return preface, chapters


def prepare_fixes(from_name):
    preface, chapters = get_chapters(from_name)
    howmany = 0
    try: os.makedirs("fix-%s" % from_name)
    except: pass
    for c, cc in chapters.items():
        for v, vv in cc.items():
            if len(vv) != 15:
                print "CHAPTER", c, "VERSE", v, "=", len(vv)
                with open("fix-%s/%d-%d.txt" % (from_name,c,v), "w") as f:
                    f.write( "\n".join(vv))
                    f.close()
                howmany += 1
    print " --- TOTAL", howmany


def merge_fixes(from_name, to_name):
    preface, chapters = get_chapters(from_name)
    composition = preface
    for c, cc in chapters.items():
        composition += ["\nChapter %d" % c]
        for v, vv in cc.items():
            composition += [""]
            try:
                with open("fix-%s/%d-%d.txt" % (from_name,c,v), "r") as f:
                    lines = f.readlines()
                    composition += [t.strip() for t in lines]
            except Exception as e:
                composition += [t.strip() for t in chapters[c][v]]
    with codecs.open("%s.txt" % to_name, "w", encoding='utf-8') as fo:
        fo.write("\n".join(composition))

prepare_fixes("falen")
#merge_fixes("falen", "falen-from-fix")
