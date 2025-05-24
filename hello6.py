a = "I am global"

def f():
    global a
    a = "Modified globally"
    print(a)

f()
print(a)