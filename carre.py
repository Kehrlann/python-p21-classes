from rectangle import Rectangle


class Carre(Rectangle):
  def __init__(self, vertex, side):
      super().__init__(vertex, side, side)
  
  def __repr__(self):
      return f"Carré [{self.s1}, {self.width}]"

if __name__ == "__main__":
    c = Carre(
        (4, 4),
        5
    )
    print("q:", c)
    print("Périmètre de q:", c.perimetre())
    print("Aire de q:", c.aire())
    print("~~~~~~~~~~~~~~~")

    r = Rectangle((1,1), 1, 2)
    print(type(r))
    print(type(c))
    print(type(r) == type(c)) 
    print(isinstance(c, Carre))
    print(isinstance(c, Rectangle))
    print("rect")
    print(isinstance(r, Carre))
