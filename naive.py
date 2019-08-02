#import packages
import nltk
nltk.download('punkt')
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import csv
l=[]
lp=[]
ln=[]

with open('train.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	for row in reader:
		l.append(row)
csvFile.close()

cl = NaiveBayesClassifier(l)

def txtblb(text_str):
	blob = TextBlob(text_str, classifier=cl)
	for sentence in blob.sentences:	
		val=sentence.classify()
		if(val=="pos"):
		   lp.append(val)
		if(val=="neg"):	
		   ln.append(val)
	    	

str1=input("Rate your past experiences : ")
str2=input("Hows your present going on : ")
str3=input("Whats your expectition about future : ")

txtblb(str1)
txtblb(str2)
txtblb(str3)

a=len(lp)
b=len(ln)
if(a>b):
	print("Optimist")
elif(a==b):
	print("Normal")
else:
	print("Pessimist")		


