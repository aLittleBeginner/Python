# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 17:27:00 2021

@author: 10304
"""

#Chapter 2, excercise 2.1
#编写一个程序，检查三个变量x,y,z，输出其中最大的奇数。如果其中没有奇数，就输出一个消息进行说明。
# =============================================================================
# def compare(a, b):
#     if a >=b:
#         return a
#     else:
#         return b
# 
# #first version
# x, y, z = int(input("Enter a number x: ")), int(input("Enter a number y: ")), int(input("Enter a number z: "))
# if x%2 == 0 and y%2 == 0 and z%2 == 0:
#     print("There is no odd integer!")
# elif x%2 == 1:
#     if y%2 == 1 and z%2 == 1:
#         comp_num = compare(y, z)
#         result = compare(comp_num, x)
#     elif y%2 == 1 and z%2 != 1:
#         result = compare(x, y)
#     elif y%2 != 1 and z%2 == 1:
#         result = compare(x, z)
#     else:
#         result = x
#     print("The largest odd integer is:", result)
#     
# else:
#     if y%2 == 1 and z%2 == 1:
#         result = compare(y, z)
#     elif y%2 == 1 and z%2 != 1:
#         result = y
#     else:
#         result = z
#     print("The largest odd integer is:", result)
# =============================================================================


#将以下代码中的注释替换为while循环语句
# =============================================================================
# numXs = int(input('How many times should I print the letter X? '))
# toPrint = ''
# #concatenate X to toPrint numXs times
# x = 0
# while (x < numXs):
#     toPrint += 'X'
#     x += 1 #while loop counter
# print(toPrint)
# =============================================================================


#编写一个程序，要求用户输入10个整数，然后输出其中最大的奇数。如果用户没有输入奇数，则输出一个消息进行说明。
def max_number(arraylist):
    max_value = arraylist[0]
    for i in range(1, len(arraylist)):
        if max_value < arraylist[i]:
            max_value = arraylist[i]
    return max_value

numbers = []
x = input("Enter 10 integers, separating with a blankspace:").split()
for i in x:
    if int(i)%2 == 1:
        numbers.append(int(i))
if numbers == []:
    print("There is no odd interger in your input!")
else:
    max_number(numbers)
print("The largest odd integer number is " + str(max_number((numbers))))






