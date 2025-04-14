class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my age is {self.age}")

p1 = person("yuva", 36)
p1.myfunc()