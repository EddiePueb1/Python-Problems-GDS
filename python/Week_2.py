
first_value = int(input('Value 1: '))
second_value = int(input('Value 2: '))

def min(val1, val2):

  if val1 < val2:
    return val1
  else:
    return val2

print(min(first_value, second_value))
'''
'''
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

'''
# medium
 
'''
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
'''

# Hard
'''
num_list = [3,5,8,2,4]

def avg(aList):
  sum_list = sum(aList)
  return sum_list/len(aList)

print(avg(num_list))


# Very Hard

nums = [4,5,6,7,0,1,2]

def find_index(List):
  target = int(input("Target value: "))
  for i in range(len(List)):
    if List[i] == target:
      return List.index(target)
    elif target not in List:
      return (f'{target} not in the list')
  

print(find_index(nums))

