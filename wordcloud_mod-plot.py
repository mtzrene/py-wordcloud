#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt

textwc = ""
with open('hive.txt', encoding='utf-8') as f:
    textwc = ''.join(f.readlines())

wordcloud = WordCloud(font_path = None,
                        width = 4000,
                        height = 2000,
                        mask = None,
                        color_func = None,
                        max_words = 300,
                        min_font_size = 12,
                        stopwords = None,
                        background_color = "white",
                        max_font_size = 300,
                        colormap = "gist_heat",
                        contour_width = 0,
                        contour_color = "white")

wordcloud.generate(textwc)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

