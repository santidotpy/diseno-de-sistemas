# abstract factory pattern in python

from abc import ABCMeta, abstractmethod

class AbstractFactory(metaclass=ABCMeta): 
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

class AbstractProductA(metaclass=ABCMeta):
    @abstractmethod
    def useful_function_a(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self): # override abstract method in AbstractProductA
        return "The result of the product A1."

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A2."

class AbstractProductB(metaclass=ABCMeta):
    @abstractmethod
    def useful_function_b(self):
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator):
        pass

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator):
        result = collaborator.useful_function_a()
        return "The result of the B1 collaborating with the ({})".format(result)

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator):
        result = collaborator.useful_function_a()
        return "The result of the B2 collaborating with the ({})".format(result)

def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_b.useful_function_b())
    print(product_b.another_useful_function_b(product_a), end="")

if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())
    print("")



