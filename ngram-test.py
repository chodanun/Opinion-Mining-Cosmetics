import csv
from nltk import ngrams
from wordcut import Wordcut
import operator

def readFile(path):
	return open(path,'r')

def main():
	f = readFile('./data/comments-removing-redundant.csv')
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		dict_twogram = {}
		spamreader = csv.reader(f, delimiter=',')
		for row in spamreader:
			if (int(row[0]) >= 921 and int(row[0]) <= 2173):
				token = wordcut.tokenize(row[3].replace(' ',''))
				twograms = ngrams(token, 2)			
				try:
					for i in twograms:
						if i in dict_twogram:
							dict_twogram[i] +=1
						else:
							dict_twogram[i] = 1
				except (TypeError):
					pass
		sorted_x = sorted(dict_twogram.items(), key=operator.itemgetter(1),reverse=True)
		print (sorted_x)

if __name__ == '__main__' :
	main()