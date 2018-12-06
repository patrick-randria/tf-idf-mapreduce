#!/usr/bin/python2
# coding=utf-8

"""WORDCOUNT MAPPER

   Read all files from standard input
   Split and clean all words to map as list of key-values
   Ki, Vi => List(Ki, Vi)

   key = (word, doc_id)
   value = 1

   Input: stdin
   Output: ((word, doc_id), 1)
"""

import sys
import os
import re

stopwords = open('utils/stopwords_en.txt').read().split("\n")
current_filename = ""
doc_id = 0

for line in sys.stdin:
    # Set file ID as collection ID
    file_name = os.getenv('map_input_file')
    if current_filename != file_name:
        current_filename = file_name
        doc_id += 1

    # Set to lowercase, remove punctuations and tokenize
    line = line.lower().strip()
    line = re.sub(r"[^\w\s]", "", line)
    words = line.split()

    for word in words:
        any_digit = any(str.isdigit(c) for c in word)
        if len(word) > 3 and not any_digit and word not in stopwords:
            print '(("%s", %d), 1)' % (word, doc_id)
