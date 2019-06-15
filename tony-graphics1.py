from ezgraphics import GraphicsWindow
w= GraphicsWindow(640,480)
c= w.canvas()
c.setFill(0,255,255)
c.drawRect(310,260,100,100)
c.setFill(0,155,255)
c.drawRect(150,100,30,30)
c.setFill(0,55,155)
c.drawRect(180,130,50,50)
c.setFill(0,255,155)
c.drawRect(230,180,80,80)
c.setFill(0,155,155)
w.wait()

