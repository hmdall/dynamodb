import simplejson as json
import os

basics='/Users/walkerrowe/Documents/imdb/100.basics.json'
fBasics = open(basics, 'r')

ratings='/Users/walkerrowe/Documents/imdb/title.ratings.tsv'
fRatings = open(ratings, 'r')


data=json.loads(fBasics.read())

outRatings = open('/Users/walkerrowe/Documents/imdb/100.ratings.json', 'w')

titles = []
for k,v in data.items():
    for t in v:
        titles.append(t["PutRequest"]["Item"]["tconst"]["S"])

for title in fRatings:
    r = title.split('\t')
    if r[0] in titles:
        print(title)
        outRatings.write(title)







fBasics.close()
fRatings.close()
