# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!
def full_name(first_name,last_name):
    return first_name+" "+last_name
name1 = full_name("Eddie", "Aikau")
print(name1) # should print Eddie Aikau
# Challenge 2: 
#   Call the function again using your own name and print the results!
name2 = full_name("Seifeddine", "Ksontini")
print(name2)
mylist=[]
def multiply(num_list, num):
    for x in num_list:
        x *= num
        mylist.append(x)
    return mylist
a = [2,4,10,16]
b = multiply(a,5)
print(b)

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)




