fname = input("Enter file name: ")
count = 0
fh = open(fname)
for lines in fh:
    if not lines.startswith("From "):
        continue
    else:
        emails = lines.rstrip().split()
        print(emails[1])
        count = count + 1
print("There were",count,"lines in the file with From as the first word")
