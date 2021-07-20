
# VERY EASY: Create two variables and assign a number to each. Print the difference between the numbers. 
# Example output: “The difference between 6 and 2 is 4”

num1 = 4
num2 = 5

def num_difference():
  return num1 - num2

print(f'The difference between {num1} and {num2} is {num_difference()}')


# EASY: Create two variables and assign a person’s name to each. Print a statement that says which name 
# is shorter or longer, and by how many characters.

person1 = input("Name 1: ")
person2 = input("Name 2: ")

def name_length():
  p1 = len(person1)
  p2 = len(person2)

  if p1 < p2:
    return f'The name {person1} is shorter than {person2} by {abs(p1-p2)} letters'
  elif p1 > p2:
    return f'The name {person1} is longer than {person2} by {abs(p1-p2)} letters'
  else:
    return 'Both names are the same length'
  
print(name_length())


# MEDIUM: Write a program to tell if someone is shouting (typing in all caps), whispering (typing in all lowercase),
#  or neither. Use prompt to get user input, and then print whether the user was shouting, whispering, or talking normally.


user_string = input("Type something: ")

def text_voice():
  user_check = user_string.isupper()

  if user_check == True:
    return f"User is screaming {user_string}"
  elif user_check == False:
    if user_string.islower() == True:
      return f"User is whispering {user_string}"    
    else:
      return f"User said '{user_string}' and is talking normally"
  
print(text_voice())

#  Create a simple calculator that prompts the user for a number, an operator (either +, -, * or /) and another number,
#  and then uses the functions created in the hard challenge to output the value in sentence form. Example output: "3 + 4 = 7"



def add(x,y):
  return x + y
def substract(x,y):
  return x - y
def multiply(x,y):
  return x * y
def divide(x,y):
  return x / y 


num1 = float(input("First number: "))
operation = input("Operation: ")
num2 = float(input("Second number: "))

if operation == "+":
  print(f'{num1} + {num2} = {add(num1, num2)}')
elif operation == "-":
  print(f'{num1} - {num2} = {substract(num1, num2)}')
elif operation == "*":
  print(f'{num1} * {num2} = {multiply(num1, num2)}')
elif operation == "/":
  print(f'{num1} / {num2} = {divide(num1, num2)}')
else:
  print("Cannot compute")




 