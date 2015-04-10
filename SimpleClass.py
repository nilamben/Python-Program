class A:

    def getX(self):
        return self.x
    def setX(self,x):
        self.x = x
        
def main():
    a = A() # create object of Class A
    a.setX(3)
    print(a.getX())

main()
