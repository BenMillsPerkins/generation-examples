def outer_function():
  b = 20
  print("b", b)
  def inner_func():
    c = 30
    print("c", c)
  inner_func()

a = 10
b = 50
print("a", a)
outer_function()
print("b", b)