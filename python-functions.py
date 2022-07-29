
## Challenge 1
print('==================== Challenge 1 ====================')
def sum_to(num):
  sum = 0
  for i in range(0,num+1, 1):
    sum += i

  return print(sum)

sum_to(6)
sum_to(10)

## Challenge 2
print('==================== Challenge 2 ====================')

def largest(array):
  largest = 0
  for element in array:
    if(element > largest):
      largest = element
    
  return print(largest)

largest([1, 2, 3, 4, 0]) # returns 4
largest([10, 4, 2, 231, 91, 54]) # returns 231

## Challenge 3
print('==================== Challenge 3 ====================')

def occurrences(string1, string2):
  return print(string1.count(string2))

occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0

## Challenge 4
print('==================== Challenge 4 ====================')

def product(*args):
  product = 1
  for operand in args:
    product *= operand
  
  return print(product)

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0