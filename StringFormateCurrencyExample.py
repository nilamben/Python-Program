def main():
    print ("Change Counter\n")
    print ("Enter the count of each coin type.")
    quarters = eval(input("No of Quarters: "))
    dimes = eval(input("No of Dimes: "))
    nickels = eval(input("No of Nickels: "))
    pennies = eval(input("No of Pennies: "))
    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies
    print ("The total value of your change is ${0}.{1:0>2}"
    .format(total//100, total%100))
main()
