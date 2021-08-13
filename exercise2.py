# print('nice to meet you sir ? ')
# name = input ("can we ave your name  please ! ")
# color = input("what is your favourite color ? ")
# print (name + " like " + color)
# exercise 3 
# birth_year=input("Birth year : ")
# print (type(birth_year))
# age = 2021 - int (birth_year)
# print (age)
# print (type(age))
# print (" you are "+str(age)+ " year old ")
# exercise 4
# print ("it's been pleasure having you at our doorstep")
# weight = input("what is your weight in pounds ?  ")
# kg_weight = float(weight) *0.45
# print("your weight in kg is = "+ str(kg_weight))
#exercise 5
# cousre = "python-boss"
# print (cousre[1:-1])
 #formatted strings 
# first  ='John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder '
# # print(message)
# msg = f' {first} [{last}] is a coder '
# print (msg)
# course = 'Python for beginners '
# print (len(course))
# print(course.upper())
# print(course.lower())
# print (course.find('o'))
# print(course.replace('beginners ',' absolute beginners'))
# print(course.find('a'))
# course.replace('beginners ',' absolute beginners')
# print('python' in course )
# print (course.title())
#arithmatic operations 
# x=2.9
# print(round(x))
# print(abs(-2.9))

# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))
# print(math.comb(5,2))
# print(math.copysign(1.0,-0.0)) # return the value of x with the sign of y
# print(math.fabs(-2.5)) # return the absolute value 
# is_hot=False
# is_cold =True
# if is_hot:
#     print(" It's  a hot day")
#     print ("drink plenty of water ")
# elif is_cold :
#     print("It's a cold day")
#     print("Wear warm clothes")
# else :
#     print ("It's a lovely day")
    
# print("Enjoy you day")
# logical operators
# has_high_income= True
# has_good_credit=True
# name="jghjbfkakfhkahkfahkhfakfnfnbfigfuysatg"
# if len(name) < 3:
#     print("name must be atleast 3 character")
# elif len(name) >50 :
#     print ("Name must be maximum of 50 character")
# else :
#     print ("Name looks good")
# weight= input("Weight :  ")
# unit = input("(L)bs or (K)g :  ")

# if unit.upper() == 'K':
#     weight = float (weight)*2.20
#     print("you are " + str(weight)+ " Pounds")
# elif unit.upper() == 'L' :
#     weight = float(weight) *0.4536
#     print (f" you are {weight} kilos")
#  i=1
#  while i<=5:
#      print(i)
#      i=i+1
# print("Done")
# make a guess

# secret_number = 9
# guess_count=0
# guess_limit =3
# while guess_count<guess_limit:
#     guess=int (input("Guess :  "))
#     guess_count +=1
#     if guess ==secret_number :
#         print("you won hurrey!")
#         break;
# else :
#     print ("Sorry, You failed")
command =""
started=False
stoped=False
while True:
    command = input(" >  ").lower()  
    if command =="start" :
        if started:
            print("the car is already started")
        else :
            started =True
            print("car started Brum Brum!!")
        
    elif command=="stop" :
        if stoped:
            print("the car has already stopped!")
        else :
            stoped =True
            print("car stopped !")
    elif command =="help":    
        print(""" 
start - to start the car
stop - to stop the car
quit - to quit
              """)
    elif command.lower() == "quit":
        break           
    else :
        print(" Sorry, I don't understand it !")


    
    
      
      
      
      
      
      
      
      
      
      
      
      
