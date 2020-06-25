#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wordcloud import WordCloud

textwc = ""
with open('hive.txt', encoding='utf-8') as f:
    textwc = ''.join(f.readlines())

wordcloud = WordCloud(font_path = "/usr/share/fonts/truetype/andika/Andika-R.ttf",
                        width = 4000,
                        height = 2000,
                        mask = None,
                        color_func = None,
                        max_words = 300,
                        min_font_size = 12,
                        stopwords = None,
                        background_color = "gray",
                        max_font_size = 300,
                        colormap = "gist_heat",
                        contour_width = 0,
                        contour_color = "white")

wordcloud.generate(textwc)

wordcloud.to_file('hive_mod.png')
