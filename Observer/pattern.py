# observer pattern implementation in python

# observable
class Subject(object):
    def __init__(self):
        self.observers = []
    def register(self, observer):
        self.observers.append(observer)
    def unregister(self, observer):
        self.observers.remove(observer)
    def notify(self): # notify all observers
        for observer in self.observers:
            observer.update(self)


class Observer(object):
    def __init__(self, subject):
        subject.register(self)
    def update(self, subject):
        print(type(self).__name__, subject)
        print(f'{subject.name} esta siendo observado')

class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self.data = 0
    def setData(self, data):
        self.data = data
        self.notify()
    def getData(self):
        return self.data

def main():
    data = Data('data1')
    data2 = Data('data2')

    view1 = Observer(data)
    view2 = Observer(data)
    view3 = Observer(data2)
    
    data.setData(10)
    data.setData(20)
    data.setData(30)

    data2.setData('hello')
    data2.setData('world')

if __name__ == '__main__':
    main()