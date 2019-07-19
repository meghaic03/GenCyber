'''
Your program should be able to read a file and then counts
the word frequencies in the file

In terminal: python count_words.py -f INPUT_FILE -o OUTPUT_FILE
'''
import argparse
parser = argparse.ArgumentParser(description='This is a File manipulation program.  Input your file.  Input format: -f INPUT_FILE -o OUTPUT_FILE')

parser.add_argument("-f", required = True, type=argparse.FileType('r'),   help="Input file required!")

parser.add_argument("-o", type=argparse.FileType('w'), help="Name of output file", nargs = '?')

args = parser.parse_args()

if args.o:
    OutputFileName = args.o.name

'''
accepts one line at a time from a file and removes characters that are not needed
#(all characters except a-z, A-Z, and 0-9), and replaces with a space, and deletes all " ' "
updates stripped lines onto a new file
'''
def cleanupLine(File_in,  OUTPUTin):
        FILE20 = open(File_in, "r")
        OUTPUT = open(OUTPUTin, "w")
        line = FILE20.readline()
        while line:
            newline= cleanupLineLogic(line)
            OUTPUT.write(newline+ "\n")
            line = FILE20.readline()
        FILE20.close()
        OUTPUT.close()

def cleanupLineLogic(str1):
    str2 = ""
    len1= len(str1)
    for i in range (0, len1):
        if str1[i].isalnum():
            str2+= str1[i]
        elif (str1[i] == "'"):
            str2+= ""
        else:
            str2 += " "
    return str2

'''
counts the words in the first line from the stripped output file (above)
and updates the variable wordsDict{}
'''
def countWords(File_in):
        FILE20 = open(File_in, "r")
        line = FILE20.readline()
        newline= countWordsLogic(line)
        return (newline)
        FILE20.close()

def countWordsLogic(line1):
    line2 = line1.lower()
    wordsDict = dict()
    words = line2.split()
    for i in words:
        if i in wordsDict:
            wordsDict[i] += 1
        else:
            wordsDict[i] = 1
    return wordsDict

'''
returns a list with the frequencies as follows:
 "to" for File1.txt (requirements document)
 "the" for File2.txt (levels description)
 "computer" for File3.txt (Download Python and PyCharm instructions)
'''
f1 = open("File1.txt" , "r+")
f2 = open("File2.txt" , "r+")
f3 = open("File3.txt" , "r+")

def count_specified_word(file,specified_word):
    count = 0
    line = file.readline()
    while line:
        words = line.split()
        len1 = len(words)
        for i in range (0,len1):
            if words[i] == specified_word:
                count +=1
        line = file.readline()
    return count

def results():
    num1 = count_specified_word(f1, "to")
    num2 = count_specified_word(f2, "the")
    num3 = count_specified_word(f3, "computer")
    list1 = [num1, num2, num3]
    return list1
    f1.close()
    f2.close()
    f3.close()

#main function (calling the functions)
cleanupLine(args.f.name, OutputFileName)
countWords(OutputFileName)
results()
