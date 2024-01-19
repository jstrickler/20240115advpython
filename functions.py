
# FUNC(...)
# VAR = FUNC(...)
# x + FUNC(...)

def hello():  #  can define parameters
    print("Hello, Python world!")

hello()   # can pass arguments

def greet(whom="world"):
    print(f"Hello, {whom}")

greet("world")
greet("Mom")
greet("everybody!")
greet(1234)
greet()




