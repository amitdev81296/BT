from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np 
import spacy 
from sklearn.svm import LinearSVC
nlp=spacy.load('en')
#open file
file='overlapping.xlsx'
sheet=pd.ExcelFile(file)
df=sheet.parse("Sheet2")

#preprocessing [labelEncoding]

label_encoding=preprocessing.LabelEncoder()
df['CategoryLabel']=label_encoding.fit_transform(df['Category'])
def WriteToFile(df):
	np_array=df.values
	writer =pd.ExcelWriter('overlapping.xlsx')
	df.to_excel(writer,'Sheet2')
	writer.save()
WriteToFile(df)

question_train, question_test, category_train, category_test = train_test_split(df['Question'], df['CategoryLabel'], test_size=0.2, random_state=50)


vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(question_train).toarray() 
y_train=list(category_train)
X_test=vectorizer.transform(question_test).toarray()
y_test=list(map(int, category_test))
clf=LinearSVC()
clf.fit(X_train,y_train)
y_pred=list(map(int,clf.predict(X_test)))



from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
