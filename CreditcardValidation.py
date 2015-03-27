# This Program will Vallidate Credit card 

#Step -1 :Double every second digit from right to left.
#If doubling of a digit results in a 2-digit number,make it single by adding two digit.

def sumOfEvenPosition(no):
    even=''
    no=no[:-1]
    for n in no[::-2]:
        double=int(n)*2
        
        if len(str(double))==2:
            add=0
            for ch in str(double):
                add=int(ch)+add
            even=str(add)+even
        else:
            even=str(double)+even

    sumEven = sumOfEvenSingleDigit(even)
    return sumEven
    
#Step -2 :Add all the single digit numbers from step 1            
def sumOfEvenSingleDigit(even):
    sum=0
    for no in str(even):
        sum=int(no)+sum           
    return sum

#Step -3 :Add all digits in the odd places from right to left in the card number
def sumOfOddPosition(no):
    sumOdd=0
    for n in no[::-2]:
       sumOdd= sumOdd+int(n) 
    return sumOdd

#Step -4 :Sum the results from step 2 and step 3
def getDigitSum(n1,n2):
     return n1+n2


#Step -5 :If the result from step 4 is divisible by 10, the card number is valid otherwise, it’s invalid.
def isValid(card1,n):    
    if n%10 !=0:        
         print ("This is an invalid "+card1+" Card number !")
    else:       
         print ("This is a good "+card1+" Card number !")
   

#CheckType() will check card number
def checkType(cno):   
    
    card=''
    if cno[0]=='4':
        card="Visa"
    elif cno[0]=='5':
        card="Master"
    elif cno[0]=='6':
        card="Discover"
    elif cno[0:2]=='37':
        card="American Express"
    
    return card


def main():
    cno=input("Enter your Credit Card number:")
    if ((len(cno)>=13 or len(cno) <=16) and cno.isdigit()== True):
        
        sumEven=sumOfEvenPosition(cno)
        sumOdd=sumOfOddPosition(cno)
        digitSum=getDigitSum(sumEven,sumOdd)
        cardType= checkType(cno)
        isValid(cardType,digitSum)
    else:
        print("This an invalid card number !")
       
      
main()
