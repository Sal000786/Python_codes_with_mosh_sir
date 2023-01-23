# length function
course='python for beiggeners'
print(len(course))

# upper case function
print(course.upper()) #this will convert the string to upper case just for now. It wont change the original string
print(course)

# lower case function 

print(course.lower()) #this will convert the string to lower case just for now. It wont change the original string

# find method
print(course.find('o')) 

# Note:- Find method in a string returns the index of the  first character passed into the function if the passed input string isn't found in original string then it will return the index as -1

#replace function

print(course.replace('python','programming in c'))
#note the replace function in python replaces a character or a word if the character matches with the string then it replaces otherwise returns the priginal string

# in operator 

print("python" in course)
# it returns true or false if the entered string is present then returns true otherwise false

