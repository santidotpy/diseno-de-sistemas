# example of the observer pattern 

class Subject:
    def __init__(self):
        self.observers = []
    def attach(self, observer):
        self.observers.append(observer)
    def notify(self, modifier=None):
        for observer in self.observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject):
    def __init__(self, name=""):
        Subject.__init__(self)
        self.name = name
        self._temp = 0
    @property
    def temp(self):
        return self._temp
    @temp.setter
    def temp(self, temp):
        self._temp = temp
        self.notify()

class TempViewer:
    def update(self, subject):
        print(f"Temperature Viewer: {subject.name} has Temperature {subject.temp}")

# Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

# Let's change the temperature of our first core
c1.temp = 80
c1.temp = 90

# Let's attach our observer to the second core
c2.attach(v1)
c2.temp = 120

# Output:
# Temperature Viewer: Core 1 has Temperature 80
# Temperature Viewer: Core 1 has Temperature 90
# Temperature Viewer: Core 2 has Temperature 120
