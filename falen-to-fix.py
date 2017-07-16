import sys; reload(sys); sys.setdefaultencoding('utf-8')
import sys;
import re
import codecs


def en_simplify_line(line):
    line = " "+line.strip(",.;\"\n\r")+" "
    return line.strip()



chapters = dict()
c = v = None
with codecs.open("falen.txt", encoding='utf-8') as fr, codecs.open("evgeny.txt", encoding='utf-8') as fo:
    for line in fr.readlines():
        line = en_simplify_line(line)
        m = re.match(r'^chapter\s+([0-9]+).*', line, flags=re.I)
        if m:
            c = int(m.group(1))
            chapters[c] = dict()
            v = None
        if c is not None:
            m = re.match(r'^([0-9]+).*', line, flags=re.I)
            if m:
                v = int(m.group(1))
                chapters[c][v] = []
        if c is not None and v is not None:
            if len(line) > 0:
                chapters[c][v] += [line]


howmany = 0
for c, cc in chapters.items():
    for v, vv in cc.items():
        if len(vv) != 15:
            print "CHAPTER", c, "VERSE", v, "=", len(vv)
            with open("fix/%d-%d.txt" % (c,v), "w") as f:
                f.write( "\n".join(vv))
                f.close()
            howmany += 1

print " --- TOTAL", howmany


# for c, cc in chapters.items():
#     print "CHAPTER", c, cc.keys()
# print "\n".join(chapters[2][12])
