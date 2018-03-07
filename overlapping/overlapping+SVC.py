from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing
import pandas as pd
import numpy as np 

from sklearn.svm import LinearSVC

#open file and selecting sheet 
file='overlapping.xlsx'
sheet=pd.ExcelFile(file)
df=sheet.parse("Sheet1")

def labelEncoding(df):

	label_encoding=preprocessing.LabelEncoder()
	df['CategoryLabel']=label_encoding.fit_transform(df['Category'])
	return df
label_encode=labelEncoding(df)
#writing the labels for categories into file
def WriteToFile(df):
	np_array=df.values
	writer =pd.ExcelWriter('overlapping.xlsx')
	df.to_excel(writer,'Sheet2')
	writer.save()
def splitSet(df):
	from sklearn.model_selection import train_test_split
	question_train, question_test, category_train, category_test = train_test_split(df['Question'], df['CategoryLabel'], test_size=0.2,random_state=50)
	splitset=[question_train,question_test,category_train,category_test]
	return splitset
split=splitSet(label_encode)
question_train=split[0]
question_test=split[1]
category_train=split[2]
category_test=split[3]
def Vectoriser(question_train,question_test,category_train,category_test):	
	#Count Vectoriser 
	vectorizer = CountVectorizer()
	
	#training set 
	X_train = vectorizer.fit_transform(question_train).toarray() 
	y_train=list(category_train)

	#testing set
	X_test=vectorizer.transform(question_test).toarray()
	y_test=list(map(int, category_test))
	vectoriser_output=[X_train,X_test,y_train,y_test]
	return vectoriser_output
vectoriser_output =Vectoriser(question_train,question_test,category_train,category_test)
X_train=vectoriser_output[0]
X_test=vectoriser_output[1]
y_train=vectoriser_output[2]
y_test=vectoriser_output[3]

def SVCclassifier(X_train,X_test,y_train,y_test):
	#linear SVC 
	clf=LinearSVC()
	clf.fit(X_train,y_train)
	#predicting the results

	y_pred=list(map(int,clf.predict(X_test)))
	return y_pred
y_pred=SVCclassifier(X_train,X_test,y_train,y_test)

def outputMetrics(y_pred,y_test):
	from sklearn.metrics import classification_report
	print(classification_report(y_test,y_pred))

	from sklearn.metrics import confusion_matrix 	
	print(confusion_matrix(y_test,y_pred,labels=[4,5,1,0,3,2]))
	from sklearn.metrics import accuracy_score
	print(accuracy_score(y_test,y_pred))
outputMetrics(y_pred,y_test)
