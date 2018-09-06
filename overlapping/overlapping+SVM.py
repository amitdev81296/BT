from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np 

from sklearn.svm import SVC

#open file and selecting sheet 
file='overlapping.xlsx'
sheet=pd.ExcelFile(file)
df=sheet.parse("Sheet2")

#preprocessing [labelEncoding]

label_encoding=preprocessing.LabelEncoder()
df['CategoryLabel']=label_encoding.fit_transform(df['Category'])
print(label_encoding.inverse_transform([0,1,2,3,4,5]))

#writing the labels for categories into file
def WriteToFile(df):
	np_array=df.values
	writer =pd.ExcelWriter('overlapping.xlsx')
	df.to_excel(writer,'Sheet2')
	writer.save()
WriteToFile(df)

#splitting into test and train rs=90
question_train, question_test, category_train, category_test = train_test_split(df['Question'], df['CategoryLabel'], test_size=0.20,random_state=0)
#print(question_test)
#Count Vectoriser 
vectorizer = CountVectorizer()
#training set 
X_train = vectorizer.fit_transform(question_train).toarray() 
y_train=list(category_train)
#testing set
X_test=vectorizer.transform(question_test).toarray()
y_test=list(map(int, category_test))
#linear SVC 
clf=SVC()
from sklearn.model_selection import cross_val_score
scores = cross_val_score(clf,X_train,y_train, cv=10)
#from sklearn.metrics import accuracy_score

'''
clf.fit(X_train,y_train)
predicting the results

y_pred=list(map(int,clf.predict(X_test)))


from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))


from sklearn.metrics import confusion_matrix 
print(confusion_matrix(y_test,y_pred,labels=[4,5,1,0,3,2]))

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))
'''
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

