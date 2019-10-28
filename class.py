z = 10  # a global variable

class A:
    @classmethod
    def f(cls, a1):
        cls.a = a1
    def g(self, b1):
        global z
        self.b = b1
        z = 20

obj1 = A()
obj2 = A()
print(z)

obj1.f(10)
obj1.g(20)
print(obj1.a, obj1.b)
print(z)

obj2.f(30)
obj2.g(40)
print(obj2.a, obj2.b)
print(z)

print(obj1.a, obj1.b)
