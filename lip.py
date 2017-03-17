import csv
from wordcut import Wordcut
from nltk import ngrams
import operator

features_lip = {'สี':0,'ติด':0,'เนื้อ':0,'กลิ่น':0}
positive_sentiments_lip = {'สวย':0,'แน่น':0,'ทน':0,'คม':0,'ดี':0,'ชัด':0,'หอม':0,'ปัง':0,'ถูกใจ':0,'ชอบ':0,'เจิด':0}
negative_sentiments_lip = {'แห้ง':0,'เป็นก้อน':0,'เป็นคราบ':0,'เหลว':0,'จาง':0}
inverse_sentiments_lip = {'ไม่':0,'ไม่ค่อย':0}
alone_positive_sentiment_lip = {'หอม':0}
alone_negative_sentiment_lip = {'เป็นคราบ':0}

def readFile(path):
	return open(path,'r')

def writeFile(path):
	return open(path,'w')

def matchItemIdToType():
	type_item = csv.reader(readFile('./data/items.csv'), delimiter=',')
	typeOfItem = {}
	for row_item in type_item:
		typeOfItem[row_item[0]] = row_item[5]
	return typeOfItem

def pattern_lipstick(row):
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		comment = row[3].split(' ')
		for part in comment:
			token = wordcut.tokenize(part)
			for i in range(len(token)):
				if token[i] in features_lip: # 1,2
					try:
						if token[i-1] in positive_sentiments_lip or token[i-1] in negative_sentiments_lip: # type 2
							pass
						else: #1
							pass 
					except Exception as e:
						raise e
				else: #3
					pass
	
# comments => 0:comment_id,1:item_id,2:coment_title,3:comment_com,4:age,5:rate
def opinion(csvfile):
	spamreader = csv.reader(csvfile, delimiter=',')
	typeOfItem = matchItemIdToType()
	for row in spamreader:
		if (typeOfItem[row[1]] == "lipstick" ): # lip-209 
			pattern_lipstick(row)
		break
	# sorted_words = sorted(dict_words.items(), key=operator.itemgetter(1),reverse=True)
	# print (sorted_words)

def main():
	comments = readFile('./data/comments-removing-redundant.csv')
	opinion(comments)
	# test()

def  test():
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		print (wordcut.tokenize("เกลี่ยง่าย"))
	

if __name__ == '__main__' :
	main()