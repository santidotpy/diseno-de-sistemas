# visitor pattern 

class Visitor(object):
    def visit(self, element):
        pass

class Element(object): # Visitable
    def accept(self, visitor):
        pass

class ConcreteVisitor1(Visitor):
    def visit(self, element):
        print("ConcreteVisitor1: visit element %s" % element)

class ConcreteVisitor2(Visitor): # implementacion del visitante
    def visit(self, element):
        print("ConcreteVisitor2: visit element %s" % element)

class ConcreteElement1(Element):
    def accept(self, visitor):
        visitor.visit(self)

class ConcreteElement2(Element):
    def accept(self, visitor):
        visitor.visit(self)

class ObjectStructure(object):
    def __init__(self):
        self.elements = []

    def attach(self, element):
        self.elements.append(element)

    def detach(self, element):
        self.elements.remove(element)

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)

if __name__ == "__main__":
    obj = ObjectStructure()
    obj.attach(ConcreteElement1())
    obj.attach(ConcreteElement2())

    visitor1 = ConcreteVisitor1()
    obj.accept(visitor1)

    visitor2 = ConcreteVisitor2()
    obj.accept(visitor2)

