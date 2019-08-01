#import packages
import nltk
nltk.download('punkt')
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import csv
l=[]

#read csv files
with open('train.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        l.append(row)
csvFile.close()

cl = NaiveBayesClassifier(l)


str=input("Enter a string : ")
# Classify a TextBlob
blob = TextBlob(str, classifier=cl)

for sentence in blob.sentences:
    print(sentence.classify())






