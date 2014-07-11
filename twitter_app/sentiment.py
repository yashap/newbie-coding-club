import csv

def load():
	out = {}
	with open('AFINN-111.txt','rb') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		for row in tsvin:
			out[row[0]] = int(row[1])
	return out

test = load()

tweet = "Greeting world my name is crap"
tweet_list = tweet.split()

for word in tweet_list:
	print("%s %s" % (word, test.get(word)))
