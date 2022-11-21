import abc 


# Visitante
class Visitor(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def visit_mago(self, mago):
        pass

    @abc.abstractmethod
    def visit_guerrero(self, guerrero):
        pass

    @abc.abstractmethod
    def visit_characters(self, characters): # visitante de cualquier tipo de personaje
        pass



# Visitable / Visitable
class Visitable(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def accept(self, visitor):
        pass



# Equipar encantacion

class EquiparEncantacion(Visitor):
    
    def visit_mago(self, mago):
        #print("Equipar encantacion a mago")
        if mago.get_magic_level() <= 5:
            mago.set_encantacion('Fuego')
        else:
            mago.set_encantacion('Hielo')

    def visit_guerrero(self, guerrero):
        #print("Equipar encantacion a guerrero")
        pass

    def visit_characters(self, characters):
        #print("Equipar encantacion a cualquier personaje")
        for character in characters:
            character.accept(self)


# Equipar arma

class EquiparArma(Visitor):
        
        def visit_mago(self, mago):
            #print("Equipar arma a mago")
            mago.set_arma('Varita')
    
        def visit_guerrero(self, guerrero):
            #print("Equipar arma a guerrero")
            guerrero.set_arma('Espada')
            # if guerrero.get_strength() <= 5:
            #     guerrero.set_weapon('Espada')
            # else:
            #     guerrero.set_weapon('Hacha')
    
        def visit_characters(self, characters):
            #print("Equipar arma a cualquier personaje")
            for character in characters:
                character.accept(self)



# Mago

class Mago(Visitable):

    def __init__(self):
        self.__magic_level = 1
        self.__encantacion = ''
        self.__arma = ''

    def get_arma(self):
        return self.__arma

    def set_arma(self, arma):
        self.__arma = arma

    def get_encantacion(self):
        return self.__encantacion

    def set_encantacion(self, encantacion):
        self.__encantacion = encantacion

    def get_magic_level(self):
        return self.__magic_level

    def set_magic_level(self, magic_level):
        self.__magic_level = magic_level

    def accept(self, visitor):
        visitor.visit_mago(self)


# Guerrero

class Guerrero(Visitable):

    def __init__(self):
        self.__arma = ''

    def get_arma(self):
        return self.__arma

    def set_arma(self, arma):
        self.__arma = arma

    def accept(self, visitor):
        visitor.visit_guerrero(self)



# Cliente

def main():
    # creamos 2 guerrerros y 2 magos
    w1 = Guerrero()
    w2 = Guerrero()

    m1 = Mago()
    m2 = Mago()

    # cada mago con distintos niveles de magia
    m1.set_magic_level(3)
    m2.set_magic_level(7)

    characters = [w1, w2, m1, m2]

    # visitantes concretos
    equipar_arma = EquiparArma()
    equipar_arma.visit_characters(characters)

    equipar_encantacion = EquiparEncantacion()
    equipar_encantacion.visit_characters(characters)

    print(f'Magic level of {m1} is {m1.get_magic_level()}, encantacion is {m1.get_encantacion()}, weapon is {m1.get_arma()}')
    print(f'Magic level of {m2} is {m2.get_magic_level()}, encantacion is {m2.get_encantacion()}, weapon is {m2.get_arma()}\n')

    print(f'Guerrero {w1}, arma: {w1.get_arma()}')
    print(f'Guerrero {w2}, arma: {w2.get_arma()}\n')

    # for character in characters:
    #     print(character.get_arma())


if __name__ == "__main__":
    main()

