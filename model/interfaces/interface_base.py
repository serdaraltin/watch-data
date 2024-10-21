from abc import ABC, abstractmethod

class IBase(ABC):

    @abstractmethod
    def __str__(self) -> str:
        return self.__str__

    @abstractmethod
    def __repr__(self) -> str:
        return self.__repr__
    
    # @abstractmethod
    # def __dict__(self) -> dict:
    #     return self.__dict__
    

    @property
    @abstractmethod
    def id(self):
        pass

    @id.setter
    @abstractmethod
    def id(self, value):
        pass

    @property
    @abstractmethod
    def createdAt(self):
        pass

    @createdAt.setter
    @abstractmethod
    def createdAt(self, value):
        pass

    @property
    @abstractmethod
    def updatedAt(self):
        pass

    @updatedAt.setter
    @abstractmethod
    def updatedAt(self, value):
        pass