from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQGLViewer import QGLViewer
from OpenGL.GL import *

class Viewer(QGLViewer):
    def __init__(self, parent=None):
        QGLViewer.__init__(self, parent)

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-0.7, 0.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.7, 0.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 1.0, 0.0)
        glEnd()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_W:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        elif e.key() == Qt.Key_F:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        self.update()

def main():
    qapp = QApplication([])
    viewer = Viewer()
    viewer.show()
    qapp.exec_()

if __name__ == '__main__':
    main()
