from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np 
import spacy 
from sklearn.svm import LinearSVC
nlp=spacy.load('en')
#open file00
file='non-overlapping.xlsx'
sheet=pd.ExcelFile(file)
df=sheet.parse("Sheet1")
#selecting category
#df['Category']=np.where(df['Category'] =="Remembering" ,1, 0)
question_train, question_test, category_train, category_test = train_test_split(df['Question'], df['Category'], test_size=0.3, random_state=45)

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(question_train).toarray() 
y_train=list(category_train)
X_test=vectorizer.transform(question_test).toarray()
y_test=list(map(int, category_test))
clf=LinearSVC(multi_class='crammer_singer')
clf.fit(X_train,y_train)
y_pred=list(map(int,clf.predict(X_test)))



from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))
