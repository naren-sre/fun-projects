import argparse
import fileinput
def parsebyword(file,type,word):
    try:

        count=0
        with open(file, "r") as f:  '''open file in read mode and read each line if type is set then change word and line to lowercase(casefold) and add read occurance into list by splitting till the word of your interest'''
            for line in f:
                if type==True:
                    word = word.casefold()
                    line = line.casefold()

                line = line.split(word)
                temp = len(line) - 1 '''substract -1 from total length of list because after last split of line by word we do not need that value'''
                count = count + temp  '''use temp variable to track count value through each line in file'''
        return count

    except:
        raise Exception()


def main():
    parser = argparse.ArgumentParser(
        description="read the file"
    )
    parser.add_argument("filename", help="path to a file")
    parser.add_argument("-i", help="input your case insensitve ", action='store_true')
    parser.add_argument("-w", help="input your word", type=str,default='')
    args = parser.parse_args() ''' read all arguments into dict'''

    count=0
    word=args.w '''user provided args about word of interest will be read into word'''
    f1 = args.filename
    try:
        count = parsebyword(f1,args.i,word)

        print("The word ",word,"is case sensitve:",args.i,",occured " , count," times in file" )
    except:
        print("error")
if __name__== '__main__':
    main()










