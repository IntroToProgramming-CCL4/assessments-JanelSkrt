places= ['Germany','Japan','England','Spain','Thailand']
print ("Original:", places)

print ("Alphabetical:", sorted(places))

print ("Original 2:", places)

print ("Reverse alphabetical:", sorted(places, reverse=True))

print ("Original 3:", places)

places.reverse()

print ('Reversed:', places)

places.reverse()

print ('Original after reversing:', places)

places.sort()

print ('Alphabetical order with Sort():', places)

places.sort(reverse=True)

print ('Reverse alphabetical with Sort():', places)