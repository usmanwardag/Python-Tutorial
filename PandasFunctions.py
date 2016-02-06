import pandas as pd

'''
Creating Pandas DataFrame and populating
it.
'''


def pandasCreateDf():
    df = pd.DataFrame(columns=['A','B','C'])
    df.append([1,2,3])


def main():
    pandasCreateDf()


if __name__ == '__main__':
    main()