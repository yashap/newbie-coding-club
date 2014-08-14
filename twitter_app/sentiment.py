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

def tweet_score(words, score_dict):
	score = 0
	for word in words:
		score += score_dict.get(word,0)
	return score

def main():
	test = load("AFINN-111.txt")
	tweet = "Greeting great great world my name is crap"
	tweet_array = tweet_to_array(tweet)
	print tweet_score(tweet_array, test)

if __name__ == "__main__":
	main()
