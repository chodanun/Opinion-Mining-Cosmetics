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

def writeScoreDictInFile(score_dict,scorefile,item_type):
	if item_type == 'lipstick':
		for key,val in score_dict.items():
			scorefile.write("%d,%d,%d,%d,%d,%d,%d,%d\n"%(key,val['color_pos'],val['smell_pos'],val['durable_pos'],val['color_neg'],val['smell_neg'],val['durable_neg'],val['reviews']))
	if item_type == 'skin_protection':
		for key,val in score_dict.items():
			scorefile.write("%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n"%(key,val['sticky_pos'],val['permeate_pos'],val['stain_pos'],val['smell_pos'],val['moist_pos'],val['irritate_pos'],val['waterproof_pos'],val['sunproof_pos'],val['sticky_neg'],val['permeate_neg'],val['stain_neg'],val['smell_neg'],val['moist_neg'],val['irritate_neg'],val['waterproof_neg'],val['sunproof_neg'],val['reviews']))
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
					score_lip[itemIdOf[int(row[0])]]['smell_pos'] += int(row[2])
				elif int(row[2]) < 0:
					score_lip[itemIdOf[int(row[0])]]['smell_neg'] += -int(row[2])
				if int(row[3]) > 0: # durable
					score_lip[itemIdOf[int(row[0])]]['durable_pos'] += int(row[3])
				elif int(row[3]) < 0:
					score_lip[itemIdOf[int(row[0])]]['durable_neg'] += -int(row[3])
			else:
				score_lip[itemIdOf[int(row[0])]] = {'color_pos':0,'smell_pos':0,'durable_pos':0,'color_neg':0,'smell_neg':0,'durable_neg':0,'reviews':0}
				score_lip[itemIdOf[int(row[0])]]['reviews'] += 1
				if int(row[1]) > 0: # color
					score_lip[itemIdOf[int(row[0])]]['color_pos'] += int(row[1])
				elif int(row[1]) < 0:
					score_lip[itemIdOf[int(row[0])]]['color_neg'] += -int(row[1])
				if int(row[2]) > 0: # smell
					score_lip[itemIdOf[int(row[0])]]['smell_pos'] += int(row[2])
				elif int(row[2]) < 0:
					score_lip[itemIdOf[int(row[0])]]['smell_neg'] += -int(row[2])
				if int(row[3]) > 0: # durable
					score_lip[itemIdOf[int(row[0])]]['durable_pos'] += int(row[3])
				elif int(row[3]) < 0:
					score_lip[itemIdOf[int(row[0])]]['durable_neg'] += -int(row[3])
		writeScoreDictInFile(score_lip,scorefile,item_type)
	
	elif item_type == "skin_protection":
		score_skin = {}
		for row in spamreader:
			if itemIdOf[int(row[0])] in score_skin:
				score_skin[itemIdOf[int(row[0])]]['reviews'] += 1
				if int(row[1]) > 0: # color
					score_skin[itemIdOf[int(row[0])]]['sticky_pos'] += int(row[1])
				elif int(row[1]) < 0:
					score_skin[itemIdOf[int(row[0])]]['sticky_neg'] += -int(row[1])
				if int(row[2]) > 0: # smell
					score_skin[itemIdOf[int(row[0])]]['permeate_pos'] += int(row[2])
				elif int(row[2]) < 0:
					score_skin[itemIdOf[int(row[0])]]['permeate_neg'] += -int(row[2])
				if int(row[3]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['stain_pos'] += int(row[3])
				elif int(row[3]) < 0:
					score_skin[itemIdOf[int(row[0])]]['stain_neg'] += -int(row[3])
				if int(row[4]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['smell_pos'] += int(row[4])
				elif int(row[4]) < 0:
					score_skin[itemIdOf[int(row[0])]]['smell_neg'] += -int(row[4])
				if int(row[5]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['moist_pos'] += int(row[5])
				elif int(row[5]) < 0:
					score_skin[itemIdOf[int(row[0])]]['moist_neg'] += -int(row[5])
				if int(row[6]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['irritate_pos'] += int(row[6])
				elif int(row[6]) < 0:
					score_skin[itemIdOf[int(row[0])]]['irritate_neg'] += -int(row[6])
				if int(row[7]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['waterproof_pos'] += int(row[7])
				elif int(row[7]) < 0:
					score_skin[itemIdOf[int(row[0])]]['waterproof_neg'] += -int(row[7])
				if int(row[8]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['sunproof_pos'] += int(row[8])
				elif int(row[8]) < 0:
					score_skin[itemIdOf[int(row[0])]]['sunproof_neg'] += -int(row[8])
			else:
				score_skin[itemIdOf[int(row[0])]] = {'sticky_pos':0,'permeate_pos':0,'stain_pos':0,'smell_pos':0,'moist_pos':0,'irritate_pos':0,'waterproof_pos':0,'sunproof_pos':0,'sticky_neg':0,'permeate_neg':0,'stain_neg':0,'smell_neg':0,'moist_neg':0,'irritate_neg':0,'waterproof_neg':0,'sunproof_neg':0,'reviews':0}
				score_skin[itemIdOf[int(row[0])]]['reviews'] += 1
				if int(row[1]) > 0: # color
					score_skin[itemIdOf[int(row[0])]]['sticky_pos'] += int(row[1])
				elif int(row[1]) < 0:
					score_skin[itemIdOf[int(row[0])]]['sticky_neg'] += -int(row[1])
				if int(row[2]) > 0: # smell
					score_skin[itemIdOf[int(row[0])]]['permeate_pos'] += int(row[2])
				elif int(row[2]) < 0:
					score_skin[itemIdOf[int(row[0])]]['permeate_neg'] += -int(row[2])
				if int(row[3]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['stain_pos'] += int(row[3])
				elif int(row[3]) < 0:
					score_skin[itemIdOf[int(row[0])]]['stain_neg'] += -int(row[3])
				if int(row[4]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['smell_pos'] += int(row[4])
				elif int(row[4]) < 0:
					score_skin[itemIdOf[int(row[0])]]['smell_neg'] += -int(row[4])
				if int(row[5]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['moist_pos'] += int(row[5])
				elif int(row[5]) < 0:
					score_skin[itemIdOf[int(row[0])]]['moist_neg'] += -int(row[5])
				if int(row[6]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['irritate_pos'] += int(row[6])
				elif int(row[6]) < 0:
					score_skin[itemIdOf[int(row[0])]]['irritate_neg'] += -int(row[6])
				if int(row[7]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['waterproof_pos'] += int(row[7])
				elif int(row[7]) < 0:
					score_skin[itemIdOf[int(row[0])]]['waterproof_neg'] += -int(row[7])
				if int(row[8]) > 0: # durable
					score_skin[itemIdOf[int(row[0])]]['sunproof_pos'] += int(row[8])
				elif int(row[8]) < 0:
					score_skin[itemIdOf[int(row[0])]]['sunproof_neg'] += -int(row[8])
		writeScoreDictInFile(score_skin,scorefile,item_type)
	# add others type here

def main():
	# opinion_lip = readFile('./data/opinion_lip.csv')
	# opinion_score_lip = writeFile('./data/opinion_score_lip.csv')
	# opinionScore(opinion_lip,opinion_score_lip,"lipstick")
	opinion_skin = readFile('./data/opinion_skin.csv')
	opinion_score_skin = writeFile('./data/opinion_score_skin.csv')
	opinionScore(opinion_skin,opinion_score_skin,"skin_protection")


if __name__ == '__main__' :
	main()