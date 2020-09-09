import csv

# opening the csvfile
with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

# sorting out the first 3 car details in the list and printing them accordingly
for x in mpg[:3]:
    for y,z in x.items():
        print(y,z)

ctylst, hwylst, cyllst, clslst, hwympgbycls, ctympgbycyl = list(), list(), list(), list(), [], []
for x in mpg:
    ctylst.append(int(x['cty']))
    hwylst.append(int(x['hwy']))
print('City mpg:', '%.2f'%float(sum(ctylst)/len(ctylst)))
print('Highway mpg:', '%.2f'%float(sum(hwylst)/len(hwylst)))
cyllst = set(cyllst)
print(cyllst)
## print(sum(float(d['cty']) for d in mpg) / len(mpg))
## print(sum(float(d['hwy']) for d in mpg) / len(mpg))
## cylinders = set(d['cyl'] for d in mpg) : print(cylinders)

## lines 25 - 37 are for getting the highway mpg per vehicle class
for x in mpg:
    clslst.append(x['class'])
clslst = set(clslst)
for x in clslst:
    sum = 0
    count = 0
    for y in mpg:
        if y['class'] == x:
            sum += int(y['hwy'])
            count += 1
    hwympgbycls.append((x, sum/count))
for x,y in hwympgbycls:
    print('Highway mpg for class', x, 'is:','%.2f'%y,'mpg')
