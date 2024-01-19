def silly():
    yield "apple"
    yield "banana"
    for i in range(3):
        yield i


s = silly()  
print(f"{s = }")
for thing in s:
    print(thing)

