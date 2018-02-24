from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from sklearn.svm import SVC
#open file
file='non-overlapping.xlsx'
sheet=pd.ExcelFile(file)
df=sheet.parse("Sheet1")
#selecting category
df['Category']=np.where(df['Category'] =="Remembering" ,1, 0)
np_array=df.values
question_train=np_array[:50,0]
category_train=np_array[:50,2]
question_test=np_array[-10:,0]
category_test=np_array[-10:,2]
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab

#vectorizer.fit(list(question_train) + list(question_test))
vectorizer.fit(question_train)

# encode document
X_train = vectorizer.transform(question_train).toarray() 
# summarize encoded vector

y_train=list(category_train)

X_test=vectorizer.transform(question_test).toarray()
y_test=list(map(int, category_test))
#SVC classifier

from collections import Counter
clf=SVC()


clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
score=clf.score(X_test,y_test)
print(score)
