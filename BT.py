'''
def overlapping(question):
	from sklearn.feature_extraction.text import CountVectorizer
	from sklearn import preprocessing
	import pandas as pd
	import numpy as np 
	from sklearn.svm import LinearSVC
	#open file and selecting sheet 
	file='overlapping.xlsx'
	sheet=pd.ExcelFile(file)
	df_train=sheet.parse("Sheet2")

	def training(df_train):

		label_encoding=preprocessing.LabelEncoder()
		df_train['CategoryLabel']=label_encoding.fit_transform(df_train['Category'])
		question_train=df_train['Question']
		category_train=df_train['CategoryLabel']
		vectorizer = CountVectorizer()
		#training set 
		X_train = vectorizer.fit_transform(question_train).toarray() 
		y_train=list(category_train)
		#linear SVC 
		clf=LinearSVC()
		clf.fit(X_train,y_train)
		return vectorizer ,clf,label_encoding

	def testing (question,vectorizer,clf,label_encoding):
		X_test= vectorizer.transform(question) 
		y_test=clf.predict(X_test)
		category=label_encoding.inverse_transform(y_test)
		question.append(category[0])
		return(question)

	vectorizer ,clf,label_encoding=training(df_train)
	output=testing(question,vectorizer,clf,label_encoding)
	return output

op=overlapping(["explain  the concept of mobile ip"])  #each question should be an array

'''
########
import csv 
from nltk import *
import os
import nltk
import csv,re
import pandas as pd
dataset='test.csv'
verblist="verb_list.csv"
import spacy
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

nlp=spacy.load('en')
question=[]
Category=[]	 
def processContent(dataset):
	try:
		with open(dataset,'r+') as dataset:
			csvReader=csv.reader(dataset)
			for row in dataset:
				row1=nlp(row)
				for token in row1:
					if token.pos_=='VERB' or token.tag_ == "WDT" or token.tag_ == "WP" or token.tag_ == "WP$" or token.tag_ == "WRB":
						verb=token.text
						category=SelectVerbCategory(verblist,verb)
						question.append(row.strip('\n'))
						Category.append(category)
						break
		dataset.close()
	except Exception as e:
		print(str(e))
processContent(dataset)

df=pd.DataFrame({'Questions':question,'Category':Category})
	



