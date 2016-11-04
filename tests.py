from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import splot_wars

window = 0


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(-1.5, 0.0, -6.0)
    if color == 1:
        glColor3f(1.0, 0.0, 0.0)
    elif color == 2:
        glColor3f(0.0, 0.0, 1.0)
    else:
        glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(x-0.1, y+0.1)
    glVertex2f(x+0.1, y+0.1)
    glVertex2f(x+0.1, y-0.1)
    glVertex2f(y-0.1, y-0.1)
    glEnd()
    glutSwapBuffers()


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Jeff Molofee's GL Code Tutorial ... NeHe '99")
    glutDisplayFunc(splot_wars.DrawGLScene)
    glutIdleFunc(splot_wars.DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    InitGL(640, 480)
    glutMainLoop()
