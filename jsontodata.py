#################################File craeted by Tandra Chakraborty, emai: t3chakra@uwaterloo.ca
import sys
import json
import re
from collections import defaultdict

data_product=[]
data_list=[]
listings={} #to keep each listing as an array index
result=[] 

######################### Procedure to read products##############################
def productRead(fileName):
	classList={}
	with open(fileName,'r') as file1:
		line=file1.readlines()
		count = len(line)
		for i in range(0, count):
			a=json.loads(line[i])			
			for key in a:
				data_product.append((key,a[key]))
				

	file1.close()
	return;
##################### procedure to read listings##################################
def listRead(fileName):
	classList={}
	with open(fileName,'r') as file2:
		line=file2.readlines()
		count = len(line)
		for i in range(0, count):
			a=json.loads(line[i])
			listings[i]=a			
			for key in a:				
				data_list.append((key,a[key]))
				

	file2.close()
	return;

###Reading input files..in a order products.txt listings.txt
fileName=sys.argv[1]
productRead(fileName)
fileName=sys.argv[2]
listRead(fileName)


d = defaultdict(list)
for k,v in data_product:
	 d[k].append(v)

e = defaultdict(list)
for k,v in data_list:
	 e[k].append(v)


prod_count=len(d['manufacturer'])
list_count=len(e['manufacturer'])

key='manufacturer'




for i in range(0,prod_count):
	for j in range(0,list_count):
		str1=d[key][i].encode('utf-8')
		str2=e[key][j].encode('utf-8')
		######################### I match product with listings only if they have same manufacturer , this is my first filter, and then I use regex to find further similarity in product name and listing
		if (str1==str2):
			name=d['product_name'][i].encode('utf-8')
			findStr=re.findall(r"[A-Z a-z 0-9]+",name)
			title=e['title'][j].encode('utf-8')
			count =0
			for k in range(0,len(findStr)):
				if(findStr[k] in title):
					count=count+1
			if(count ==len(findStr)):							
				result.append((d['product_name'][i].encode('utf-8'),j))
final=defaultdict(list)
for k,v in result:
	final[k].append(v)
################################# Print the result in Json format##############################
for k in final:
	sys.stdout.write("{\n")
	sys.stdout.write("\"product_name\": "+ k+"\n")
	sys.stdout.write("\"listings\": [")
	for l in range(0,len(final[k])):		
		num=final[k][l]
		sys.stdout.write(json.dumps(listings[num]))	
	if(l!=len(final[k])-1):
			sys.stdout.write(",")
	sys.stdout.write("]\n")
	sys.stdout.write("}\n")
	
	


