
#!/usr/bin/python
# -*- encoding: UTF-8 -*-

import sys
import csv
import codecs

# Defines list of punctuation characters that must not be taken into account

punctuation = [' ' , '\n' , '\r' , ',' , '.' , ';' , ':' , '!' , '@' , '#' , '$' , '%' , '^' , '*' , '(' , ')' , '-' , '_' , '+' , '=' , '/' , '|' , '?' , "'" , '[' , ']' , '{' , '}' , '<' , '>' , '~' , '"' , '\t', '&', '»'.decode( 'utf-8' ) , '«'.decode( 'utf-8' ) , '·'.decode( 'utf-8' ) , '”'.decode( 'utf-8' ) , '“'.decode( 'utf-8' ) , '—'.decode( 'utf-8' ) , '’'.decode( 'utf-8' ) , '‘'.decode( 'utf-8' ),'\ufeff'.decode( 'utf-8 ') , '̄'.decode( 'utf-8' ), '\xef\xbb\xbf'.decode( 'utf-8' )]





# Prints list of punctuation characters
#i = 0
#while i < len(punctuation):
#	print punctuation[i]
#	i = i + 1


# Opens the book
book = sys.argv[1]
infile = codecs.open(book, "r" , "utf8")
output = codecs.open("frecuencias_" + sys.argv[1], "w", "utf8")

#Load the full text by lines
texto = infile.readlines()

#Builds the dictionary and a list where appearance is registered.
dictionary = []
characterCount = []
frequencies = []
table = []


def buildDic(text):
	predictionary =[]
	for linea in text :
		for c in linea :
			if (c not in punctuation) :
				predictionary.append(c)
				
	dictionary.extend(list(set(predictionary)))

#Function that tracks a letter in the dictionary and gives its position
def findPosition(letter):
	index = 0
	i = 0
	found = False
	while i < len(dictionary) and found == False:
		if (letter == dictionary[i]):
			index = i
			found = True	
		i = i + 1	
	
	return index

#Function that adds 1 to the count of appearance of a character
def addToCount(letter):
	position = findPosition(letter)
	numberOfAppearance = characterCount[position]
	characterCount[position] = numberOfAppearance + 1



#Function that counts the appearance of each character
def count(dic, text):

	for character in dic:
		times = 0.0
		for line in text:
			times += line.count(character)
		
		characterCount.append(times)

	
#Function that arranges the appearance register and dictionary from most to least common character
def arrange(lista1, lista2):
	i = 0
	while i < len(lista1):
		j = i + 1	
		while j < len(lista1):
			if lista2[i] < lista2[j]:
				tempC = lista1[i]	
				tempN = lista2[i]
				lista1[i] = lista1[j]
				lista2[i] = lista2[j]
				lista1[j] = tempC
				lista2[j] = tempN
			j = j +1
		i = i +1	

#Function that computes amount of appearances of all characters together
def amount():
	i = 0.0	
	for number in characterCount:
		i+=number
	return i

#Function that computes frequency of appearance of a character
def frequency():
	i = 0
	while i < len(characterCount):
		total = amount()
		n = ((characterCount[i])/total)
		frequencies.append(n)
		i = i + 1

#Function that writes .txt file with characters
def joinLists(list1, list2):
	for i in range(len(list1)):	
		table.append((list1[i], list2[i]/amount()))


buildDic(texto)

count(dictionary, texto)

arrange(dictionary, characterCount)

frequency()

joinLists(dictionary, characterCount)

output.write('\n'.join("%s %s" % douple for douple in table))

output.close()

infile.close()
