from math import sqrt


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    @staticmethod
    def vector(p1, p2):
        return Vector(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)

    def get2D(self, camera) -> (int, int):
        # A(x - x0) + B(y - y0) + C(z - z0) = 0 =>
        # => Ax + By + Cz + D = 0
        D = (camera.x * self.x + camera.y * self.y + camera.z * self.z)

        t = D / (camera.x ** 2 + camera.y ** 2 + camera.z ** 2)

        c_x = camera.x * t
        c_y = camera.y * t
        c_z = camera.z * t

        x = sqrt((c_x - self.x) ** 2 + (c_z - self.z) ** 2)
        y = sqrt((c_y - self.y) ** 2 + (c_z - self.z) ** 2)

        """if self.x > c_x:
            x = 300 + x
        else:
            x = 300 - x

        if self.y > c_y:
            y = 300 + y
        else:
            y = 300 - y"""

        return x, y


class Vector:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Vector(x={self.x}, y={self.y}, z={self.z})'

    def add(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __add__(self, vec):
        return self.add(vec)

    def mul(self, k: int):
        return Vector(self.x * k, self.y * k, self.z * k)

    def __mul__(self, k: int):
        return self.mul(k)

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)


if __name__ == '__main__':
    pass
