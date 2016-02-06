
import numpy as np


def npFunctions():

    # Returns 6 equally spaced points between
    # 10^-4 and 10^-1.
    print np.logspace(-4,-1,6)


'''
Implements methods for lists of lists.

'''

def listOfLists():

    a = [[1,2],[3,4]]
    a = np.int0(a)
    print a
    #Put all lists' contents into one list
    print a.ravel()


def main():
    npFunctions()
    listOfLists()

if __name__ == '__main__':
    main()