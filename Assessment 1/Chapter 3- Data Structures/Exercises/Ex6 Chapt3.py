guests = ['Dobi', 'Bins', 'Danish']
for guest in guests:
    print ('I am delighted to inform that you are invited to dinner,', guest)

print (guests[0], 'Cant make it to dinner')
print ('Not coming:', guests[0])
guests.remove ('Dobi')
print ('Coming:', guests[0], guests[1])

guests.insert (0, 'Dobi')

guests = ['Dobi', 'Bins', 'Danish']
for guest in guests:
    print ('I am delighted to inform that you are invited to dinner,', guest)

print ('Im really sorry i can only invite 2 people for dinner')
poppedguest = guests.pop(0)
print ('Im sorry but you dont fit', poppedguest, 'maybe next time.')

for poppedguest in guests:
    print ('I am delighted to inform that you are still invited to dinner,', poppedguest)

del guests [0]
del guests [0]
print ('Remaining guests:',guests)