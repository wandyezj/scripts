print("Hello world!")

def f(i):
    if i % 2 == 0:
        print(f"{i} is even!")

for i in range(3):
    print(f"i = {i}")
    f(i)
    print()

print("done")

