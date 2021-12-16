class User:
  def __init__(self, name: str, age: int) -> None:
      self.name = name
      self.age = age

  def is_older(self, other):
    return self.age >= other.age

  def __repr__(user):
    return user.name + " is " + str(user.age) + " years old"
  
  def __gt__(self, other):
    return self.is_older(other)

a = User("a", 10)
b = User("b", 15)
print(b.is_older(a))
c = a
a2 = User("a", 10)
print(a)
print(c)
print(a2)
print(a > b)