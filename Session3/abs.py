# a class which contains one or more abstract methods is called an abstract class

from abc import ABC, abstractmethod
class Help4code(ABC):
    @abstractmethod
    def training(self):
        pass
    @abstractmethod
    def placement(self):
        pass

class Ashish(Help4code):
    def training(self):
        print("I am in training")
    def placement(self):
        print("Java")

class Prashant(Help4code):
    def training(self):
        print("I am in training")
    def placement(self):
        print("Python")

obj1.Ashish()
obj1.training()
      

