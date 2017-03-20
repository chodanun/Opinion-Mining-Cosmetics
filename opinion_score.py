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
		itemIdOf[int(i[0])] = int(i[1])
	return itemIdOf

def writeScoreDictInFile(score_dict,scorefile):
	for key,val in score_dict.items():
		scorefile.write("%d,%d,%d,%d,%d,%d,%d,%d\n"%(key,val['color_pos'],val['smell_pos'],val['durable_pos'],val['color_neg'],val['smell_neg'],val['durable_neg'],val['reviews']))
	scorefile.close()

def opinionScore(csvfile,scorefile,item_type):
	itemIdOf = matchCommentIDtoItemID()
	spamreader = csv.reader(csvfile, delimiter=',')
	# opinion_lip => 0:comment_id , 1:color , 2:smell , 3:durable
	if item_type == "lipstick":	
		score_lip = {}
		for row in spamreader:
			if itemIdOf[int(row[0])] in score_lip:
				score_lip[itemIdOf[int(row[0])]]['reviews'] += 1
				if int(row[1]) > 0: # color
					score_lip[itemIdOf[int(row[0])]]['color_pos'] += int(row[1])
				elif int(row[1]) < 0:
					score_lip[itemIdOf[int(row[0])]]['color_neg'] += -int(row[1])
				if int(row[2]) > 0: # smell
					pass
					score_lip[itemIdOf[int(row[0])]]['smell_pos'] += int(row[2])
				elif int(row[2]) < 0:
					pass
					score_lip[itemIdOf[int(row[0])]]['smell_neg'] += -int(row[2])
				if int(row[3]) > 0: # durable
					pass
					score_lip[itemIdOf[int(row[0])]]['durable_pos'] += int(row[3])
				elif int(row[3]) < 0:
					pass
					score_lip[itemIdOf[int(row[0])]]['durable_neg'] += -int(row[3])
			else:
				score_lip[itemIdOf[int(row[0])]] = {'color_pos':0,'smell_pos':0,'durable_pos':0,'color_neg':0,'smell_neg':0,'durable_neg':0,'reviews':1}
		writeScoreDictInFile(score_lip,scorefile)
		
	# add others type here

def main():
	opinion_lip = readFile('./data/opinion_lip.csv')
	opinion_score_lip = writeFile('./data/opinion_score_lip.csv')
	opinionScore(opinion_lip,opinion_score_lip,"lipstick")


if __name__ == '__main__' :
	main()