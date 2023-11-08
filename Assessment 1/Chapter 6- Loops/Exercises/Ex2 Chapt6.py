while True:
    age = int(input('Enter age:'))#asks user imput for their age
    if age <=3:
        print("Tickets are free!") #if user is below 12 and above 3 the tickets are 10$
    elif age >=3 and age <=12:
        print("Tickets are 10$!")
    elif age >12:
        print("Tickets are 15$!")