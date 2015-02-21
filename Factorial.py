# calculating Factorial for given number

def main():
    
    n= (eval(input("Enter number for factorial value :")))
    fact =1
    
    for factor in(range(n,0,-1)):
        fact = fact * factor

    print("factorial value of ", n , "is :" , fact)

main()





