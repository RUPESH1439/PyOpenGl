from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys
def init():
     glClearColor(1.0, 1.0, 1.0, 1.0)
     gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
def plotfunc():
  x1,x2,y1,y2 = -2,100,-7,100
  dx,dy = x2-x1,y2-y1
  x,y = x1,y1
  if (abs(dx) > abs(dy)):
    steps = abs(dx)
  else:
    steps = abs(dy)
  xInc = dx /(steps)
  yInc = dy /(steps)
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(0.0, 0.0, 0.0)
  glPointSize(1.0)
  glBegin(GL_LINES)
  glVertex2f(-5.0, 0.0)
  glVertex2f(5.0, 0.0)
  glVertex2f(0.0, 5.0)
  glVertex2f(0.0, -5.0)
  glEnd()
  
  for k in range(0,int(steps),1):
    x+= xInc
    y+= yInc

    glBegin(GL_POINTS)
    glVertex2f((x/100), (y/100))
    glEnd()
    glFlush()
           
    
def main():
     glutInit(sys.argv)
     glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
     glutInitWindowPosition(0,0)
     glutInitWindowSize(1000,1000)
     glutCreateWindow("DDA METHOD")
     glutDisplayFunc(plotfunc)
     init()
     glutMainLoop()
main()