from quadrilatere import Quadrilatere


class Rectangle(Quadrilatere):
    def __init__(self, vertex, width, height):
        self.width = width
        self.height = height
        x, y = vertex
        super().__init__(
            vertex,
            (x + width, y),
            (x + width, y + height),
            (x, y + height)
        )

    def __repr__(self):
        return f"Rectangle: [{self.s1}, {self.width}x{self.height}]"


if __name__ == "__main__":
    r = Rectangle(
        (4, 4),
        5,
        3
    )
    print("q:", r)
    print("Périmètre de q:", r.perimetre())
    print("Aire de q:", r.aire())
    print("~~~~~~~~~~~~~~~")
    print(type(r))
