import csv 
from nltk import *
import os
import nltk
import csv,re
dataset='dataset.csv'
output_file='dataset_output.csv'
verblist="verb_list.csv"

def WriteToFile(output_file,content):
	print(content)
	with open(output_file,"a") as OP:
		writer=csv.writer(OP)
		writer.writerow([content])

def SelectVerbCategory(verblist,verb):
	category=[]
	verb=verb.lower()
	with open(verblist) as File:
		reader=csv.reader(File)
		for row in reader:
			for word in row:
				if word==verb:
					category.append(row[0])
	
	if len(set(category)) ==0:
		return("Not in list")
	elif len(set(category)) ==1:
		return(category[0])
	else:
		return("Overlapping")
	File.close()


def processContent(dataset):
	try:
		with open(dataset,'r+') as dataset:
			csvReader=csv.reader(dataset)
			for row in dataset:
				tokenData=sent_tokenize(row)   #sentence tokennizer used to split in case of multiplequestions in same sub-questions
				if len(tokenData) ==1:
					word_token=word_tokenize(row)
					pos=pos_tag(word_token)
					for (word,tag) in pos:
						if re.match(r"VB|WP",tag):
							category=SelectVerbCategory(verblist,word)
							content=row.strip("\n")+","+category
							WriteToFile(output_file,content)
		dataset.close()
	except Exception as e:
		print(str(e))

processContent(dataset)


