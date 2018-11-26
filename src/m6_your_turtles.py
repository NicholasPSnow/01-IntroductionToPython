"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Nicholas Snow.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window=rg.TurtleWindow()
window.tracer(20)

turtwig=rg.SimpleTurtle()
turtwig.pen=rg.Pen('yellow',3)
turtwig.speed=1
bulbasaur=rg.SimpleTurtle()
bulbasaur.pen=rg.Pen('purple',1)
bulbasaur.speed=200

for k in range(360):
    turtwig.forward(10)
    turtwig.backward(10)
    turtwig.left(10)
    turtwig.pen_up()
    turtwig.forward(k)
    turtwig.pen_down()

colors=['red','blue','green','orange']
print(len(colors))
for k in range(200):
   bulbasaur.draw_regular_polygon(6,30+k)
   bulbasaur.left(10)
   bulbasaur.pen = rg.Pen(colors[k%4],1)

window.close_on_mouse_click()