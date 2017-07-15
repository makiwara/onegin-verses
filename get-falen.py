import sys; reload(sys); sys.setdefaultencoding('utf-8')
import sys;
import requests
import json
import re

URL = "http://lingualeo.com/ru/content/getpage?content_id=%d&page=%d"
MAX_PAGE = 69
CONTENT_ID=291492

def get_page(no):
    print "Page", no
    r = requests.get(URL % (CONTENT_ID, no))
    data = json.loads(r.text)
    return data["page"]["contentSentences"]

def get_all():
    sentences = []
    for i in range(1,MAX_PAGE):
        sentences += get_page(i)
    print
    print "Total", len(sentences)
    return u"\n".join(sentences)

with open("falen.txt", "w") as f:
    f.write(get_all())
