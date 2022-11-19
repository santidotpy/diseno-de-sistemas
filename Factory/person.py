from abc import ABCMeta, abstractstaticmethod


# la I al principio quiere decir interfaz
class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        """ Metodo de Interfaz"""



class Student(IPerson):

    def __init__(self):
        self.name = 'Nombre Estudiante'

    # como implementamos la interfaz de IPerson hay que tratar el metodo que tenga
    def person_method(self):
        print('Soy un estudiante')


class Teacher(IPerson):

    def __init__(self):
        self.name = 'Nombre Profesor'

    # como implementamos la interfaz de IPerson hay que tratar el metodo que tenga
    def person_method(self):
        print('Soy un profesor')


# Factory
class PersonFactory:

    @staticmethod
    def create_person(person_type):
        types = {"estudiante": Student, "profesor":Teacher}
        return types[person_type]()

        # if person_type == 'estudiante':
        #     return Student()
        # if person_type == 'profesor':
        #     return Teacher()
        # print('Invalid Type')
        # return -1

if __name__ == "__main__":
    choice = input('Ingrese tipo de persona (profesor / estudiante): \n')
    person = PersonFactory.create_person(choice.lower())
    person.person_method()

# s = Student()
# s.person_method()

# t = Teacher()
# t.person_method()