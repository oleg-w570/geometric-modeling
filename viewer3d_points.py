import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQGLViewer import *
from OpenGL.GL import *


class Viewer(QGLViewer):
    def __init__(self, parent=None):
        QGLViewer.__init__(self, parent)
        self.vertices: np.ndarray = np.empty((0, 3))

    def draw(self):
        glPointSize(2.5)
        glBegin(GL_POINTS)
        for vertex in self.vertices:
            glVertex3f(*vertex)
        glEnd()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_C:
            self.vertices = np.empty((0, 3))
            print("Список вершин очищен.")
            self.update()
        elif e.key() == Qt.Key_G:
            self.generate_grid()
            self.update()
        elif e.key() == Qt.Key_R:
            self.generate_random_vertices_in_cube()
            self.update()
        elif e.key() == Qt.Key_S:
            self.generate_random_vertices_in_sphere()
            self.update()
        elif e.key() == Qt.Key_O:
            self.generate_vertices_on_sphere_shell()
            self.update()
        else:
            super().keyPressEvent(e)

    def generate_grid(self):
        num_vertices = 10  # in one dimension
        grid_start = -1.0
        grid_end = 1.0

        self.vertices = np.array(
            [
                (x, y, z)
                for x in np.linspace(grid_start, grid_end, num_vertices)
                for y in np.linspace(grid_start, grid_end, num_vertices)
                for z in np.linspace(grid_start, grid_end, num_vertices)
            ]
        )
        print("Сгенерирована трёхмерная сетка вершин.")

    def generate_random_vertices_in_cube(self):
        num_vertices = 1000
        grid_start = -1.0
        grid_end = 1.0

        self.vertices = np.random.uniform(grid_start, grid_end, (num_vertices, 3))

        print("Сгенерированы случайные вершины внутри куба.")

    def generate_random_vertices_in_sphere(self):
        num_vertices = 1000

        theta = np.random.uniform(0, 2 * np.pi, num_vertices)
        phi = np.random.uniform(0, np.pi, num_vertices)
        r = np.cbrt(np.random.uniform(0, 1, num_vertices))

        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)

        self.vertices = np.column_stack((x, y, z))

        print("Сгенерированы случайные вершины внутри сферы.")

    def generate_vertices_on_sphere_shell(self):
        num_vertices = 1000
        deviation = 0.1

        theta = np.random.uniform(0, 2 * np.pi, num_vertices)
        phi = np.random.uniform(0, np.pi, num_vertices)
        r = 1 + np.random.uniform(-deviation, deviation, num_vertices)

        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)

        self.vertices = np.column_stack((x, y, z))

        print("Сгенерированы вершины вдоль оболочки сферы с отклонением.")


def main():
    qapp = QApplication([])
    viewer = Viewer()
    viewer.setWindowTitle("3D Визуализация вершин")
    viewer.show()
    qapp.exec_()


if __name__ == "__main__":
    main()
