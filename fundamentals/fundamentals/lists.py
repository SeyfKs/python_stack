# play around with the drawers!
drawers = ['documents', 'envelopes', 'pens']
# Print the second value from the list (envelopes)
# Change "pens" to "useless manuals"
# Change the first value to whatever is the second value
# What should the list look like now?
# Print the list! Does it match your prediction?

words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']
    
# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']


