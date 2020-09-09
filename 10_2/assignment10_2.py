# getting input file name from user
fname = input("Enter input name: ")
# entering file name with just pressing "Enter" for convenience
if len(fname) < 1:
    fname = "mbox-short.txt"
# sanity check if file opens successfuly or not
try:
    fh = open(fname)
except:
    print("File did not open!")
    quit()
# creating dictionary
count = dict()
# scanning each line of the document to get desired lines and run algorithms on them
for lines in fh:
    if not lines.startswith("From "):
        continue
    else:
        line = lines.split()
        time = line[5]
        # print(time)
        hour = time[:2]
        # print(hour)
        count[hour] = count.get(hour,0) + 1
# print(count)
# making temporary list to sort data
tmp = list()
# sorting data from dictionary
for k,v in count.items():
    newtup = (k,v)
    tmp.append(newtup)
tmp = sorted(tmp)
# print(tmp)
# printing data from list in the right format
for k,v in tmp:
    print(k,v)
