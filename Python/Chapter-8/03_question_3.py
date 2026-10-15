'''Write a recursive function to calculate the sum of first n natural numbers'''

def sum(n):
    if(n==1):  #base condition is used so that the function will not work as infinetly recursive
     return 1
    return sum(n-1) + (n)

n = int(input("Enter the number: "))
print (f"The sum od first n natural number is: {sum(n)}")
