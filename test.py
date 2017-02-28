import csv

def readFile(path):
	return open(path)

def writeFile(path):
	return open(path,'w')

def opinion(csvfile_items):
	spamreader_items = csv.reader(csvfile_items, delimiter=',')
	#barcode : 0:id,1:name,2:brand,3:barcode,4:description_eng,5:img,6:type
	#items : 0:item_id,1:name,2:brand,3:description_thai,4:img,5:type
	for row_items in spamreader_items:
		type_items = row_items[5]
		brand_items = row_items[2]
		name_items = row_items[1]
		id_items = row_items[0]


def main():
	csvfile_items = readFile('./data/comments.csv')
	opinion(csvfile_items)

if __name__ == '__main__' :
	main()