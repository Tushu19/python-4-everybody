fname = input("Enter a file name:")
try:
    fh = open(fname)
except:
    print("File did not open!")
    quit()
count = 0
totvalue = 0
for lines in fh:
    if not lines.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        value = lines[19:]
        value = value.rstrip()
        value = float(value)
        totvalue = totvalue + value
average = totvalue / count
print("Average spam confidence:", average)
