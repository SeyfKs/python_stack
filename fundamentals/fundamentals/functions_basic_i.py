#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# output is 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# output number_of_days_in_a_week_silicon_or_triangle_sides is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# output is 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# output is 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# output is 5 and none (the function missing return)


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# output 3 ,5 and none (the function missing return)

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# output is char 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# output is 100 ,10 and 7 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #output is 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #output is 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#output is 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# output is 8

#11
b = 500
print(b) #output is 500
def foobar():
    b = 300
    print(b)
print(b) #output is 500
foobar() #output is 300
print(b) #output is 500


#12
b = 500
print(b) #output is 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #output is 500
foobar() #output is 300
print(b) #output is 500


#13
b = 500
print(b) #output is 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #output is 500
b=foobar() #output is 300
print(b) #output is 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# output is 1,3,2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# output is 1,3,5,10