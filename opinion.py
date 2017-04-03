import csv
from wordcut import Wordcut
from nltk import ngrams
import operator

# lipstick
features_lip = {'สี':0,'ติด':0,'เนื้อ':0,'กลิ่น':0}
positive_sentiments_lip = {'แนะนำ':0,'สวย':0,'แน่น':0,'ทน':0,'คม':0,'ดี':0,'ชัด':0,'หอม':0,'หอมหวาน':0,'ปัง':0,'ถูกใจ':0,'ชอบ':0,'เจิด':0,'สด':0,'นุ่ม':0,'ลื่น':0,'ชัดเจน':0,'นาน':0,'เนียน':0,'โอเค':0,'หวาน':0,'แจ่ม':0,'นิ่ม':0,'ทาง่าย':0,'ละเอียด':0,'ติด':0,'นิ่ม':0,'เข้มข้น':0}
negative_sentiments_lip = {'แห้ง':0,'เป็นก้อน':0,'เป็นคราบ':0,'เหลว':0,'จาง':0,'ผิดหวัง':0,'ไม่ชอบ':0}
inverse_sentiments_lip = {'ไม่':0,'ไม่ค่อย':0,'ไปนิด':0}
alone_positive_sentiment_lip = {'หอม':0}
alone_negative_sentiment_lip = {'เป็นคราบ':0}

#skin protection
features_skin_protection = {'เหนียวเหนอะหนะ':0,'เหนอะหนะ':0,'เหนียว':0,'เหนอะ':0,'หนืด':0,'ซึม':0,'คราบ':0,'กลิ่น':0,'ชุ่มชื่น':0,'ชุ่ม':0,'ระคายเคือง':0,'กันน้ำ':0,'กันแดด':0,'แสงแดด':0}
positive_sentiments_skin_protection = {'ดี':0,'สุดยอด':0,'แนะนำ':0,'เยี่ยม':0,'โอเค':0,'ชอบ':0,'เทพ':0,'เร็ว':0,'หอม':0,'ปลื้ม':0,'โอเค':0,'ถูกใจ':0,'ชุ่ม':0,'ชื่น':0,'ชื้น':0,'กันน้ำ':0,'ปกป้อง':0,'ยกให้':0,'ตัวโปรด':0,'ง่าย':0,'โอ':0,'ไว':0,'เลิฟ':0,'ที่ดีที่สุด':0,'ที่ดี':0,'กัน':0,'ต้องแบรนด์นี้':0,'โปรด':0,'ในดวงใจ':0,'ดีกว่า':0,'การปกป้อง':0,'คุณภาพ':0}
negative_sentiments_skin_protection = {'แรง':0,'แปลก':0,'เหนียวเหนอะหนะ':0,'เหนียว':0,'เหนอะ':0,'เหนอะหนะ':0,'หนืด':0,'คราบ':0,'ระคายเคือง':0,'ช้า':0,'ฉุน':0,'แรง':0,'จาง':0,'เหม็น':0,'แย่':0,'ไม่ชอบ':0}
inverse_sentiments_skin_protection = {'ไม่':0,'ไม่ค่อย':0,'ไปนิด':0}

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

def report(token,comment_id,feature,case,pos_sentiment,neg_sentiment,inv_sentiment,debugMode=False):
	if debugMode:
		if pos_sentiment == False and neg_sentiment == False :
			print ("Can't detect feature : %s (case:%s, comment_id:%s) from token : %s"%(feature,comment_id,case,token))
	else:		
		if pos_sentiment == False and neg_sentiment == False :
			pass
		else :
			if pos_sentiment :
				ans = 'POSITIVE'
			elif neg_sentiment:
				ans = 'NEGATIVE'
			if inv_sentiment:
				if ans == 'POSITIVE':
					ans = 'NEGATIVE'
				elif ans == 'NEGATIVE':
					ans = 'POSITIVE'
			if case == 1:
				print (token)
				print ("case 1 (Feature : %s) - comment_id : %s\npos : %s\nneg : %s\ninv = %s\nANS : %s\n\n"%(feature,comment_id,pos_sentiment,neg_sentiment,inv_sentiment,ans))
			elif case == 2:
				print (token)
				print ("case 2 (Feature : %s) - comment_id : %s\npos : %s\nneg : %s\ninv = %s\nANS : %s\n\n"%(feature,comment_id,pos_sentiment,neg_sentiment,inv_sentiment,ans))
			elif case == 3:
				pass
			elif case == -3:
				pass

def pattern_lipstick(row,f,debugMode):
	color = 0 
	smell = 0
	durable = 0
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		comment = row[3].replace('ๆ','')
		token = wordcut.tokenize(comment)
		try:
			for i in range(len(token)):
				pos_sentiment = False
				neg_sentiment = False
				inv_sentiment = False
				check_case_two = False
				case = 0
				if token[i] in features_lip: # 1,2
					for a in range(2):
						check_case_two = (i-a >= 0) and (token[i-a] in positive_sentiments_lip or token[i-a] in negative_sentiments_lip)
					if check_case_two : # 2
						case = 2
						for b in range(4):
							if b < 3 and  i-b >= 0 and token[i-b] in positive_sentiments_lip :
								pos_sentiment = True
							if b < 3 and i-b >= 0 and token[i-b] in negative_sentiments_lip :
								neg_sentiment = True
							if i-b >=0 and token[i-b] in inverse_sentiments_lip:
								inv_sentiment = True
								break
					else: #1
						case = 1
						for d in range(5):
							if d < 2 :
								if (i-1-d >= 0 and i-1-d <len(token)) and token[i-1-d] in inverse_sentiments_lip :
									inv_sentiment = True
							if d < 4 :
								if (i+1+d >= 0 and i+1+d <len(token)) and token[i+1+d] in inverse_sentiments_lip:
									inv_sentiment = True
							if d < 5 :
								if (i+1+d >= 0 and i+1+d <len(token)) and  token[i+1+d]	in positive_sentiments_lip :
									pos_sentiment = True
									break
								elif (i+1+d >= 0 and i+1+d <len(token)) and token[i+1+d] in negative_sentiments_lip :
									neg_sentiment = True
									break

					# score calculation
					if inv_sentiment == False:
						if token[i] == "สี":
							color += int(pos_sentiment) - int(neg_sentiment)
						elif token[i] == "กลิ่น":
							smell += int(pos_sentiment) - int(neg_sentiment)
						elif token[i] == "ติด":
							durable += int(pos_sentiment) - int(neg_sentiment)
					else:
						if token[i] == "สี":
							color += -int(pos_sentiment) + int(neg_sentiment)
						elif token[i] == "กลิ่น":
							smell += -int(pos_sentiment) + int(neg_sentiment)
						elif token[i] == "ติด":
							durable += -int(pos_sentiment) + int(neg_sentiment)
					report(token,row[0],token[i],case,pos_sentiment,neg_sentiment,inv_sentiment,debugMode)

				else: #3
					if token[i] in alone_positive_sentiment_lip:
						case = 3
						print ("case 3")
					elif token[i] in alone_negative_sentiment_lip:
						case = -3
						print ("case -3")
		except (TypeError):
			pass
		f.write("%s,%d,%d,%d\n"%(row[0],color,smell,durable))		
		# print("%s,%d,%d,%d\n"%(row[0],color,smell,durable))

def openMultipleFile(function):
	file_dict = {}
	if 'lipstick' in function :
		f_lip = writeFile('./data/opinion_lip.csv')
		file_dict['lipstick'] = f_lip
	if 'skin_protection' in function :
		f_skin = writeFile('./data/opinion_skin.csv')
		file_dict['skin_protection'] = f_skin
	
	return (file_dict)

def closeMultipleFile(function,f_all):
	if 'lipstick' in function :
		f_all['lipstick'].close()
	if 'skin_protection' in function :
		f_all['skin_protection'].close()

def pattern_skinProtection(row,f,debugMode):
	sticky = 0
	permeate = 0
	stain = 0
	smell = 0
	moist = 0
	irritate = 0
	waterproof = 0
	sunproof = 0
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		comment = row[3].replace('ๆ','').split(' ') 
		for part in comment:
			token = wordcut.tokenize(part)
			try:
				for i in range(len(token)):
					pos_sentiment = False
					neg_sentiment = False
					inv_sentiment = False
					check_case_two = False
					case = 0
					if token[i] in features_skin_protection: # 1,2
						for checkcase in range(4) : #0-3
							if (i-checkcase >= 0 and i-checkcase <len(token)) and (token[i-checkcase] in positive_sentiments_skin_protection or token[i-checkcase] in negative_sentiments_skin_protection ):
								check_case_two = True
						if (check_case_two) : # type 2
							case = 2
							for b in range(5):
								if i-b >=0 and token[i-b] in positive_sentiments_skin_protection :
									pos_sentiment = True
								elif i-b >=0 and token[i-b] in negative_sentiments_skin_protection :
									neg_sentiment = True
								elif i-b >=0 and token[i-b] in inverse_sentiments_skin_protection:
									inv_sentiment = True
									break
						else: #1
							case = 1
							for d in range(5):
								if d < 2 :
									if (i-d >= 0 and i-d <len(token)) and token[i-d] in inverse_sentiments_skin_protection :
										inv_sentiment = True
								if d < 4 :
									if (i+d >= 0 and i+1+d <len(token)) and token[i+d] in inverse_sentiments_skin_protection:
										inv_sentiment = True
								if d < 6 :
									if (i+d >= 0 and i+d <len(token)) and  token[i+d] in positive_sentiments_skin_protection :
										pos_sentiment = True
										break
									elif (i+d >= 0 and i+d <len(token)) and token[i+d] in negative_sentiments_skin_protection :
										neg_sentiment = True
										break

						# score calculation
						# 'คราบ':0,'กลิ่น':0,'หอม':0,'ชุ่มชื่น':0,'ชุ่ม':0,'ระคายเคือง':0,'กันน้ำ':0,'กันแดด':0}
						if inv_sentiment == False:
							if token[i] in {'เหนียวเหนอะหนะ','เหนอะหนะ','เหนียว','เหนอะ','หนืด'}:
								sticky += int(pos_sentiment) - int(neg_sentiment)
							elif token[i] in {'ซึม'}:
								permeate += int(pos_sentiment) - int(neg_sentiment)
							elif token[i] in {'คราบ'}:
								stain += int(pos_sentiment) - int(neg_sentiment)
							elif token[i] in {'กลิ่น','หอม'}:
								smell += int(pos_sentiment) - int(neg_sentiment)
							elif token[i] in {'ชุ่มชื่น','ชุ่ม'}:
								moist += int(pos_sentiment) - int(neg_sentiment)
							elif token[i] in {'ระคายเคือง'}:
								irritate += int(pos_sentiment) - int(neg_sentiment)
							elif token[i] in {'กันน้ำ'}:
								waterproof += int(pos_sentiment) - int(neg_sentiment)
							elif token[i] in {'กันแดด','แสงแดด'}:
								sunproof += int(pos_sentiment) - int(neg_sentiment)
						else:
							if token[i] in {'เหนียวเหนอะหนะ','เหนอะหนะ','เหนียว','เหนอะ','หนืด'}:
								sticky += -int(pos_sentiment) + int(neg_sentiment)
							elif token[i] in {'ซึม'}:
								permeate += -int(pos_sentiment) + int(neg_sentiment)
							elif token[i] in {'คราบ'}:
								stain += -int(pos_sentiment) + int(neg_sentiment)
							elif token[i] in {'กลิ่น'}:
								smell += -int(pos_sentiment) + int(neg_sentiment)
							elif token[i] in {'ชุ่มชื่น','ชุ่ม'}:
								moist += -int(pos_sentiment) + int(neg_sentiment)
							elif token[i] in {'ระคายเคือง'}:
								irritate += -int(pos_sentiment) + int(neg_sentiment)
							elif token[i] in {'กันน้ำ'}:
								waterproof += -int(pos_sentiment) + int(neg_sentiment)
							elif token[i] in {'กันแดด','แสงแดด'}:
								sunproof += -int(pos_sentiment) + int(neg_sentiment)
						
						report(token,row[0],token[i],case,pos_sentiment,neg_sentiment,inv_sentiment,debugMode)

					else: #3
						pass
					# 	if token[i] in alone_positive_sentiment_skin_protection:
					# 		case = 3
					# 		print ("case 3")
					# 	elif token[i] in alone_negative_sentiment_skin_protection:
					# 		case = -3
					# 		print ("case -3")
			except (TypeError):
				pass
		f.write("%s,%d,%d,%d,%d,%d,%d,%d,%d\n"%(row[0],sticky,permeate,stain,smell,moist,irritate,waterproof,sunproof))		
		# print("%s,%d,%d,%d,%d,%d,%d,%d,%d\n"%(row[0],sticky,permeate,stain,smell,moist,irritate,waterproof,sunproof))		

def opinion(csvfile,function):
	# comments => 0:comment_id,1:item_id,2:coment_title,3:comment_com,4:age,5:rate
	spamreader = csv.reader(csvfile, delimiter=',')
	typeOfItem = matchItemIdToType()
	f_all = openMultipleFile(function)
	for row in spamreader:
		if ( 'lipstick' in function and typeOfItem[row[1]] == "lipstick" ):
			pattern_lipstick(row,f_all['lipstick'],debugMode=True)
		if ( 'skin_protection' in function and typeOfItem[row[1]] == "skin protection" ):
			pattern_skinProtection(row,f_all['skin_protection'],debugMode=False)

	closeMultipleFile(function,f_all)

def main():
	comments = readFile('./data/comments-removing-redundant.csv')
	opinion(comments,{'lipstick'}) #skin_protection, lipstick
	# test()

def  test():
	with open('bigthai.txt', encoding="UTF-8") as dict_file:
		word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
		wordcut = Wordcut(word_list)
		print (wordcut.tokenize("ไม่ค่อยชอบกลิ่นเลยค่ะ"))
	

if __name__ == '__main__' :
	main()