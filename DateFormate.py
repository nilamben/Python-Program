# Dater converter 
def main():
    dateInput = input("Please enter ther date in this formate: mm/dd/yyyy")
    month,date,year = dateInput.split("/")
    months = ["January","February","March","April","May","June","July","August","September","Octomber","November","December"]
    monthStr = months[int(month)-1]

    output = monthStr+","+date+","+year
    print("Converted Date is:" ,output)

main()
    
