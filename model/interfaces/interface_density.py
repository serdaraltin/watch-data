from abc import ABC, abstractmethod
from datetime import datetime
from .interface_base import IBase

class IDensity(IBase):

    @property
    @abstractmethod
    def camera_id(self):
        pass

    @camera_id.setter
    @abstractmethod
    def camera_id(self, value):
        pass
    
    @property
    @abstractmethod
    def label(self):
        pass

    @label.setter
    @abstractmethod
    def label(self, value):
        pass

    @property
    @abstractmethod
    def additional(self):
        pass

    @additional.setter
    @abstractmethod
    def additional(self, value):
        pass

    @property
    @abstractmethod
    def status(self):
        pass

    @status.setter
    @abstractmethod
    def status(self, value):
        pass