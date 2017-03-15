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
			break
		sorted_words = sorted(dict_words.items(), key=operator.itemgetter(1),reverse=True)
		print (sorted_words)

def main():
	features_lip = {'สี','ติด','เนื้อ','กลิ่น'}
	positive_sentiments_lip = {'สวย','แน่น','ทน','คม','ดี','ชัด','หอม','ปัง','ถูกใจ','ชอบ','เจิด'}
	negative_sentiments_lip = {'แห้ง','เป็นก้อน'}
	comments = readFile('./data/comments-removing-redundant.csv')
	opinion(comments)
	# test()

def  test():
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		print (wordcut.tokenize("ชอบมากก"))
	

if __name__ == '__main__' :
	main()