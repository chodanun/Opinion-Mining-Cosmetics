import csv
from wordcut import Wordcut

def readFile(path):
	return open(path)

def writeFile(path):
	return open(path,'w')

def opinion(csvfile):
	spamreader = csv.reader(csvfile, delimiter=',')
	#comments => 0:comment_id,1:item_id,2:coment_title,3:comment_com,4:age,5:rate
	for row in spamreader:
		print (row[0])

def main():
	lip_file = readFile('./data/comments.csv')
	opinion(lip_file)

if __name__ == '__main__' :
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		print(wordcut.tokenize("กากา cat หมา"))
	# main()