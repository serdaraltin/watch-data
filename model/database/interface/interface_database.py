from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def close(self):
        pass
    
    @abstractmethod
    def select(self):
        pass
    
    @abstractmethod
    def insert(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass    