
# example of a composite object with a single child that contains a single child

class Component(object):

    def __init__(self, *args, **kwargs):
        self.children = []
        self.name = kwargs.get('name', None)

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_child(self, index):
        return self.children[index]

    def operation(self):
        print("operation on %s" % self.name)
        for child in self.children:
            child.operation()

if __name__ == "__main__":

    root = Component(name="root")
    child1 = Component(name="child1")
    child2 = Component(name="child2")
    root.add(child1)
    root.add(child2)
    child1.add(Component(name="grandchild1"))
    child1.add(Component(name="grandchild2"))
    child2.add(Component(name="grandchild3"))
    root.operation()
    