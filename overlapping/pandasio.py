import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
#from matplotlib import pyplot as plt
file='dataset.xlsx'
def RemoveDuplicatesAndOverlapping(file):
	sheet=pd.ExcelFile(file)
	df=sheet.parse("ConsolidatedSheet")
	df1=df.loc[df['Type']=='overlapping']
	df2=df1.drop_duplicates('Question')
	return df2

def WriteToFile(df):
	np_array=df.values
	writer =pd.ExcelWriter('overlapping.xlsx')
	df.to_excel(writer,'Sheet2')
	writer.save()

dataframe_op=RemoveDuplicatesAndOverlapping(file)
writing_to_file=WriteToFile(dataframe_op)
np_array=dataframe_op.values
train=np_array[:450,0:3]
test=np_array[-1:-50,0]
vect=CountVectorizer()
a=np_array[:,0]

vect.fit(a)

#print()
#vect.get_feature_names()  //names of tokens created
dtm=vect.transform(a)
print("Shape of Sparse Matrix:"+str(dtm.shape))
print("Non-Zero occurences:"+str(dtm.nnz))

#print(pd.DataFrame(dtm.toarray(), columns=vect.get_feature_names()))

