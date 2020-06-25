# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt

textwc = ""
with open('hive.txt', encoding='utf-8') as f:
    textwc = ''.join(f.readlines())

wordcloud = WordCloud()

wordcloud.generate(textwc)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
