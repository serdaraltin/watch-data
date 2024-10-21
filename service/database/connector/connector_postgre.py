from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime
from config import config



from database.model import PersonDB, EnterExitDB, GenderDB, AgeDB


class PersonDatabase:
    def __init__(self) -> None:
        self.person_id = None

        provider_db = config.setting.network.database.provider
        host_db = config.setting.network.database.host
        port_db = config.setting.network.database.port
        database_db = config.setting.network.database.database
        user_db = config.setting.network.database.user
        password_db = config.setting.network.database.password

        # Veritabani baglantisi
        DATABASE_URL = f"{provider_db}+psycopg2://{user_db}:{password_db}@{host_db}:{port_db}/{database_db}"
        engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def set_data(self, data):
        self.data = data


    def get_person_data(self):
        return {
            "camera_id": self.data["camera_id"],
            "detection_time": self.data["detection_time"],
            "label": self.data["label"],
            "confidence": self.data["confidence"],
        }

    def get_enterexit_data(self, person_id):
        enter_exit_data = self.data["enter_exit"]
        if isinstance(enter_exit_data, dict):
            return {
                "person_id": person_id,
                "event_time": enter_exit_data["event_time"],
                "event_type": enter_exit_data["event_type"],
            }
        elif enter_exit_data:
            return {
                "person_id": person_id,
                "event_time": enter_exit_data.event_time,  
                "event_type": enter_exit_data.event_type,  
            }
        elif enter_exit_data == None:
            return None

    def get_gender_data(self, person_id):
        gender_data = self.data["gender"]
        if isinstance(gender_data, dict):
            return {
                "person_id": person_id,
                "gender": gender_data["gender"],
                "confidence": gender_data["confidence"],
            }
        elif gender_data:
            return {
                "person_id": person_id,
                "gender": gender_data.gender,  
                "confidence": gender_data.confidence,  
            }
        elif gender_data == None:
            return None

    def get_age_data(self, person_id):
        age_data = self.data["age"]
        if isinstance(age_data, dict):
            return {
                "person_id": person_id,
                "age_range": age_data["age_range"],
                "confidence": age_data["confidence"],
            }
        elif age_data:
            return {
                "person_id": person_id,
                "age_range": age_data.age_range, 
                "confidence": age_data.confidence, 
            }
        elif age_data == None:
            return None

    def commit(self):
        person = PersonDB(**self.get_person_data())
        self.session.add(person)
        self.session.commit()

        person_id = person.id
        print(f"Person data commit: id = {person_id}")

        if self.get_enterexit_data(person_id):
            enterexit = EnterExitDB(**self.get_enterexit_data(person_id))
            self.session.add(enterexit)
            self.session.commit()
            print(f"EnterExit data commit: id = {enterexit.id}")

        if self.get_gender_data(person_id):
            gender = GenderDB(**self.get_gender_data(person_id))
            self.session.add(gender)
            self.session.commit()
            print(f"Gender data commit : id = {gender.id}")

        if self.get_age_data(person_id):
            age = AgeDB(**self.get_age_data(person_id))
            self.session.add(age)
            self.session.commit()
            print(f"Age data commit : id = {age.id}")

        # self.session.close()
