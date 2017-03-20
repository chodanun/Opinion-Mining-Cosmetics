import csv
import operator

def readFile(path):
	return open(path,'r')

def writeFile(path):
	return open(path,'w')

def matchCommentIDtoItemID():
	comments = readFile('./data/comments-removing-redundant.csv')
	itemIdOf = {}
	spamreader = csv.reader(comments, delimiter=',')
	# comments => 0:comment_id,1:item_id,2:coment_title,3:comment_com,4:age,5:rate
	for i in spamreader:
		itemIdOf[i[0]] = i[1]
	return itemIdOf

def opinionScore(csvfile,scorefile,item_type):
	itemIdOf = matchCommentIDtoItemID()
	spamreader = csv.reader(csvfile, delimiter=',')
	# opinion_lip => 0:comment_id , 1:color , 2:smell , 3:durable
	if item_type == "lipstick":	
		score_lip = {}
		for row in spamreader:
			pass
			# print  itemIdOf[row[0]]

	# add others type here

def main():
	opinion_lip = readFile('./data/opinion_lip.csv')
	opinion_score_lip = writeFile('./data/opinion_score_lip.csv')
	opinionScore(opinion_lip,opinion_score_lip,"lipstick")


if __name__ == '__main__' :
	main()