'''
Created on 26-Jan-2019

@author: Pritam
'''

def main():
    """ We have a group of python beginners and we have been give the below tasks to complete 
    
    """
    # Execrise 1
    # Write a program to display "Hello python"
    print ("Hello python")
    
    # Execise 2
    # DataTypes in Python
    # Write a program to add 2 numbers
    x=10
    y=20
    print ("The sum of x & y is - ", x + y)
    
    #Exercise 3
    # *******************  Operators ******************************************************************
    # Find the area of a circle given the radius ( use * , ** operator )
    
    # Lets import math package to use the pi variable
    import math
    radius = 5.5
    area= math.pi * radius ** 2
    print ("Area of the Circle =" , area)
    
    # Exercise 4
    # Test the operators available in Python and see the result to verify how they work
    
    # Arithmetic operator
    x=40 
    y =3
    print ( "x + y =" , x + y)
    print ( "x - y =" , x - y)
    print ( "x * y =" , x * y)
    print ( "x ** y =" , x ** y)
    print ( "x / y =" , x / y)
    print ( "x // y =" , x // y)
    print ( "x % y =" , x % y)
    
    # Unary minus
    print ( "Negation of x =" , -x )
    
    #Relational Operators
    
    print ( x and y)  # Displays 3
    print ( x or y)  # Displays 40
    if ( x >y ): print ("x is greater than y")
    
    # similarly you can test more such operators. We will use it in our later exercises
    
    
    # *******************  INPUT / OUTPUT ******************************************************************
    
# passing a string to the print statement

# Displays "Hello" 
    print ("Hello Python" )

# escape charaters can be used between strings 
    print ("Hello \n Python" )   # Displays Hello and then Python is displayed in the next line


# passing variables to print statement
    x=20
    y =13
    print ( x , y ) # Displays the values fo x and y 

# by default space is the default separator . When can override the separator as below

    print ( x , y , sep='++++++++++++') # displays value of x and y separated by the separator provided.


# Combine variable list and string in Python
    print ( "the value of x is - " , x )

# we can use the C style printing as well
    print ( 'x = %d y =%d'  % ( x , y ))


# We can use the formatted strings as well which is quite useful. See the example below
    print ( "The value of x = {0} and the value of y = {1}".format(x, y))
    
# use input to get an input from the keyboard
    str1=input("Enter your name")
    print ("Hi " , str1 , ". How are you today?")
    
    # exercise 5 
    # Write a program to take 2 numbers from the user and display the sum
    x = int(input("enter a number"))
    y = int(input("enter another number"))
    print ( "The sum of the number {0} and {1} is {2}".format(x, y , x+y))
    
    # exercise 6
    # Write a program to get 3 number separated by comma and display their sum
    x , y , z = [int (x) for x in input("enter 3 numbers separated by comma").split(',')]
    print ( "The sum of the number {0} , {1} , {2} is {3}".format(x, y ,z, x+y+z))
    
    

if __name__ == '__main__':
    main()