from abc import ABC, abstractmethod
from .interface_base import IBase


class ICamera(IBase):

    # branch_id
    @property
    @abstractmethod
    def branch_id(self):
        pass

    @branch_id.setter
    @abstractmethod
    def branch_id(self):
        pass

    # model
    @property
    @abstractmethod
    def model(self):
        pass

    @model.setter
    @abstractmethod
    def model(self):
        pass

    # resolution
    @property
    @abstractmethod
    def resolution(self):
        pass

    @resolution.setter
    @abstractmethod
    def resolution(self):
        pass

    # install_date
    @property
    @abstractmethod
    def install_date(self):
        pass

    @install_date.setter
    @abstractmethod
    def install_date(self):
        pass

    # status
    @property
    @abstractmethod
    def status(self):
        pass

    @status.setter
    @abstractmethod
    def status(self):
        pass


    # streaming_url
    @property
    @abstractmethod
    def streaming_url(self):
        pass

    @streaming_url.setter
    @abstractmethod
    def streaming_url(self):
        pass

