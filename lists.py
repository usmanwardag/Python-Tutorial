import sys


def listConcepts():
	
	'''Illustrates basic list concepts'''

	a = ['Usman','Mahmood','Khan']
	b = a							#Does not create a copy
	c = a[:]						#Creates a copy
	a.append('-')
	print b 						#Changes with 'a'
	print c 						#Does not change with 'a'

	if 'Khan' in a:
		#do something
		print 'Yay'

	print '--------------------------------------------------'


def listMethods():

	'''Illustrates list methods'''

	a = ['Usman','Mahmood','Khan']
	b = [1,2,3]

	a.append('-')
	print a
	a.insert(0,'Mr.')
	print a
	a.extend(b)						#Adds elements of b towards the end
	print a
	a.remove('-')					#Finds the element and removes it
	print a
	a.pop(0)						#Removes the elemnt from index no.
	print a

	#Note that these methods do not return lists

	print '--------------------------------------------------'


def listComprehension():

	'''Illustrates List comprehension'''

	nums = [1, 2, 3, 4]
	vals = [10,11,12,13]
	print [n*n for n in nums] 
	print [n*n for n in nums if n>=3]
	print [n*j for n in nums for j in vals]


	print '--------------------------------------------------'


def main():
	listConcepts()
	listMethods()
	listComprehension()

if __name__ == '__main__':
	main()