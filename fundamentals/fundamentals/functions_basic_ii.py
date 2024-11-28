# Countdown
mylist=[]
def Countdown(a):
    for i in range(a,-1,-1):
        mylist.append(i)
    return print(mylist)
Countdown(10)
# Print and Return
def print_and_return(a,b):
    print(a)
    return b
print(print_and_return(1,2))
# First Plus Length
def first_plus_length(mylist):
    return mylist[0]+len(mylist)
b=first_plus_length([1,2,3,4,5])
print(b)

# Values Greater than Second
mylist2=[]
def values_greater_than_second(mylist):
    if len(mylist)>2:
        for i in range(0,len(mylist)) :
            if mylist[i]>mylist[1]:
                mylist2.append(mylist[i])
        return mylist2,len(mylist2)
    else: 
        return False

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5]))
# This Length, That Value 
def length_and_value(a,b):
    lenval=[]
    for j in range (a):
        lenval.append(b)
    print(lenval)

length_and_value(4, 7)
length_and_value(6, 2)