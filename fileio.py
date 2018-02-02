import csv
def SelectVerbCategory(verblist,verb):
	category=[]
	verb=verb.lower()
	with open(verblist) as File:
		reader=csv.reader(File)
		for row in reader:
			for word in row:
				if word==verb:
					category.append(row[0])
	File.close()
	if len(set(category)) ==0:
		return("Not a verb")
	elif len(set(category)) ==1:
		return(category[0])
	else:
		return("Overlapping")
	
SelectVerbCategory("non_overlapping_verbs.csv","Who")

def NonOverlapping(dataset,output_file):
	with open(dataset,"r") as IP:
		reader=csv.reader(IP)
		with open(output_file,"w") as OP:
			writer=csv.writer(OP)
			for row in reader:
				writer.writerow([row[0],row[1],row[2],verb])
