for item in 'python':
    print(item)
#here python is s string.

for item in ['sowji','jonnala','siva']:
    print(item)
#here it is a list

for item in (1,2,3,4,5):
    print(item)
#here it is a tuple

for item in range(15):
    print(item)
#it is a range function.used for more numbers.10 not included

for item in range(5,10):
    print(item)

for item in range(5,10,2):
    print(item)
#here first print 5 next 7 next 9

prices=[10,20,30,40]
total=0
for price in prices:
    total=total+price
#total+=price
print(f"total:{total}")



#nested loops:

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

 #form a f:
numbers =[5,2,5,2,2]
for x_count in numbers:
    print('x'* x_count)       

#LISTS:
names=['so','for','is','no']
names[0]='soon'
print(names)
print(names[0])
print(names[3])
print(names[-1])
print(names[-2])

#largest number
numbers=[5,9,8,6,2,10]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)


#2d lists

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1]=20
print(matrix[0][1])

numbers=[5,2,1,7,4]
numbers.append(25)
print(numbers)

numbers=[5,2,1,7,4]
numbers.insert(0,8)
print(numbers)

numbers=[1,2,3,4,5,6]
numbers.remove(3)
print(numbers)

numbers=[1,2,3,4,5,6]
numbers.clear()
print(numbers)

numbers=[1,2,3,4,5,6]
numbers.pop()
print(numbers)

numbers=[1,2,3,4,5,6]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#TUPLES:
#TUPLES ARE IMMUTABLE.WE CAN NOT CHANGE
numbers=(1,2,3,5)
print(numbers[0])
print(numbers[1])
print(numbers[2])