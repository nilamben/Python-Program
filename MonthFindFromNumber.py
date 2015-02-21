# if you want 3character in month
def main():
    # months is used as a lookup table
     months = "JanFebMarAprMayJunJulAugSepOctNovDec"
     n = eval(input("Enter a month number (1-12): "))
     # compute starting position of month n in months
     pos = (n-1) * 3

     # Grab the appropriate slice from months
     monthAbbrev = months[pos:pos+3]
     # print the result
     print ("The month abbreviation is", monthAbbrev + ".")
main()

#if you want full month name
def main1():

 # months is a list used as a lookup table
     months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

     n = eval(input("Enter a month number (1-12): "))
     print ("The month abbreviation is", months[n-1] + ".")
main1()

