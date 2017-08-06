# -*- coding: utf-8 -*-
import re
from pprint import pprint
import random

ONEGIN_STRUCTURE = "A1A1BB22C33CDD"
KNOWN_TAILS = [
    ["+", "ing", "embly"],
    ["ings"],
    ["call"],
    ["ast"],
    ["art"],
    ["arted"],
    ["arts"],
    ["asses"],
    ["ill"],
    ["oss"],
    ["ave"],
    ["lad"],
    ["+", "ight", "ite"],
    ["ights", "ites"],
    ["ought", "aught"],
    ["ustle"],
    ["ented"],
    ["chants", "dance", "trance", "aunt s"],
    ["ense", "ence", "ance", "erents"],
    ["ide", "dyed", "ried", "pied", "died", "fied"],
    ["ated", "aded", "freighted"],
    ["ided", "ighted", "ited", "eated", "eeted", "eted", "eeded", "ceded"],
    ["ife", "alive"],
    ["honour", "Tatyana", "Svetlana", "Madonna", "Diana", "upon her"],
    ["ages", "gauges", "ageous"],
    ["urges", "erges"],
    ["and", "anned"],
    ["earned", "erned",],
    ["eard", "erred", "ord", "ird", "irred", "ored", "poured"],
    ["+", "dead", "head", " bed", " led", "stead", "dread", " red", " fed", "fled", "bled", "sled", "said", "shed",
            "spread", "sped", "tread", "thread", "leaves unread", "had read", "once read", "like lead"],
    ["aid", "ayed", "veyed", "ade"],
    ["eed", "ead"],
    ["really", "clearly"],
    ["chuckled", "cookold"],
    ["ightly", "itely"],
    ["early"],
    ["ickly"],
    ["joy", "boy"],
    ["reply", "spy", "lie", "fly", " by", "eye", "bye", "sly", "buy", "sigh", "cry", "die", "high", "sky", " I", "why", "try",
        "pie", "dry"],
    ["ear", "eer", "ere", "dier"],
    ["ears", "eers", "eres"],
    ["rhyme", "climb"],
    ["eather", "ether"],
    ["other", "ather", "others", "other s"],
    ["over"],
    ["ssly", "sely"],
    ["nd her", "nder", "endour"],
    ["mour", "mmar"],
    ["allor", "alour", "partner"],
    ["our", "ower"],
    ["martyr"],
    ["eed her", "ead her", "eader", "eeder", "eeter"],
    ["ide her", "ied her"],
    ["by her", "higher"],
    ["ave her", "aver"],
    ["eady"],
    ["oken"],
    ["aken"],
    ["uty"],
    ["hen", "when", "again", "pen", "yen", "men", "den"],
    ["ain", "sane", "agne", "ane", "vein"], # ^!
    ["are", "air", "ayer"],
    ["adly"],
    ["tone", "lone", "oan", "own", "gone", "awn", "rone"],
    ["oon", " tune"],
    ["ussian"],
    ["eason", "Fonvizin"],
    [" one", "done", "un", "on"],
    [" in", "kin", "sin", "begin", "spin", "din", "win", "bin", "lin", "een", "thin", "sine", "zine", "cene", "rene", "ean", "gene",
        "een", "ene", "rin", "pauline", "Knyazhnin"],
    ["ected", "rect it"],
    ["know it", "poet"],
    ["ick it", "icket"],
    ["ank it", "anket"],
    ["ished"],
    ["eny it"],
    ["ore it"],
    ["ine", "ign"],
    ["ession", "etion"],
    ["ition", "ician"],
    ["assion", "ation", "ashion"],
    ["inion"],
    ["ntion"],
    ["action"],
    ["+", "ation", "asion"],
    ["ection", "exion"],
    ["otion", "ocean"],
    ["out", "doubt"],
    ["ate", "ait"],
    ["in it", "minute", "bit", "wit", "fit", "lit", "sit"],
    ["est", "ssed", "ests" ],
    ["apture"],
    ["easure", "eisure"],
    ["easures", "eisures"],
    ["end", "enned"],
    ["ind", "gned", "ined"],
    ["ound", "owned"],
    ["ess"],
    ["yre", "ire", "lier", "pariah", "fire", "voronskaya", "liar"],
    ["dallies", "valleys"],
    ["ries", "lies", "eyes"],
    ["owers", "hours"],
    ["eat", "eet", "ete"],
    ["aim", "ame"],
    ["eem", "eam"],
    ["ome", "oam"],
    ["matey", "lady"],
    ["demurely", "zizi"],
    ["rely"],
    ["lley", "dally"],
    ["usion"],
    ["eese", "eeze", "abcs", "vry s"],
    ["+", "away", "ay", "ey", "soire", "leigh", "chausse", "beret", "Triquet", "blancmanger", "pince nez"],
    ["ease", "eace"],
    ["highways", "byways"],
    ["+", "ace", "ase", "aze", "aise", "ays"],
    ["then"],
    ["eased"],
    ["passed"],
    ["choir"],
    ["all", "awl"],
    ["soul", "goal", "control", "role", "oll", "col"],
    ["vel", "evil"],
    ["ell", "el", "ele"],
    ["ile", "yle"],
    ["eats", "its"],
    ["et", "ebts", "ebt", "ets",  "ette", " tte", "ettes"], # "get", "set", "yet", "pet", "ret", "thet"],
    ["how", " now"],
    ["llow"],
    ["+", "ore", "oar", "oor", "o", "oe", "ow", "guillot", "bough", "Rousseau", "owe", "war", "Tissot"],
    ["too", "adieu", "loup", "two"],
    ["got", "lot", "not", "what", "ott", "shot"],
    ["you", "rough", "rue", "ew", "lue", "though", "due", "cue"],
    ["youth", "truth"],
    ["come", "dumb"],
    ["psichore", "ee", "ea", "be", "me", "he", "ennui"],
    ["ones"],
    ["song", "long", "rong"],
    ["ended"],
    ["ends"],
    ["quies", "ees", "eas", "eys"],
    ["pieces", "ceases", "creases"],
    ["cies", "ces", "sis"],
    ["oice", "oise", "oys"],
    ["rise", "rice", "lies", "ties", "ighs"],
    ["Pustyakva", "Harlikva"],
    ["iss", "is"],
    ["chorus"],

    ## 6
    ["ations", "ations s", "ation s"],
    ["ptions", "ptions s"],
    ["ctions", "ptions s"],
    ["med her"],
    ["eet her"],
    ["urr", "o her", "demur"],
    ["ord her", "order"],
    ["ight her", "ighter"],
    ["ip her", "ipper"],
    ["ake him"],
    ["ear him"],
    ["uns him"],
    ["olds him"],
    ["rned him"],
    ["eetely", "eately", "etely"],
    ["old", "mould"],
    ["them", "condemn", "solemn", "column"],
    ["orse", "ourse", "erse", "urse"],
    ["eary", "eery"],
    ["ild", "iled"],
    ["ept", "leapt"],
    ["eams", "emes", "eems"],
    ["eetly", "eatly", "etely"],
    ["ook"],
    ["atter"],
    ["ingers"],
    ["ief", "leaf"],
    ["itter"],
    ["arkly"],
    ["oors"],
    ["utter"],
    ["etter"],
    ["ssions"],
    ["ersions"],
    ["isions"],
    ["itions"],
    ["esses"],
    ["uttered", "uddered"],
    ["owered"],
    ["membered", "endered"],
    ["overed"],
    ["urry", "orry", "ary", "sary", "arry", "lory"],
    ["tory", "tery"],
    ["each", "eech"],
    ["ires", "oirs"],
    ["acted"],
    ["eared", "eered"],
    ["ently"],
    ["uster", "ustre"],
    ["rish"],
    ["ass", "alas"],
    ["eak", "eek"],
    ["anted"],
    ["overs"],
    ["ivers"],
    ["gory"],
    ["altered"],
    ["attered"],
    ["umbered"],
    ["ndered"],
    ["oom", "tomb"],
    ["asted"],
    ["ever"],
    ["ands"],
    ["ired"],
    ["ood", "ould", "bued"],
    ["uarter", "water", "aughter"],
    ["ater"],
    ["uarters", "waters", "aughters"],
    ["aters"],
    ["ttle", "etal"],
    ["iver"],
    ["ises", "izes"],
    ["aises", "ases"],
    ["ouses", "owses"],
    ["uses", "ooses"],
    ["oses", "ozes"],
    ["ades", "adies"],
    ["onders", "anders"],
    ["inger"],
    ["ove", " of"],
    ["oured"],
    ["icken"],
    ["red him", "re him", "Grimm", "of him"],
    ["alls"],
    ["ent", "ant"],
    ["atches"],
    ["unches"],
    ["enters"],
    ["atters"],
    ["erted"],
    ["anner"],
    ["inner"],
    ["airs", "ares"],
    ["entive"],
    ["active", "uctive"],
    ["dant", "sant"],
    ["mble", "mble s"],
    ["able"],
    ["irded", "erted"],
    ["ains", "eigns"],
    ["usive"],
    ["ssive"],
    ["nsive"],
    ["ainted"],
    ["ault her", "altar"],
    ["aught her", "ought her"],
    ["ound her"],
    ["eet her", "eat her"],
    ["oo her", "do her"],
    ["armed her"],
    ["in her", "blur"],
    ["ind her"],
    ["aste", "aced"],
    ["umbers"],
    ["uly"],
    ["ows", "oze", "ose", "oes", "zeros"],
    ["ews", "use"],
    ["end us"],
    ["out us", "oubt us"],
    ["for us", "fuss"],
    ["ushes"],
    ["aches"],
    ["ample"],
    ["aper"],
    ["ools", "ules"],
    ["ouldn t"],
    ["eep"],
    ["ale", "ail", "eil"],
    ["aily"],
    ["ack", "nac"],
    ["orn", "urn", "orne", "earn"],
    ["ectly"],
    ["ice"],
    ["ables"],
    ["ales", "ails", "eils"],
    ["oubles"],
    ["oans"],
    ["ark"],
    ["oldly"],
    ["ote"],
    ["uple", "pupil"],
    ["oint"],
    ["oad", "ode"],
    ["oke", "oak"],
    ["acks", "acts"],
    ["at"],
    ["oop", "oup"],
    ["owd", "oud", "owed"],
    ["oach"],
    ["young", "tongue"],
    ["guish"],
    ["ounds", "owns"],
    ["eels", "eals"],
    ["for us", "thus"],
    ["ore us", "chorus"],
    ["Nina"],
    ["Laura", "aura"],
    ["Thomas"],
    ["alk"],
    ["eature"],
    ["eatures"],
    ["ertly"],
    ["ince"],
    ["itch", "ich"],
    ["anny"],
    ["orth"],
    ["earer", "irror"],
    ["illed"],
    ["cenes", "eans", "cine s"],
    ["itten"],
    ["astened"],
    ["ealed"],
    ["ared"],
    ["ested"],
    ["oot", "uit", "ute"],
    ["uch", "ooch"],
    ["older", "oulder"],
    ["arkled"],
    ["ouble"],
    ["ointed"],
    ["inted"],
    ["urled", "world"],
    ["ounded"],
    ["eerful", "earful"],
    ["usions"],
    ["ocker"], ["icker"],
    ["anic"],
    ["iteful", "ightful"],
    ["ateful"],
    ["aven", "seven"],
    ["ext", "exed"],
    ["amber", "amper", "ember"],
    ["melody", "endormie"],
    ["ize", "ise"],
    ["ogue"],
    ["isses"],
    ["ips", "eaps", "eeps"],
    ["yly"],
    ["ust"],
    ["ick"],
    ["arm"],
    ["ops"],
    ["op"],
    ["ap"],
    ["an"],
    ["aws"],
    ["ask"],
    ["ilt"],
    ["ope"],
    ["nely"],
    ["ames", "aims"],
    ["aw"],
    ["ovna"],
    ["tius", "cias"],
    ["ont"],
    ["am"],
    ["ool"],
    ["ix"],
    ["ror", "roar"],
    ["Aurora", "ore her", " her"],
    ["ynov"],
    ["inners"], ["inner"],
    ["offers"], ["immers"],
    ["ridge"], ["assock"],
    ["ush"],
    ["abble"],
    ["ash"],
    ["utely"],
    ["arms"],
    ["angers"],
    ["olly", "oly"],
    ["odded"],
    ["ism"],
    ["ooled"],
    ["cond", "ckoned"],
    ["irls"],
    ["entions"],
    ["served"],
    ["serves"],
    ["ortals"],
    ["ards"],
    ["eath"],
    ["elf"],
    ["nators"],
    ["ort", "ourt"],
    ["enery"],
    ["age"],
    ["uted"],
    ["oted"],
    ["aster"],
    ["ans", "anns"],
    ["auded"],
    ["udes"],
    ["eal"],
    ["osed"],
    ["ot"],
    ["younger", "hunger"],
    ["anges"],
    ["ock"],
]
KNOWN_TAILS_MAP = dict()
for T in KNOWN_TAILS:
    for t in T:
        if T[0] == "+":
            KNOWN_TAILS_MAP[t.lower()] = T[1]
        else:
            KNOWN_TAILS_MAP[t.lower()] = T[0]
CORRECT_TAILS = [T[1] for T in KNOWN_TAILS if T[0] == "+"]
KNOWN_TAILS_SEQ = sorted(KNOWN_TAILS_MAP.keys(), lambda a,b: len(b)-len(a))


def canonise_line(line):
    return (re.sub(ur'(\s|[,;\.!?\-:\'\"\(\)—])+', u' ', line.lower())).strip()

def tail(line):
    cline = canonise_line(line)
    for t in KNOWN_TAILS_SEQ:
        if cline[-len(t):] == t:
            return KNOWN_TAILS_MAP[t]
    words = cline.split(" ")
    # exit()
    return words[-1]#[-6:]
    # return u" ".join(words[-2:])


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
    return preface, chapters

def get_verses(s):
    preface, chapters = get_chapters(s)
    verses = []
    for chapter in chapters.values():
        verses += chapter.values()
    return [v for v in verses if len(v) > 0]

def get_raw_rhyming_lines(s):
    verses = get_verses(s)
    result = []
    # prepare verses of Onegin structure
    proper_verses = []
    for verse in verses:
        verse_cut = verse[1:]
        while len(verse_cut) >= 14:
            proper_verses+= [verse_cut[0:14]]
            verse_cut = verse_cut[14:]
    # split verse into primitive rhymes
    for verse in proper_verses:
        rhymes = dict()
        for i in range(0, len(ONEGIN_STRUCTURE)):
            if ONEGIN_STRUCTURE[i] not in rhymes:
                rhymes[ONEGIN_STRUCTURE[i]] = []
            rhymes[ONEGIN_STRUCTURE[i]] += [verse[i]]
        result += rhymes.values()
    return result


def get_rhyming_lines(s):
    lines = get_raw_rhyming_lines(s)
    rhymes = dict()
    for line in lines:
        tails = [tail(x) for x in line]
        tails.sort()
        if not tails[0] in KNOWN_TAILS_MAP and tails[1] in KNOWN_TAILS_MAP:
            t = tails[0]
            tails[0] = tails[1]
            tails[1] = t
        if tails[0] not in rhymes:
            rhymes[tails[0]] = dict(
                lines=[],
                tails=[tails[0]],
            )
        rhymes[tails[0]]["lines"] += [ dict(
                line=l,
                tail=tail(l),
                known=tail(l) in KNOWN_TAILS_MAP,
                pair=line
            ) for l in line ]
    def sort_func(a,b):
        return len(b["lines"]) - len(a["lines"])
    rhymes_list = sorted(rhymes.values(), sort_func)
    for rl in rhymes_list:
        rl["tails"] = [x["tail"] for x in rl["lines"]]
        rl["tails"] = list(set(rl["tails"]))
    return rhymes_list


def scan_for_rhymes(s):
    lines = get_rhyming_lines(s)
    for r in lines:
        # if len(r["lines"]) > 2:
            filtered = [l["line"] for l in r["lines"] if not l["known"]]
            filtered_pairs = [l for l in r["lines"] if not l["known"]]
            raw =  [l["line"] for l in r["lines"]]
            if len(filtered) > 0:
                print
                print (u", ".join(r["tails"])).encode('utf-8')
                print "------------"
                for l in filtered_pairs:
                    print l["line"].encode('utf-8')
                    # for p in l["pair"]:
                    #     print "    ", p.encode('utf-8')
                # print (u"\n".join(filtered)).encode('utf-8')
                # for t in r["tails"]:
                #     for l in raw:
                #         print (t).encode('utf-8'), (l).encode('utf-8')
    print


def map_rhymes(s):
    lines = get_rhyming_lines(s)
    line_map = dict()
    for r in lines:
        for l in r["lines"]:
            if l["tail"] not in line_map:
                line_map[l["tail"]] = dict(
                    tail=l["tail"],
                    lines=[]
                )
            line_map[l["tail"]]["lines"] += [l]

    def sort_func(a,b):
        return len(b["lines"]) - len(a["lines"])
    checkout = sorted(line_map.values(), sort_func)
    correct_lines = []
    correct = []
    to_fix = []
    to_fix_lines = []
    for r in checkout:
        if r["tail"] in CORRECT_TAILS or len(r["lines"]) == 2:
            correct_lines += r["lines"]
            correct += [r]
        elif len(r["lines"]) > 2:
            to_fix += [r]
            to_fix_lines += r["lines"]
    return dict(
        all=checkout,
        fix=to_fix,
        fix_lines=to_fix_lines,
        correct=correct,
        correct_lines=correct_lines
    )

def validate(s):
    mapped = map_rhymes(s)
    print "Total rhymes:", len(mapped["all"]), "   Remaining:", len(mapped["fix"])
    print "Lines accessible:",  len(mapped["correct_lines"])
    print "Lines to validate:", len(mapped["fix_lines"])
    for r in mapped["fix"]:
        print u"----------------"
        print r["tail"].encode('utf-8')
        print u"----------------"
        def reverse(strs):
            return u''.join([strs[i] for i in xrange(len(strs)-1, -1, -1)])
        for l in sorted(r["lines"], lambda a,b: reverse(a["line"]) > reverse(b["line"])):
            print l["line"].encode('utf-8')
        print u"----------------"
        exit()

# to run through the russian source and eventually compose
def en_pushkinize(s, style):
    mapped = map_rhymes(s)

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
        sequence = [g for g in mapped["correct"] if len(g["lines"]) >= item["count"] and not "is_used" in g]
        sample = random.sample(sequence, 1)
        sample[0]["is_used"] = True
        item["lines"] = random.sample(sample[0]["lines"], item["count"])
        letters[ item["letter"] ] = item
    return letters

# ================================================================================
# ================================================================================
# ================================================================================
