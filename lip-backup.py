import csv
from wordcut import Wordcut
from nltk import ngrams
import operator

def readFile(path):
	return open(path,'r')

def writeFile(path):
	return open(path,'w')

def opinion(csvfile):
	# dict_words = {('สี', 'สวย'):0,('ติด', 'ทน'):0}
	dict_words = {}
	spamreader = csv.reader(csvfile, delimiter=',')
	#comments => 0:comment_id,1:item_id,2:coment_title,3:comment_com,4:age,5:rate
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		for row in spamreader:
			if (int(row[1]) <= 209 ) : # lip-209 
				# print ("title : %s , item_id : %s\n"%(row[2],row[1]))
				com = row[3].replace(' ','')
				token = wordcut.tokenize(com)
				try:
					bigrams = ngrams(token, 2)
					for i in bigrams:
						if i in dict_words :
							dict_words[i] += 1
						else :
							# pass
							dict_words[i] = 1
				except Exception as e:
					pass
				
				# print (dict_words)
				# input()
		sorted_words = sorted(dict_words.items(), key=operator.itemgetter(1),reverse=True)
		print (sorted_words)

def main():
	comments = readFile('../data/comments-removing-redundant.csv')
	opinion(comments)
	# test()

def  test():
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		print (wordcut.tokenize("ชอบมากก"))
	

if __name__ == '__main__' :
	main()