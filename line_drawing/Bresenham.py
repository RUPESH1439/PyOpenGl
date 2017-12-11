from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
     glClearColor(1.0, 1.0, 2.0, 1.0)
     gluOrtho2D(-5.0, 5.0, -5.0, 5.0)


def plot():
	x1,x2,y1,y2 = -2,100,-7,100
	dx,dy = abs(x2-x1),abs(y2-y1)
	p = 2*dy - dx
	twoDy,twoDyDx = 2*dy,2*(dy - dx)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,3.0,0.0)
	glPointSize(1.0)
	glBegin(GL_LINES)
	glVertex2f(-5.0, 0.0)
	glVertex2f(5.0, 0.0)
	glVertex2f(0.0, 5.0)
	glVertex2f(0.0, -5.0)
	glEnd()
	if (x2 < x1):
		x = x2
		y = y2
		xEnd = x1
	else:
		x = x1
		y = y1
		xEnd = x2
	while x < xEnd:
		x+= 1
		if (p < 0):
			p+= twoDy
		else:
			y+= 1
			p+= twoDyDx
		glBegin(GL_POINTS)
		glVertex2f(x/100,y/100)
		glEnd()
		glFlush()
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowPosition(0,0)
	glutInitWindowSize(1000,1000)
	glutCreateWindow("Bresenham Method")
	glutDisplayFunc(plot)
	init()
	glutMainLoop()

main()
		 

  