#!/usr/bin/env python
import sqlite3 as sql
import sys, os, os.path

_conn = sql.connect('pyrhyme/data/rhyme.db')

def rhymes_with(word):
    """Returns a list of words that rhyme, or [] if no words rhyme."""
    global _conn
    cursor = _conn.execute("select * from words where word=?", (word.lower(),))
    row = cursor.fetchone()
    if not row: return []
    word, sound, key = row
    cursor = _conn.execute("select * from rhymes where sound=?", (sound,))
    sound, words = cursor.fetchone()

    #return all the matching words. If a word has a (n) on it, clip it off,
    #and also don't return the original word
    return [x.split('(')[0] for x in words.split() if x.lower() != word.lower()]

def main():
    for word in sys.argv[1:]:
        print '%s: %s' % (word, ', '.join(rhymes_with(word)))
main() if __name__=='__main__' else None
