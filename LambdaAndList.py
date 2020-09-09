people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

print('----')
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

print(times_tables() == [i*j for i in range(10) for j in range(10)])

print('----')
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]
for x in answer[:50]:
    print(x)
