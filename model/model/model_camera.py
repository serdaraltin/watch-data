from interfaces import ICamera
from datetime import datetime
import json

class Camera(ICamera):
    def __init__(
        self,
        id=None,
        branch_id=None,
        label=None,
        protocol=None,
        host=None,
        port=None,
        user=None,
        password=None,
        channel=None,
        model=None,
        type=None,
        resolution=None,
        install_date=None,
        status=None,
        additional=None,
        created_at=None,
        updated_at=None,
    ):
        self.id = id
        self.branch_id = branch_id
        self.label = label
        self.protocol = protocol
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.channel = channel
        self.model = model
        self.type = type
        self.resolution = resolution
        self.install_date = install_date if install_date else datetime.now()
        self.status = status
        self.additional = additional if additional else {}
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def to_json(self):
        return {
            "id": self.id,
            "branch_id": self.branch_id,
            "label": self.label,
            "protocol": self.protocol,
            "host": self.host,
            "port": self.port,
            "user": self.user,
            "password": self.password,
            "channel": self.channel,
            "model": self.model,
            "type": self.type,
            "resolution": self.resolution,
            "install_date": self.install_date.isoformat()
            if self.install_date
            else None,
            "status": self.status,
            "additional": json.dumps(self.additional),
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    def from_json(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        attributes = ", ".join(
            [f"'{k.strip('_')}': {repr(v)}" for k, v in self.__dict__.items()]
        )
        return f"{{{attributes}}}"

    def __str__(self):
        return self.__repr__()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
