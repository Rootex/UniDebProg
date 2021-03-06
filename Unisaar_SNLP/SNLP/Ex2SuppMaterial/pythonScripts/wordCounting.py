import os
from sets import Set

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'dataset/')

#insert the paths of the training spam and non spam dataset. Don't remove the r before ''
pathSpamTrain=DATA_PATH + 'spam-train'
pathNonSpamTrain=DATA_PATH + 'nonspam-train'

#Insert the threshold. Only words with document frequency bigger than the threshold will be printed
threshold=40 


#the following code will print 3 columns. First column is if the word is in the spam or non-spam collection.
#The second column is the word and the third  column is the document frequency of the term
#Notice that the document frequencies are not for the whole collection
def spamTrain(dictionary):
    for filename in os.listdir(pathSpamTrain):
        with open(pathSpamTrain+'/' +filename, 'r') as document:
            boo=False
            for line in document:
                tokens = line.split()
                for token in tokens:
                    if not dictionary.has_key(token.lower()):
                        docs=Set()
                        docs.add(filename)
                        dictionary[token.lower()]=docs
                    else:
                        dictionary[token.lower()].add(filename)
    return dictionary
#
        

def nonSpamTrain(dictionary):
    for filename in os.listdir(pathNonSpamTrain):
        with open(pathNonSpamTrain+'/' +filename, 'r') as document:
            boo=False
            for line in document:
                tokens = line.split()
                for token in tokens:
                    if not dictionary.has_key(token.lower()):
                        docs=Set()
                        docs.add(filename)
                        dictionary[token.lower()]=docs
                    else:
                        dictionary[token.lower()].add(filename)
    return dictionary

def print_data():
    dictionary=dict()
    for key in spamTrain(dictionary):
        if len(dictionary[key])>=threshold:
            print 'spam', key,len(dictionary[key])

    dictionary=dict()
    for key in nonSpamTrain(dictionary):
        if len(dictionary[key])>=threshold:
            print 'non-spam',key,len(dictionary[key])
        
        

