#importing regex to use re.search and re.findall functions
import re
fname = input("Enter file name: ")
#convenience by opening test.txt by just pressing Enter
if len(fname) < 1:
    fname = "actual-data.txt"
#sanity check for file opening
try:
    fh = open(fname)
except:
    print("File did not open!")
    quit()
total = 0
#lst = list with sublists of integers per line that has integers
lst = list()
#flatlst = final big list of all integers in a file
flatlst = list()
#reading lines in file
for lines in fh:
    #filtering out lines that do not have an integer in them
    if not re.search('[0-9]+', lines):
        continue
    else:
        stuff = re.findall('[0-9]+', lines)
        #print(stuff)
        #appending found numbers in a list
        lst.append(stuff)
#problem was, each line that had an integer made a list of those integers
#within the previous list. Essentially creating a list within a list of
#integers.
#this algorithm is to take out numbers from the sublists and append them
#to a new list to have one list of all the integers.
for list in lst:
    for numbers in list:
        flatlst.append(numbers)
#print(flatlst)
#getting the sum of all the integers in the list.
for num in flatlst:
    total += int(num)
print(total)
