'''
Grid Printer Exercise
Printing a Grid (adapted from Downey, “Think Python”, ex. 3.5)

Goal:
Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
hints
A couple features to get you started...

use print("+", end = " ") to print continuous line without carriage return

A print function with no arguments ends the current line and goes to the next line:

Simple string manipulation:
You can put two strings together with the plus operator:

"this" + "that" ===>  'thisthat'
Particularly useful if they have been assigned names:
plus = '+'
minus = '-'

You can also multiply strings:
'+' * 10 ===> '++++++++++'
'''
def kola():
    for j in range(2):
        if j<1:
            print("+",end=" ")
            for i in range(8):
                print("-",end=" ")
            print("+", end=" ")
            for i in range(8):
                print("-", end=" ")
            print("+")
        for i in range(6):
            print("|",end=" ")
            for i in range(8):
                print(" ",end=" ")
            print("|",end=" ")
            for i in range(8):
                print(" ",end=" ")
            print("|")
        print("+",end=" ")
        for i in range(8):
            print("-",end=" ")
        print("+",end=" ")
        for i in range(8):
            print("-",end=" ")
        print("+")
kola()
'''
Part 2
Making it more general

Make it a function
One of the points of writing functions is so you can write code that does similar things, but customized to input parameters. So what if we want to be able to print that grid at an arbitrary size?

Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.

For example,

print_grid(3) would print a small grid:

+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
print_grid(15) prints a larger grid:

+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
'''
def cela(n):
    def beggining():
        x = n
        if (x) % 2 != 0:
            x += 1
        if (x > 6):
            print("+", end=" ")
            for i in range((x - 3) // 2):
                print("-", end=" ")
            print("+", end=" ")
            for i in range((x - 3) // 2):
                print("-", end=" ")
            print("+")
        else:
            print("+", end=" ")
            for i in range(1):
                print("-", end=" ")
            print("+", end=" ")
            for i in range(1):
                print("-", end=" ")
            print("+")


    def middle():
        x = n
        if (x) % 2 != 0:
            x += 1
        if x > 6:
            for i in range((x - 3) // 2 - 1):
                print("|", end=" ")
                for i in range((x - 3) // 2):
                    print(" ", end=" ")
                print("|", end=" ")
                for i in range((x - 3) // 2):
                    print(" ", end=" ")
                print("|")
        else:
            for i in range(1):
                print("|", end=" ")
                for i in range((1)):
                    print(" ", end=" ")
                print("|", end=" ")
                for i in range((1)):
                    print(" ", end=" ")
                print("|")


    def end():
        x = n
        if (x) % 2 != 0:
            x += 1

        if (x > 6):
            print("+", end=" ")
            for i in range((x - 3) // 2):
                print("-", end=" ")
            print("+", end=" ")
            for i in range((x - 3) // 2):
                print("-", end=" ")
            print("+")
        else:
            print("+", end=" ")
            for i in range(1):
                print("-", end=" ")
            print("+", end=" ")
            for i in range(1):
                print("-", end=" ")
            print("+")
            #I defined the functions inside the main function. I guess I could have used a class but I don't think we were supposed to
            #I did this to handle the scope issue of n being defined.
    for j in range(2):
            if j<1:
                beggining()
            middle()
            end()

cela(3)

'''

Part 3:
Even more general...

A function with two parameters
Write a function that draws a similar grid with a specified number of rows and columns, and each cell a given size.

for example, print_grid2(3,4) results in:

+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
What to do about rounding? – you decide.

Another example: print_grid2(5,3):

+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
'''

def cela1(n,m):
    def beggining():
        zborce=0
        x = n
        if (x) % 2 != 0:
            x += 1
        for i in range(n):
                zborce+=1
                if (x > 6):
                        if(i==0):
                            print("+", end=" ")
                        for i in range(m):
                            print("-", end=" ")
                        if (zborce <= n-1):
                            print("+", end=" ")
                        else:
                            print("+")

                else:
                    if(i==0):
                        print("+", end=" ")
                    for i in range(m):
                        print("-", end=" ")
                    if (zborce<=n-1):
                        print("+", end=" ")
                    else:
                        print("+")


    def middle():
        x = n
        if (x) % 2 != 0:
            x += 1

        for i in range(m):
            print("|", end=" ")
            for i in range(n):
                for i in range(m):
                    print(" ", end=" ")
                print("|", end=" ")
            print()




    def end():
        x = n
        zborce=0
        if (x) % 2 != 0:
                x += 1
        for i in range(n):
                zborce+=1
                if (x > 6):
                        if(i==0):
                            print("+", end=" ")
                        for i in range(m):
                            print("-", end=" ")
                        if (zborce <= n-1):
                            print("+", end=" ")
                        else:
                            print("+")

                else:
                    if(i==0):
                        print("+", end=" ")
                    for i in range(m):
                        print("-", end=" ")
                    if (zborce<=n-1):
                        print("+", end=" ")
                    else:
                        print("+")

            #I defined the functions inside the main function. I guess I could have used a class but I don't think we were supposed to
            #I did this to handle the scope issue of n being defined.
    for j in range(n):
            if j<1:
                beggining()
            middle()
            end()

cela1(6,5)