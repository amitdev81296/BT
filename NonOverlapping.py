import csv 
from nltk import *
import os
import nltk
import csv,re
dataset='dataset.csv'
output_file='dataset_output.csv'
verblist="verbs_list.csv"

def WriteToFile(output_file,row,verb):
	with open(output_file,"w") as OP:
		writer=csv.writer(OP)
		writer.writerow([row[0],row[1],row[2],verb])

def SelectVerbCategory(verblist,verb):
	category=[]
	verb=verb.lower()
	with open(verblist) as File:
		reader=csv.reader(File)
		for row in reader:
			for word in row:
				if word==verb:
					category.append(row[0])
	File.close()
	if len(set(category)) ==0:
		return("Not in list")
	elif len(set(category)) ==1:
		return(category[0])
	else:
		return("Overlapping")

print(SelectVerbCategory(verblist,"Explain"))
def processContent(dataset):
	try:
		with open(dataset,'r+') as dataset:
			csvReader=csv.reader(dataset)
			for row in dataset:
				tokenData=sent_tokenize(row)   #sentence tokennizer used to split in case of multiplequestions in same sub-questions
				#if len(tokenData) ==1:
				word_token=word_tokenize(row)
				pos=pos_tag(word_token)
				
				
				for t in pos:
					if t[1]=="VB":
						print(t[0])
						category=SelectVerbCategory(verblist,t[1])
						#print(category)
						WriteToFile(output_file,row,category)
		dataset.close()
	except Exception as e:
		print(str(e))

#processContent(dataset)


