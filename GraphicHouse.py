from graphics import *

def drawHome():
    win = GraphWin("House - 82978 ",600,600,autoflush=False)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    
    # To draw Hosue Structure
    h1,h2 =Point(5,0),Point(1,0)
    h3,h4 =Point(1,3),Point(5,3)
    h5,h6 =Point(8,1),Point(8,4)
    base = Polygon(h1,h2,h3,h4,h1,h5,h6,h4)
    base.setFill("Pale Goldenrod")   
    base.draw(win)
    #To draw shultter of house and Chimany
    s1,s2 =Point (3,5),Point(6,5.8)
    l1,l2,l3,l4,l5,l6=Point(3.82,5.20),Point(5.77,3.25),Point(6.51,3.53),Point(4.54,5.40),Point(5.40,5.64),Point(7.31,3.80)
    c1,c2,c3,c4 =Point(2,4),Point(2,5.6),Point(2.7,5.9),Point(2.7,4.7)
    roof = Polygon(h4,h3,c1,c2,c3,c4,s1,h4,h6,s2,s1)
    roof.setFill("brown")    
    roof.draw(win)
    line1 = Line(l1,l2)
    line2 = Line(l3,l4)
    line3=Line(l5,l6)
    line1.draw(win),line2.draw(win),line3.draw(win)
    #To draw smoke from Chimany
    s1,s2,s3,s4 =Point(2.03,5.69),Point(2.07,5.8),Point(2.12,5.92),Point(2.10,6.04)    
    s5,s6,s7,s8=Point(2.03,6.12),Point(1.98,6.22),Point(1.98,6.34),Point(2.03,6.49)
    s9,s10,s11,s12,s13 =Point(2.28,5.9),Point(2.3,6),Point(2.27,6.17),Point(2.22,6.34),Point(2.28,6.51)
    s14,s15,s16 = Point(2.52,6.02),Point(2.53,6.29),Point(2.57,6.42)
    s1.draw(win),s2.draw(win),s3.draw(win),s4.draw(win)
    s5.draw(win),s6.draw(win),s7.draw(win),s8.draw(win)
    s9.draw(win),s10.draw(win),s11.draw(win),s12.draw(win),s13.draw(win),s14.draw(win),s15.draw(win),s16.draw(win)
    #To draw window and door
    w1,w2,w3,w4 =Point(6,2.5),Point(6,1.8),Point(6.9,2.2),Point(6.9,2.9)
    d1,d2,d3,d4 = Point(2.2,0),Point(2.2,1.9),Point(3.2,1.9),Point(3.2,0)
    door = Polygon(d1,d2,d3,d4)
    door.setFill("Khaki")
    door.draw(win)
    window = Polygon(w1,w2,w3,w4)
    window.setFill("Khaki")
    window.draw(win)
    #To draw sun and sun rays
    center = Point(8,8)
    sun = Circle(center,0.4)
    sun.setFill("yellow")
    sun.draw(win)
    a1,a2,a3,a4,a5,a6,a7,a8 =Point(8.01,8.39),Point(8.09,8.91),Point(8.16,8.38),Point(8.28,8.63),Point(8.28,8.29),Point(8.66,8.58),Point(8.36,8.19),Point(8.63,8.28)
    b1,b2,b3,b4,b5,b6,b7,b8 = Point(8.39,8.08),Point(8.83,8.04),Point(8.41,7.92),Point(8.68,7.87),Point(8.34,7.79),Point(8.69,7.52),Point(8.24,7.69),Point(8.36,7.49)
    e1,e2,e3,e4,e5,e6,e7,e8=Point(8.11,7.61),Point(8.23,7.16),Point(7.94,7.59),Point(7.94,7.26),Point(7.81,7.62),Point(7.57,7.26),Point(7.71,7.72),Point(7.49,7.57)
    f1,f2,f3,f4,f5,f6,f7,f8=Point(7.62,7.84),Point(7.14,7.67),Point(7.59,7.94),Point(7.24,7.97),Point(7.61,8.13),Point(7.06,8.28),Point(7.69,8.24),Point(7.41,8.39)
    g1,g2,g3,g4=Point(7.79,8.34),Point(7.49,8.77),Point(7.91,8.41),Point(7.84,8.71)
    rays =Polygon(a1,a2,a1,a3,a4,a3,a5,a6,a5,a7,a8,a7,b1,b2,b1,b3,b4,b3,b5,b6,b5,b7,b8,b7,e1,e2,e1,e3,e4,e3,e5,e6,e5,e7,e8,e7,f1,f2,f1,f3,f4,f3,f5,f6,f5,f7,f8,f7,g1,g2,g1,g3,g4,g3)
    sun.setOutline("Orange")
    rays.setOutline("Orange")
    rays.draw(win)

    #To draw man
    center1 = Point(8.86,2.93)
    man = Circle(center1,0.4)
    man.setFill("Moccasin")
    man.draw(win)
    lineman = Line(Point(8.86,2.55),Point(8.86,1.2))
    lineman1 =Line(Point(8.86,1.2),Point(8.31,0.43))
    lineman2 =Line(Point(8.86,1.2),Point(9.38,0.48))
    lineman3 =Line(Point(8.33,2.22),Point(9.36,2.22))
    lineman4 =Line(Point(8.33,2.22),Point(8.24,2.07))
    lineman5 =Line(Point(9.36,2.22),Point(9.49,2.10))    
    lineman.draw(win),lineman1.draw(win),lineman2.draw(win),lineman3.draw(win),lineman4.draw(win),lineman5.draw(win)
          
    # Wait for another click to exit
    
    win.getMouse()
    win.close()

drawHome()
