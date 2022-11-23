# facade pattern 

class Subsystem1(object):
    def method1(self):
        print("Subsystem1: method1")

class Subsystem2(object):
    def method2(self):
        print("Subsystem2: method2")

class Facade(object):
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def method(self):
        self.subsystem1.method1()
        self.subsystem2.method2()

if __name__ == "__main__":
    facade = Facade()
    facade.method()

# Path: Facade/pattern.py
# facade pattern

