

def exercise7():
    import sys
    # Get all the numbers provide via command line except the program name. 
    #Note the program name argv[0]
    
    # We are using list slicing and getting all the values provided in command line starting from index 1
    # as index 0 has the program name itself
    cmd_args = sys.argv[1:]
    print ( cmd_args)
    
    sum=0
    # Loop through all the numbers in cmd_args and sum it only if it is an even number
    for num in cmd_args:
        x = int(num)
        # Check if number is even
        if x % 2 == 0:   # We are using the arithmetic operator % and relational operator ==  here
            sum+=x       # We are using the arithmetic operator += here
        
    print ( "The sum of the even numbers provided via command line is -" , sum)
    

def main():
  
    import sys
  
    total_args = len(sys.argv)
    print ( "the number of command line argumnets provided = " , total_args)
    print ( "the arguments provided are {0} , {1} , {2}" , sys.argv[0], sys.argv[1], sys.argv[2])
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    
    print ( "The sum of the number {0} and {1} is {2}".format(x, y , x+y))
    

def execise8():
    
    for i in range(1,11):
        print ( "** Multiplication table -" , i , "**")
        for j in range (1,11):
            print ( i ,   " X " , j , "=" , i*j)      
    

    a = int(input("Enter a positive number :"))
    assert a>0 , "You did not enter a positive number"
    print ( "Number u have entered - " , a )

if __name__ == '__main__':
    main()
    # exercise7
    # pass on few integers from command line and find the sum of the ven numbers passed
#     exercise7()
    
    # execise8
    # Write a program to display multiplication table till 10.
    execise8()
    

    # execise9
    # Write a program display the fibonacci number series
        
    
    
