# This program will get point with mouse and draw Triangle

from graphics import *

def getPoint():
    win = GraphWin()
    
    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # This will print pixel on shell
    print(p1.getX(), ":",p1.getY() )
    print(p2.getX(),":",p2.getY())
    print(p3.getX(),":",p3.getY())
    
    #Draw traingle with given point and fill color yello
    traingle = Polygon(p1,p2,p3)
    traingle.setFill("yellow")
    traingle.draw(win)
    
    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

getPoint()
