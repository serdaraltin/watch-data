from abc import ABC, abstractmethod
from datetime import datetime
from .interface_base import IBase

class IPerson(IBase):

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
    def detection_time(self):
        pass

    @detection_time.setter
    @abstractmethod
    def detection_time(self, value):
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
    def confidence(self):
        pass

    @confidence.setter
    @abstractmethod
    def confidence(self, value):
        pass

class IEnterExit(IBase):


    @property
    @abstractmethod
    def person_id(self):
        pass

    @person_id.setter
    @abstractmethod
    def person_id(self, value):
        pass

    @property
    @abstractmethod
    def event_time(self):
        pass

    @event_time.setter
    @abstractmethod
    def event_time(self, value):
        pass

    @property
    @abstractmethod
    def event_type(self):
        pass

    @event_type.setter
    @abstractmethod
    def event_type(self, value):
        pass

class IGender(IBase):

    @property
    @abstractmethod
    def person_id(self):
        pass

    @person_id.setter
    @abstractmethod
    def person_id(self, value):
        pass

    @property
    @abstractmethod
    def gender(self):
        pass

    @gender.setter
    @abstractmethod
    def gender(self, value):
        pass

    @property
    @abstractmethod
    def confidence(self):
        pass

    @confidence.setter
    @abstractmethod
    def confidence(self, value):
        pass

class IAge(IBase):

    @property
    @abstractmethod
    def person_id(self):
        pass

    @person_id.setter
    @abstractmethod
    def person_id(self, value):
        pass

    @property
    @abstractmethod
    def age_range(self):
        pass

    @age_range.setter
    @abstractmethod
    def age_range(self, value):
        pass

    @property
    @abstractmethod
    def confidence(self):
        pass

    @confidence.setter
    @abstractmethod
    def confidence(self, value):
        pass

class IMovement(IBase):

    @property
    @abstractmethod
    def person_id(self):
        pass

    @person_id.setter
    @abstractmethod
    def person_id(self, value):
        pass

    @property
    @abstractmethod
    def movement_type(self):
        pass

    @movement_type.setter
    @abstractmethod
    def movement_type(self, value):
        pass

    @property
    @abstractmethod
    def start_time(self):
        pass

    @start_time.setter
    @abstractmethod
    def start_time(self, value):
        pass

    @property
    @abstractmethod
    def end_time(self):
        pass

    @end_time.setter
    @abstractmethod
    def end_time(self, value):
        pass