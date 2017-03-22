import csv

def readFile(path):
	return open(path,'r')

def writeFile(path):
	return open(path,'w')

def preprocessing(file,func_write=False):
	except_words = [',',"\"",' ','ด']
	if func_write :
		newfile = writeFile('./data/comments-removing-redundant.csv')
	
	for i in file:
		comment_new =""
		for j in range(len(i)):
			if i[j] in except_words or i[j].isdigit():
				comment_new+=i[j]
			else :
				if j > 0 and j < len(i)-1:
					if i[j] == i[j-1] and i[j] == i[j-2] and j>1 :
						pass
					elif i[j] != i[j-1] or i[j] != i[j+1] :
						comment_new+=i[j]
				else :
					comment_new+=i[j]

		if comment_new != i :
			print (i)
			print (comment_new)
		if func_write :
			newfile.write("%s"%comment_new)	
	# close file
	if func_write :
		newfile.close()
	

def main():
	# 1: preprocessing step
	comments = readFile('./data/comments.csv')
	preprocessing(comments,func_write=False)


if __name__ == '__main__' :
	main()