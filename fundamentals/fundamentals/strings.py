#Concatenating Strings and Variables with the print function
name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

# Type Casting or Explicit Type Conversion

print("Hello " + str(42))		# output: Hello 42

total = 35
user_val = "26"
total = total + int(user_val)		# total will be 61

# String Interpolation
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")


first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

# Practice Challenge: Correct the errors!
first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5
greeting = "Hello my name is "+ first_name + " " + last_name
print(greeting) 
# Desired output: Hello my name is Alana Da Silva
print(f"I am {age} years old") 
# Desired output: I am 36 years old
print("I work as a {}.".format(profession))
# Desired output: I work as a Software Developer.
exp_string = "I have worked in the field for {} years."
print(exp_string.format(years_experience ))
# Desired output: I have worked in the field for 5 years.
print(f"I started in the field when I was {age - years_experience} years old.")
# Desired output: I started in the field when I was 31 years old.


hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

