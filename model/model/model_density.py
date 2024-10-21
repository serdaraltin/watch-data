from interfaces import IDensity
from datetime import datetime
from config import config

class Density(IDensity):
    modules = None
    def __init__(self, *args,**kwargs):
        # print("MODEL giriş")
        # super().__init__()
        # print("MODEL İÇİ")
        # self.status=status
        # print("STatus", self.status)
        # self.additional = additional if additional else {}
        # print("model içi kontrol")

        if kwargs:
            self._id = kwargs.get("id", -1)
            self._camera_id = kwargs["camera_id"]
            self._label = kwargs["label"]
            self._additional = kwargs["additional"]
            self._status = kwargs["status"]

        else:
            (   self._id,
                self._camera_id,
                self._label,
                self._additional,
                self._status
            ) = args
        
        self._createdAt = datetime.now().isoformat()
        self._updatedAt = datetime.now().isoformat()
    
    def yazdir(self):
        print("id" , self._id)
        print("camera_id" , self._camera_id)
        print("label",self._label)
        print("status", self._status)
        print("additional", json.dumps(self.additional))
    yazdir

    """
    def to_json(self):
        return {
            "id" : self._id,
            "camera_id" : self._camera_id,
            "label": self._label,
            "status": self._status,
            "additional": json.dumps(self.additional),
            "created_at": self._created_at.isoformat() if self._created_at else None,
            "updated_at": self._updated_at.isoformat() if self._updated_at else None
        }

    def from_json(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    """
    def __repr__(self):
        attributes = ", ".join(
            [f"'{k.strip('_')}': {repr(v)}" for k, v in self.__dict__.items()]
        )
        return f"{{{attributes}}}"

    def __str__(self):
        return self.__repr__()
    
    def to_dict(self):
        return {k.lstrip('_'): v for k, v in self.__dict__.items()}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def camera_id(self):
        return self._camera_id

    @camera_id.setter
    def camera_id(self, value):
        self._camera_id = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    
    @property
    def additional(self):
        return self._additional

    @additional.setter
    def additional(self, value):
        self._additional = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
        
    @property
    def createdAt(self):
        return self._createdAt

    @createdAt.setter
    def createdAt(self, value):
        self._createdAt = value

    @property
    def updatedAt(self):
        return self._updatedAt

    @updatedAt.setter
    def updatedAt(self, value):
        self._updatedAt = value
