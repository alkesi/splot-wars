import numpy as np; import ctypes
import pyglet; import pyglet.gl as gl

def drawArray(someArray):

    vertPoints = someArray[:,:2].flatten().astype(ctypes.c_float)
    vertices_gl = vertPoints.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    vertColors = someArray[:,2:].flatten().astype(ctypes.c_float)
    colors_gl = vertColors.ctypes.data_as(ctypes.POINTER(ctypes.c_float))

    gl.glVertexPointer(2, gl.GL_FLOAT, 0, vertices_gl)
    gl.glColorPointer(3,  gl.GL_FLOAT, 0, colors_gl)
    gl.glDrawArrays(gl.GL_POINTS, 0, len(vertPoints) // 2)

window = pyglet.window.Window(400,400)

@window.event
def on_draw(points):
    gl.glPointSize(1.0)
    gl.glEnable(gl.GL_POINT_SMOOTH)
    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
    gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
    gl.glEnableClientState(gl.GL_COLOR_ARRAY)

    drawArray(points)


pyglet.app.run()