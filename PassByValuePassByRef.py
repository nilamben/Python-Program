

def change(array,x):
    #int[] b = new int[10]
    b =array
    b[0] = 0
    b[1] = 1
    x=11

def main():
    x=10
    a = [1,2,3,4,5,6,7,8,9,10]
    change(a,x)
    print (a) # Pass By Reference
    print(x)    #pass by Value
main()
