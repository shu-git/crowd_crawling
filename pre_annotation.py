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

#tweet_original.csvからランダムで500コとってきてPandasを介してtweet_selection.csvに入れる
pickup = random.sample(range(numOfTweet), k=500)
text = []
for i in pickup:
    text.append(df.iat[i, 0])
    
df = pd.read_csv("tweet_original.csv", names=["tweet"], encoding='utf_8_sig')
df2 = pd.DataFrame([text]).T
df2.to_csv("tweet_selection.csv", encoding='utf_8_sig',header=None, index=False)
