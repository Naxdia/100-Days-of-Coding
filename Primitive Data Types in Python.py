#Type Errors

#The following line will cause a TypeError because it tries to concatenate a string with an integer.
###print("Number of letters in your name: " + len(input("What is your name? ")))

#To fix the error, we can convert the integer to a string using the str() function.
###print("Number of letters in your name: " + str(len(input("What is your name? "))))

#If we wanted to use the data given by the user, we could store it in a variable.
user_name = input("What is your name? ") #str
length_of_name = len(user_name) #int
print("Number of letters in your name: " + str(length_of_name))