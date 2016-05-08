# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 19:43:07 2015

@author: Kem Andrew
Contemporary Programming Languages
Dr. Stringfellow
Python - Evaluating the Readibility of Text.
         Calculating the Gunning Fog Index of
         an article.
11/16/2015
"""
import sys
import string
print 'Kem Andrew'

num_lines = 0
num_sentences = 0
num_words = 0
difficult_words = 0
my_list = []
GFI = 0.4

text_file = open("c:\users\kem\desktop\data4.txt",'r')

for each_line in text_file:
    #print(each_line)

    #increment the number of lines
    num_lines+= 1

    #calculate number of sentences
    num_sentences += each_line.count('.') + each_line.count('!') + each_line.count('?')

    #Splits the lines into a list of words
    tempwords = each_line.split(None)

    #calculate number of words
    num_words += len(tempwords)

    #Add each word to the list
    for i in tempwords:
        my_list.append(i)

print "The number of lines: ", num_lines
print "The number of sentences: ", num_sentences
print "The number of words: ", num_words

#print my_list


#prints an error message if file has less than 100 words
if num_words < 100:
    print("The file does not contain 100 words. ")
    sys.exit()


#Close the text file
text_file.close()

print '-' * 40

print ("Calculate Gunning Fog Index...")

# Variables and counters
count = 1
wordsinsent = 0
numwords = []
sentences = 0

# This variable holds all punctuation mark characters
punct = string.punctuation

# Loop through each word to perform calculations
for i in range(0, 99):

    # counts each wordin the sentence
    wordsinsent +=1

    #create variable to store words and remove punctuation
    word = my_list[i]
    word = word.strip(punct)

    # counts words with length greater than 8
    if len(word) >= 8:
        #print word
        difficult_words += 1

    #checks if this is the end of a sentence and counts sentences
    if '.' in my_list[i] or '!' in my_list[i] or '?' in my_list[i]:
        #print 'yes'
        sentences += 1
        numwords.append(wordsinsent)
        wordsinsent = 0

#Make calculations for GFI
sumwords = sum(numwords)
average = (sumwords/wordsinsent)
percentdiff = (float(difficult_words)/sumwords)*100.0
total = average + percentdiff
fogindex = GFI * total


# Output statements
print "# of sentences:", sentences
print "# of words in each sentence:", numwords
print "# of difficult words: ", difficult_words
print "percent difficult words: ", round(percentdiff, 2)
print "Gunning Fog Index: ", round(fogindex, 0)

if fogindex > 12:
    print ("General public will have difficulty understanding text material.")
else:
    print ("General public will understand text material.")

saveFile = open('data.txt','w')
#saveFile.write()
saveFile.close
