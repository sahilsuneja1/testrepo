def f():
    fd = open("sagar.txt","w")
    fd.write("I am awesome!")
    fd.close()

def g():
    with open("sahil", "a") as f:
        f.write("Me too!\n")
        f.write("Me loo!\n")
        f.write("Me poo!")

def h():
    z = open("sahil","r")
    lines = z.readlines()
    for line in lines:
        print(line.upper())

def h1():
    print("hello")
