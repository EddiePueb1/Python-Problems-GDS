# VERY EASY: Write a function named min that takes two arguments and returns their minimum.

first_value = int(input('Value 1: '))
second_value = int(input('Value 2: '))

def min(val1, val2):

  if val1 < val2:
    return val1
  else:
    return val2

print(min(first_value, second_value))

# EASY: Create an array of students holding their last name, first name, and age with 3 students. 
# To validate, please log a greeting with the first name, last name and age of the 2nd student.
#  The output should look like "Hello, my name is John Doe and I'm 19 years old."

students = {
  'student1': ['Doe', 'John', 20],
  'student2': ['Capps','Leland', 21],
  'student3': ['Holland','Tom', 18 ]
}

def student_search():
  for i in students:
    if i == 'student2':
      student_info = students[i]
      return f"Hello, my name is {student_info[1]} {student_info[0]} and i'm {student_info[2]} years old"

print(student_search())


# MEDIUM: Create a program that accepts a number (1-12) as input and logs to the console that number 
# and its corresponding month. For example: if the user enters the number 3, then it should return the
# month “March.” Alert the user if they enter an invalid number (e.g. less than 1 or greater than 12).
 

def find_month():
  month_dict = {
    '1':'Janauary',
		'2':'February',
		'3':'March',
		'4':'April',
		'5':'May',
		'6':'June',
		'7':'July',
		'8':'August',
		'9':'September',
		'10':'October',
		'11':'November',
		'12':'December'
  }

  user_input = input("Enter a value you want to find: ")  
  if user_input not in month_dict.keys():
    return ('Invalid input')
  else:
    return month_dict[user_input]
print(find_month())


# HARD: Write a function that takes in an array of numbers and outputs the average of all the numbers.

num_list = [3,5,8,2,4]

def avg(aList):
  sum_list = sum(aList)
  return sum_list/len(aList)

print(avg(num_list))


# VERY HARD: Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return 
# “The input is not on this list”

nums = [4,5,6,7,0,1,2]

def find_index(List):
  target = int(input("Target value: "))
  for i in range(len(List)):
    if List[i] == target:
      return List.index(target)
    elif target not in List:
      return (f'{target} not in the list')
  

print(find_index(nums))

