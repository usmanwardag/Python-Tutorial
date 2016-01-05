import sys

'''
Demonstrates string functions
'''

def stringMethods():


	s = 'Hello, how are you doing?'

	print s.strip()				#Removes whitespaces
	print s.lower()
	print s.upper()				#Changes case 
	print s.isalpha()
	print s.isdigit()
	print s.isspace()			#If all characters belong to a class
	print s.startswith('H')
	print s.endswith('ng?')
	print s.find('are')			#Locates the index where the char/string starts
	print s.replace('?', '!?')
	print s.split('o') 			#Splits on specified character
	examples = ['Usman','Mahmood','Khan']
	print ' '.join(examples)	#Joins list with a given character/string

	#Search for more by typing "Python String methods"

	print '---------------------------------------------------------------------'
	
'''
Demonstrates procedures to find sub-strings
'''

def stringSlicing():


	s = 'I am doing great! How about you?'

	print s[4:]					#all characters from 4 onwards
	print s[-1]					#last character
	print s[:-3]				#all characters until the third last
	print s[-5:]				#all characters starting from fifth last

	print '---------------------------------------------------------------------'

'''
Displays the string in unicode format
'''

def unicodeString():


	examples = ['Usman','Mahmood','Khan']
	s = ('\n').join(examples)
	t = unicode(s,'utf-8')
	print t						#String in unicode format

	print '---------------------------------------------------------------------'

'''
Main function to run test modules.
Run any one of above listed function to test
with commands.

'''


def main():

	stringMethods()
	stringSlicing()
	unicodeString()

if __name__ == '__main__':
	main()