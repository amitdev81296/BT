
def overlapping(question):
	#open file and selecting sheet
	f='overlapping.xlsx'
	sheet=pd.ExcelFile(f)
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

op=overlapping([ip"])  #each question should be an array


########
'''
import nltk
import csv,re
import pandas as pd
import spacy
output_file='bt_output.xlsx'
verblist="verb_list.csv"
test_data='test.xlsx'
sheet=pd.ExcelFile(test_data)
df=sheet.parse("test")
print(df)

def WriteToFile(df,output_file):
	np_array=df.values
	writer =pd.ExcelWriter(output_file)
	df.to_excel(writer,'Sheet2')
	writer.save()

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
#text=nlp('explain the function')
def processContent(text):
    for token in nlp(text):
        if token.pos_=='VERB' or token.tag_ == "WDT" or token.tag_ == "WP" or token.tag_ == "WP$" or token.tag_ == "WRB" :
            verb=token.text
            category=SelectVerbCategory(verblist,verb)
            df['Category']=category
            break
df['Questions'].apply(processContent,axis=1)
print(df)     
    
import pandas as pd 
file='test.xlsx'
sheet=pd.ExcelFile(file)
df1=sheet.parse("test")
print(type(df1))
for index,row in df1.iterrows():
	print(row['Questions'])
	break
#if df1['Category']=='understand':
#	print(df1['Questions'])
'''
