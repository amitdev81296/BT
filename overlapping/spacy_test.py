import spacy 
nlp=spacy.load('en')
train=[[nlp('Discuss two ways of determining Trust.'),'Creating'],[nlp('Discuss the undesirable effects of virtualization.'),'Creating'],[nlp('Discuss the top security concerns for cloud users.'),'Creating'],[nlp('Discuss two ways of determining trust.'),'Creating'],[nlp('Discuss different aspects related to contract between the user and the Cloud Service Provider to minimize security risks.'),'Creating'],[nlp('What do you understand by Mesh? How will you add a system to a Mesh? How will you access a Mesh- Enabled Web application?'),'Remembering'],[nlp('What are public cloud adoption phases for SMBs ? What are cloud vendor roles and responsibilities towards SMBs.'),'Remembering'],[nlp('What are the risks associated with  cloud computing.'),'Remembering'],[nlp('What are the fundamental requirements for cloud application architecture.'),'Remembering'],[nlp('What is the need of virtualization? Define Server virtualization, Application virtualization, Presentation Virtualization.'),'Remembering'],[nlp('What is Data Migration?'),'Remembering'],[nlp('How is Amazon DynamoDB different from MYSQL database?'),'Remembering'],[nlp('What are security groups & key pairs?'),'Remembering'],[nlp('What is there significance in Amazon AWS cloud computing environment?'),'Remembering']]

test = [[nlp('Discuss the naming and addressing in wireless sensor network.'),'Creating'],[nlp('Differentiate between the content based and the geographic routing'),'Understanding'],[nlp('What is an IP Address?'),'Remembering'],[nlp('What are the challenges faced by distributed system'),'Remembering'],[nlp('State the relationship between HYPERLAN-2 and WATM.'),'Analysing']]


def SvCclassifier(test,train):
	from sklearn import svm
	X_train=[question[0] for question in train]
	y_train=[question[1] for question in train]
	X_test=[question[0] for question in test]
	X_test=[question[0] for question in test]	
	clf=svm.SVC()
	clf.fit(X,y)
	clf.predict(y_test[0])
	

'''
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import string
import re

steps=[('tokenisaton',tokeniser),('SVM',SVC())]
pipeline = Pipeline(steps)

def  toke



pipeline.fit(X_train,y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test,y_pred))


'''
from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()




	
