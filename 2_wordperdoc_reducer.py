#!/usr/bin/python2
# coding=utf-8

"""WORDPERDOC REDUCER

   Retreive the mapper results from the standard input

   Input: (doc_ID, (word, wordcount))
   Output: ((word, doc_ID), (wordcount, wordperdoc))
"""

import sys

wordperdoc = {}
lines = []

for line in sys.stdin:

    line = line.strip()
    lines.append(line)
    docid, word_count = eval(line)

    if docid not in wordperdoc:
        wordperdoc[docid] = int(word_count[1])
    else:
        wordperdoc[docid] += int(word_count[1])

# Loop to output the right format
for line in lines:
    docid, word_count = eval(line)
    print '(("%s", %s), (%d, %d))' %(word_count[0], docid,
                                     int(word_count[1]), int(wordperdoc[docid]))
