import argparse
import fileinput
def parsebyword(file,type,word):
    try:

        count=0
        with open(file, "r") as f:
            for line in f:
                if type==True:
                    word = word.casefold()
                    line = line.casefold()

                linearray = line.split(word)
                temp = len(linearray) - 1
                count = count + temp
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
    args = parser.parse_args()

    count=0
    word=args.w
    f1 = args.filename
    try:
        count = parsebyword(f1,args.i,word)

        print("The word ",word,"is case sensitve:",args.i,",occured " , count," times in file" )
    except:
        print("error")
if __name__== '__main__':
    main()










