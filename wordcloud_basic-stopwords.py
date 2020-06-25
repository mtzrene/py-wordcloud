#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wordcloud import WordCloud
from stop_words import get_stop_words

sw_en = get_stop_words('en')
#sw_en = get_stop_words('english')
sw_es = get_stop_words('es')
#sw_es = get_stop_words('spanish')
stopwords = sw_en + sw_es

textwc = ""

with open('hive.txt', encoding='utf-8') as f:
    textwc = ''.join(f.readlines())

wordcloud = WordCloud(stopwords = stopwords)

wordcloud.generate(textwc)

wordcloud.to_file('hive_basic_stopwords.png')
