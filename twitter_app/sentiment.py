import csv

def load():
	out = {}
	with open('AFINN-111.txt','rb') as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		for row in tsvin:
			out[row[0]] = int(row[1])
	return out