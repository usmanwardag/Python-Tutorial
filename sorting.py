import sys

def sortFunc(s):
	return s[-1]


def sortConcepts():

	'''Illustrates basic sorting through sorted()'''

	a = [5,2,1,3]
	print sorted(a)
	print sorted(a, reverse = True)

	a = ['aaa','bb','dda','cc']
	print sorted(a, key = len)					#Custom sorts can be done based on our choice of functions	
	print sorted(a, key=sortFunc)

	print '----------------------------------------------'

def main():

	sortConcepts()


if __name__ == '__main__':
	main()