from abc import ABC, abstractmethod

class IStatistic():
    
    
    @property
    @abstractmethod
    def enter(self):
        pass
    
    @property
    @abstractmethod
    def exit(self):
        pass
    
    @property
    @abstractmethod
    def female(self):
        pass
    
    @property
    @abstractmethod
    def male(self):
        pass
    
    @property
    @abstractmethod
    def total(self):
        pass
    
    @property
    @abstractmethod
    def current(self):
        pass

    @property
    @abstractmethod
    def current_female(self):
        pass
    
    @property
    @abstractmethod
    def current_male(self):
        pass
    
    @abstractmethod
    def push(self, value):
        pass
    
    @abstractmethod
    def pop(self):
        pass
    
    @abstractmethod
    def filter_by_key(self, value):
        pass
    
class IStatisticDensity():

    @property
    @abstractmethod
    def label(self):
        pass

    @property
    @abstractmethod
    def status(self):
        pass