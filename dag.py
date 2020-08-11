#!/usr/bin/env python

import sys, random, getopt

#Setup vars
acronym = ""
word_list = open('words/swearWords', 'r')
bad_words = []
output = ""

#Check for passed acronym
argv = sys.argv[1:]
try:
    options, arguments = getopt.getopt(argv, "a:")
except getopt.GetoptError:
    print("dag.py -a <Acronym>")
    sys.exit((2))

for option, argument in options:
    if option == '-a':
        acronym = argument

#add all words into a list
for line in word_list:

    line = line.strip('\n')
    bad_words.append(line)

#if acronym wasnt passed ask for it
if not acronym:
    while not acronym.isalpha():
        acronym = input("Please input your letter acronym (Letters Only): ")

#loop through acronym and find all words that start with that letter of the acronym
for letter in acronym:
    matched_words = []

    for word in bad_words:

        if word[0].lower() == letter.lower():

            matched_words.append(word)

#Select a random word frome the applicable list, then add it to output
#If list is empty then do nothing
    if not matched_words == []:
        word_to_add = random.choice(matched_words)
        word_to_add = word_to_add.capitalize()
        output += word_to_add + " "

#Output
print("(" + acronym.upper() + ")" + " " + output)