import pandas as pd 
file='dataset.xlsx'
sheet=pd.ExcelFile(file)
df=sheet.parse("ConsolidatedSheet")
df1=df.loc[df['Type']=='overlapping']
df2=df1.drop_duplicates('Question')
writer =pd.ExcelWriter('overlapping.xlsx')
df2.to_excel(writer,'Sheet1')
writer.save()
