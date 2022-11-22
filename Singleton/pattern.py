# singleton pattern in python


class Singleton:
    __instance = None # private static attribute to hold the instance of the class 

    @staticmethod # static method doesn't require an instance of the class to be called 
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

s = Singleton()
print(s)

s = Singleton.get_instance()
print(s)


