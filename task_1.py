# -*- coding: utf-8 -*-
"""Task_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J9RN3cCQkPEkmUZiR6u3sEQ8qm4V1MHX
"""

'''Task 1
- CELIA HERNANDEZ CRUZ

1.
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
'''

r = 5

num = r

for i in range(r, 0, -1):

    for j in range(0, i):

        print(num, end= ' ')

    print("\r")

''' 2.
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1'''

r = 5

for i in range(r, 0, -1):

    for j in range(0, i + 1):

        print(j, end= ' ')

    print("\r")

''' 3.   1
         3 3
         5 5 5
         7 7 7 7
         9 9 9 9 9 '''
r = 5

i = 1

while i <= r:

    j = 1

    while j <= i:

        print((i * 2 - 1), end= ' ')
        j = j + 1

    i = i + 1

    print()

'''4.
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1'''

r = 6

for row in range(1, r):

    for column in range(row, 0, -1):

        print(column, end= ' ')

    print("")

'''5.
1
3 2
6 5 4
10 9 8 7
'''
start = 1

stop = 2

currentNumber = stop

for r in range(2, 6):

    for c in range(start, stop):

        currentNumber -= 1

        print(currentNumber, end= ' ')

    print("")

    start = stop

    stop += r

    currentNumber = stop

'''6.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1'''

def print_row_triangule (size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set r
r = 7
print_row_triangule(r)

'''7.
1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5
'''
r = 5
for i in range(1, r + 1):
    for j in range(1, r + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

'''8.
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36
7 14 21 28 35 42 49
8 16 24 32 40 48 56 64'''

r = 8

for i in range(1, r + 1):
    for j in range(1, i + 1):
        
        square = i * j
        print(i * j, end=' ')
    print()

'''9.
 * * * * * *
 * * * * *
 * * * *
 * * *
 * *
 * '''

r = 5
c = 2 * r - 2
for i in range(r, -1, -1):
    for j in range(c, 0, -1):
        print(end="")
    c = c + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print(" ")

'''10.
 *
 * *
 * * *
 * * * *
 * * * * *
 * * * * * *'''

r = 6
m = (2 * r) - 2
for i in range(0, r):
    for j in range(0, m):
        print(end="")
        
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end='')
    print(" ")

'''11.
11.
*
* *
* * *
* * * *
* * * * *
* * * * * *

* * * * * *
* * * * *
* * * *
* * *
* *
* '''

r = 6
for i in range(0, r):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(r + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

'''12.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

a = 5
for i in range(0, a):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(a, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

'''13.
            *
          * *
        * * *
      * * * *
    * * * * *
      * * * *
        * * *
          * *
            * 
'''
r = 5
a = 1
while a <= r:
    j = a
    while j < r:
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= a:
        print('*', end=' ')
        k += 1
    print()
    a += 1

a = r
while a >= 1:
    j = a
    while j <= r:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < a:
        print('*', end=' ')
        k += 1
    print('')
    a -= 1

'''14.
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *    
 '''
r = 5
a = 0
while a <= r - 1:
    j = 0
    while j < a:
        print('', end=' ')
        j += 1
    k = a
    while k <= r - 1:
        print('*', end=' ')
        k += 1
    print()
    a += 1

a = r - 1
while a >= 0:
    j = 0
    while j < a:
        print('', end=' ')
        j += 1
    k = a
    while k <= r - 1:
        print('*', end=' ')
        k += 1
    print('')
    a -= 1

'''
15.
****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*
'''

r = 14
print("*" * r, end="\n")
a = (r // 2) - 1
j = 2
while a != 0:
    while j <= (r - 2):
        print("*" * a, end="")
        print("_" * j, end="")
        print("*" * a, end="\n")
        a = a - 1
        j = j + 2

