#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wordcloud import WordCloud

textwc = ""

with open('hive.txt', encoding='utf-8') as f:
    textwc = ''.join(f.readlines())

wordcloud = WordCloud()

wordcloud.generate(textwc)

wordcloud.to_file('hive_basic.png')