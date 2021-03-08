#Find an intro to lists here
#https://www.w3schools.com/python/python_lists.asp

#Read in a file, split() it on space to get a list of words, then find every word
#that starts with a capital letter or has a digit
#See if you can read the words into a list using a list comprehension

import sys

#the following is a way to split the file using list comprehension
#splits each line in the file and adds the words in each line to the list of words
words = [word for line in open(sys.argv[1], 'r') for word in line.split()]

#The following is a more straightforward approach that reads in the file and then
#splits the file, uncomment it if you want to try it out!

#myFile = open(sys.argv[1], 'r')
#content = myFile.read()
#words = content.split()

#define an empty list
capOrDigit = []

#go through the words of the file and if they begin with a capital letter or start
#with a digit add it to the list
for word in words:
    if word[0].isupper():
        capOrDigit.append(word)
    if word[0].isdigit():
        capOrDigit.append(word)

print(capOrDigit)

#Start with an empty list and then use a for loop to add every integer between 1
#and 20 that is divisible by 3

#start with an empty list
divByThree = []

#loop through range of 1 to 20, if index is divisible by 3 add it to the list
for i in range(1, 21):
    if i % 3 == 0:
        divByThree.append(i)

print(divByThree)

#Use a list comprehension instead of a loop to add every integer between 1 and 20
#that is divisible by 3 to a list

numsByThree = [x for x in range (1, 21) if (x % 3 == 0)]

#Another alternative that begins with a list filled from 1 to 21 (above example
#is preferable)

#nums = list(range(1, 21))
#numsByThree = [x for x in nums if (x % 3 == 0)]

print(numsByThree)
