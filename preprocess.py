import csv

def readFile(path):
	return open(path,'r')

def writeFile(path):
	return open(path,'w')

def preprocessing(file):
	# possible_words = ['อ','น']
	for i in file:
		print (i)
		for j in range(len(i)):
			if j > 0 and j < len(i)-1:
				if i[j] == i[j-1] and i[j] == i[j+1] :
					pass
				else :
					print (i[j],end='')
			else :
				print (i[j],end='')
			# elif i[j] == i[j-1]:
			# 	if i[j] in possible_words :
			# 		print (i[j],end='')


		input()
	

def main():
	# 1: preprocessing step
	comments = readFile('./data/comments.csv')
	comments = preprocessing(comments)


if __name__ == '__main__' :
	main()