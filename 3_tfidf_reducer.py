#!/usr/bin/python2
# coding=utf-8

"""TF_IDF Reducer

   Reducer to calculate the tfidf itself

   Input: word, ((word, doc_ID), (wordcount, wordperdoc))
   Output: ((word, doc_ID), TF_IDF)

"""

import sys
import os
import string
import re
import math
import glob

df_t = {}
lines = []
all_doc_id = []

for line in sys.stdin:

    line = line.strip()
    word, ((word, doc_ID), (count, wordperdoc)) = eval(line)
    lines.append(line)

    if word not in df_t:
        df_t[word] = 1
    else:
        df_t[word] += 1

    if doc_ID not in all_doc_id:
        all_doc_id.append(doc_ID)

# w_t,d = (tf_t,d / n_d) x log(N/df_t)
N = float(len(all_doc_id))

# Loop to calculate and format response
for line in lines:
    word, ((word, doc_ID), (count, wordperdoc)) = eval(line)

    tf_t_d = float(count)
    n_d = float(wordperdoc)
    df_t_val = float(df_t[word])

    tf_idf = ( tf_t_d / n_d ) * math.log10(N/df_t_val)

    print '(("%s", %s), %10.10f)' %(word, doc_ID, tf_idf)
