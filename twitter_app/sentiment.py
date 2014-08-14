import csv

def load(fname):
	out = {}
	with open(fname,"rb") as tsvin:
		tsvin = csv.reader(tsvin, delimiter="\t")
		for row in tsvin:
			out[row[0]] = int(row[1])
	return out

def tweet_to_array(tweet):
	final = []
	tweet_array = tweet.split()
	for word in tweet_array:
		final.append(word.lower())
	return final

test = load("AFINN-111.txt")
tweet = "Greeting world my name is crap"
tweet_array = tweet_to_array(tweet)

for word in tweet_array:
	print("%s %s" % (word, test.get(word)))
