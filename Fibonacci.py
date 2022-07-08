n = int(input ("How many terms you wants to print? "))  
    
n1 = 0  
n2 = 1  
count = 0  
 
if n <= 0:  
    print ("Given number is not valid")  

elif n == 1:  
    print ("The Fibonacci sequence of the numbers up to", n, ": ")  
    print(n1)  

else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n:  
        print(n1)  
        m = n1 + n2  
        n1 = n2  
        n2 = m 
        count = count+1  
