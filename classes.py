class User:
  def __init__(self, first_name, last_name) -> None:
      print("INIT", first_name)
      self._first_name = first_name
      self.last_name = last_name
      self.has_been_printed = False

  def greet(self):
    print("GREETING")
    print(f"Hello, {self._first_name}")

  def change_first_name(self, new_name):
    if not self.is_offensive(new_name):
      self._first_name = new_name
  
  def __repr__(self):
      self.greet()
      return f"{self._first_name} {self.last_name}"

daniel = User("Daniel", "Garnier")
daniel._first_name = "Trololo"
daniel.greet()
User.greet(daniel)
bianca = User("Bianca", "Castafiore")
print(bianca)