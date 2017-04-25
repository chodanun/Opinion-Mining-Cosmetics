import csv
import operator

def readFile(path):
	return open(path,'r')

def writeFile(path):
	return open(path,'w')

def typeOfItem():
	dict_type={}
	file = readFile('./data/items.csv')
	spamreader = csv.reader(file, delimiter=',')
	for i in spamreader:
		dict_type[i[0]] = i[5]
	return dict_type

def scoreCalculation(scoreList,newScoreFile):
	dict_type = typeOfItem()
	for file in scoreList:
		spamreader = csv.reader(file, delimiter=',')
		for i in spamreader:
			score = 0
			pos = 0
			neg = 0
			reviews = 0
			if dict_type[i[0]] == "lipstick":
				# there are 8 arrts -> 0:item_id, 1-6:feature, 7:reviews
				pos = int(i[1])+int(i[2])+int(i[3])
				neg = int(i[4])+int(i[5])+int(i[6])
				reviews = int(i[7])
			elif dict_type[i[0]] == "skin protection":
				# there are 18 arrts -> 0:item_id, 1-16:feature, 17:reviews
				pos = int(i[1])+int(i[2])+int(i[3])+int(i[4])+int(i[5])+int(i[6])+int(i[7])+int(i[8])
				neg = int(i[9])+int(i[10])+int(i[11])+int(i[12])+int(i[13])+int(i[14])+int(i[15])+int(i[16])
				reviews = int(i[17])
			if pos+neg == 0:
				score = 0
			else :
				score = ((pos-neg)/(pos+neg))*5
			print (i[0],dict_type[i[0]],score)
			newScoreFile.write("%s,%s,%.2f,%s\n"%(i[0],dict_type[i[0]],score,reviews))
	newScoreFile.close()

def main():
	opinion_score_lip = readFile('./data/opinion_score_lip.csv')
	opinion_score_skin = readFile('./data/opinion_score_skin.csv')

	opinion_score_calculation = writeFile('./data/opinion_score_calculation.csv')
	opinion_score_files = [opinion_score_lip,opinion_score_skin]

	scoreCalculation(opinion_score_files,opinion_score_calculation)
	


if __name__ == '__main__' :
	main()