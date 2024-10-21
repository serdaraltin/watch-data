from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
import json

Base = declarative_base()
class PersonDB(Base):
    __tablename__ = "Person"
    id = Column(Integer, primary_key=True)
    camera_id = Column(Integer)
    detection_time = Column(DateTime)
    label = Column(String)
    confidence = Column(Float)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)

class EnterExitDB(Base):
    __tablename__ = "EnterExit"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer)
    event_time = Column(DateTime)
    event_type = Column(String)
class GenderDB(Base):
    __tablename__ = "Gender"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer)
    gender = Column(String)
    confidence = Column(Float)

class AgeDB(Base):
    __tablename__ = "Age"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer)
    age_range = Column(String)
    confidence = Column(Float)


class CameraDB(Base):
    __tablename__ = 'Camera'

    id = Column(Integer, primary_key=True)
    branch_id = Column(Integer)
    model = Column(String(255))
    resolution = Column(String(20))
    install_date = Column(DateTime)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    label = Column(String(255))
    protocol = Column(String(20))
    host = Column(String(255))
    port = Column(Integer)
    user = Column(String(50))
    password = Column(String(50))
    channel = Column(Integer)
    type = Column(String(30))
    status = Column(Boolean)
    additional = Column(JSON)

    def to_json(self):
        # Bu metot nesnenin özelliklerini JSON formatına çevirir.
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
            "install_date": self.install_date.isoformat() if self.install_date else None,
            "status": self.status,
            "additional": json.dumps(self.additional) if self.additional else None,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None,
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None,
        }

class DensityDB(Base):
    __tablename__ = "Density"
    id = Column(Integer, primary_key=True)
    camera_id = Column(Integer)
    label = Column(String)
    status = Column(Boolean)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    additional = Column(JSON)

    def to_json(self):
        # Bu metot nesnenin özelliklerini JSON formatına çevirir.
        return {
            "id": self.id,
            "camera_id" : self._camera_id,
            "label": self.label,
            "status": self.status,
            "additional": json.dumps(self.additional) if self.additional else None,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None,
            "updatedAt": self.updatedAt.isoformat() if self.updatedAt else None,
        }