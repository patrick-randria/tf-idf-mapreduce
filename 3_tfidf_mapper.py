#!/usr/bin/python2
# coding=utf-8

"""TF_IDF MAPPER

   Key: word
   Value: Previous output

   Input: ((word, doc_ID), (wordcount, wordperdoc))
   Output: word, ((word, doc_ID), (wordcount, wordperdoc))
"""

import sys
import os
import string
import re
import glob

lines = []
wordperdoc = {}

for line in sys.stdin:

    (word, doc_ID), (count, wordperdoc) = eval(line.strip())
    print '"%s", %s' %(word, line.strip())
