#name : PARTH DOBARIA
#github-link : https://github.com/ParthDobaria/PythonAssignment.git


# Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.
class Stack_struct:
   def __init__(self):
      self.items = []

   def check_empty(self):
      return self.items == []

   def add_elements(self, my_data):
      self.items.append(my_data)

   def delete_elements(self):
      return self.items.pop()

my_instance = Stack_struct()
while True:
   print('Push <value>')
   print('Pop')
   print('Quit')
   my_input = input('What operation would you like to perform ? ').split()

   my_op = my_input[0].strip().lower()
   if my_op == 'push':
      my_instance.add_elements(int(my_input[1]))
   elif my_op == 'pop':
        if my_instance.check_empty():
            print('The stack is empty')
        else:
            print('The deleted value is : ', my_instance.delete_elements())
   elif my_op == 'Quit':
      break