fname = input("Enter a file name: ")
if len(fname) < 1:
    fname = "mbox=short.txt"
try:
    fh = open(fname)
except:
    print("File did not open!")
    quit()
counts = dict()
for lines in fh:
    if not lines.startswith("From "):
        continue
    else:
        line = lines.split()
        emails = line[1]
        counts[emails] = counts.get(emails,0) + 1
bigemail = None
bigcount = None
for emails,count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = emails
        bigcount = count
print(bigemail, bigcount)
