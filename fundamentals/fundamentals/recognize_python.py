num1 = 42 #variable declaration, initialize Number
num2 = 2.3 #variable declaration, initialize Number
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize Tuples
print(type(fruit)) #type check
print(pizza_toppings[1]) #access value
pizza_toppings.append('Mushrooms') #add value
print(person['name'])#access value
person['name'] = 'George'#change value
person['eye_color'] = 'blue' #add value
print(fruit[2]) # access value

if num1 > 45:
    print("It's greater")#conditional if
else:
    print("It's lower") #conditional else

if len(string) < 5: #conditional if
    print("It's a short word!")
elif len(string) > 15: #conditional else if
    print("It's a long word!")
else:
    print("Just right!") #conditional else

for x in range(5): #for loop (start from 0, stop 5)
    print(x)
for x in range(2,5): #for loop (start ,stop)
    print(x)
for x in range(2,10,3): #for loop (start ,stop,increment)
    print(x)
x = 0 #variable declaration, initialize Number
while(x < 5): #while loop ,start at 0 , stop at 5
    print(x)
    x += 1 #increment by 1

pizza_toppings.pop() #delete last value
pizza_toppings.pop(1) #delete value


print(person) #log statement
person.pop('eye_color')#delete value
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional if
        continue #for loop continue
    print('After 1st if statement')
    if topping == 'Olives': #conditional if
        break #for loop break

def print_hello_ten_times(): #function 
    for num in range(10): #for loop
        print('Hello') #log statement

print_hello_ten_times() 

def print_hello_x_times(x): #function 
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_times(4) #calling function

def print_hello_x_or_ten_times(x = 10):  #function
    for num in range(x):#for loop
        print('Hello') #log statement

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)