#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tweepy
from wordcloud import WordCloud, STOPWORDS
import collections
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import MeCab
import subprocess
import pandas as pd
import csv


# In[29]:


df = pd.read_csv("tweet_selection.csv")
data = ""

for i in range(len(df.index)):
  if df.iat[i,1] == 0:
    data = data + df.iat[i,0]


# In[4]:


#テキストの分かち書き
me = MeCab.Tagger ("-Owakati")
me.parseToNode('')
nodes = me.parseToNode(data)

#各変数の初期化
meishi_count = 0
doushi_count = 0
keiyou_count = 0
meishi_list=[]
doushi_list=[]
keiyou_list=[]


# In[24]:


#形態素のうち名詞，動詞，形容詞のみを抽出し，カウント
while nodes:
  if nodes.feature.split(",")[0] == "名詞":
    meishi_count = meishi_count + 1
    meishi_list.append(nodes.surface)
  elif nodes.feature.split(",")[0] == "動詞":
    doushi_count = doushi_count + 1
    doushi_list.append(nodes.surface)
  elif nodes.feature.split(",")[0] == "形容詞":
    keiyou_count = keiyou_count + 1
    keiyou_list.append(nodes.surface)
  else:
    pass
  nodes = nodes.next

text = ""+ " ".join(meishi_list) + " ".join(doushi_list) + " ".join(keiyou_list)


# In[27]:


#WCの下ごしらえ

stop_words = ["https", "co", "てる", "する", "そう", "すぎ", "いい", "さん", "こと"]
fpath = "/Library/Fonts//ヒラギノ丸ゴ ProN W4.ttc"

wc = WordCloud(
  font_path = fpath,
  background_color = "white",
  max_words = 2000,
  collocations = False,
  stopwords = set(stop_words)
)

# WordCloudの実行
wc.generate(text)
wc.to_file("word_cloud.png")

plt.figure(figsize=(15,12))
plt.imshow(wc)
plt.axis("off")
plt.show()

