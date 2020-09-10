#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import csv
import random
import pandas as pd

filename = "2020-08-01.jsonl"
numOfTweet = 61299

#jsonからツイート文章をとってきてtweet_original.csvに入れる
file = open('tweet_original.csv', 'w', encoding='utf_8_sig')
w = csv.writer(file, lineterminator='\n')

with open(filename, encoding='utf_8_sig') as fin:
    for line in fin:
        data = json.loads(line)
        w.writerow([data['full_text']]) 
file.close()


# In[12]:


def replaced_username_URL(text):
    
    """
    textリスト内の文章から"@username"と"://URL"の置換を行う
    改善点->前後に空白のないユーザーネームを処理できてない at 16- line
    改善点->URLが連続したとき用に空白入れてしまってる at 25 line
    改善点->ツイート内の画像も識別処理したいよねー
    """
    
    text_replaced_username = []
    text_replaced_url = []
    
    for i in range(len(text)):
    
        text_replaced_username.append(text[i])
        for j in range(len(text_replaced_username[-1].split(" "))):
            if text_replaced_username[-1].split(" ")[j].startswith("@") == True:
                replace_word = text_replaced_username[-1].split(" ")[j]
                text_replaced_username[-1] = text_replaced_username[-1].replace(replace_word, "@username")
    
        text_replaced_url.append(text_replaced_username[-1])
        for j in range(len(text_replaced_url[-1].split("https"))):
            if text_replaced_url[-1].split("https")[j].startswith("://") == True:
                replace_word = text_replaced_url[-1].split("https")[j]
                text_replaced_url[-1] = text_replaced_url[-1].replace(replace_word, "://URL ")
    
    text_replaced = text_replaced_url
    return text_replaced

#tweet_original.csvからランダムで500コとってきてPandasを介してtweet_selection.csvに入れる
pickup = random.sample(range(numOfTweet), k=1500)
text = []
df = pd.read_csv("tweet_original.csv", names=["tweet"], encoding='utf_8_sig')

for i in pickup:
    if df.iat[i, 0].startswith("RT") == False:
            text.append(df.iat[i, 0])

df2 = pd.DataFrame([replaced_username_URL(text)]).T
df2.to_csv("tweet_selection.csv", encoding='utf_8_sig', header=["Tweet"], index=False)

