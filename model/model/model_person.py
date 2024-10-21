from interfaces import IPerson, IEnterExit, IGender, IAge, IMovement
from datetime import datetime
from config import config

class Person(IPerson):
    modules = None

    def __init__(self, age, gender, enter_exit, *args, **kwargs):
        super().__init__()

        self.age = age
        self.gender = gender
        self.enter_exit = enter_exit
        

        if kwargs:
            self._id = kwargs.get("id", -1)
            self._camera_id = kwargs["camera_id"]
            self._detection_time = kwargs["detection_time"]
            self._label = kwargs["label"]
            self._confidence = kwargs["confidence"]
        else:
            (
                self._camera_id,
                self._detection_time,
                self._label,
                self._confidence,
                self._id,
            ) = args

        self._createdAt = datetime.now().isoformat()
        self._updatedAt = datetime.now().isoformat()

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
    def detection_time(self):
        return self._detection_time

    @detection_time.setter
    def detection_time(self, value):
        self._detection_time = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value

    @property
    def confidence(self):
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        self._confidence = value

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


class EnterExit(IEnterExit):
    def __init__(self, *args, **kwargs):
        super().__init__()
        if kwargs:
            self._id = kwargs.get("id", -1)
            self._person_id =  kwargs["person_id"]
            self._event_time = kwargs["event_time"]
            self._event_type = kwargs["event_type"]
        else:
            self._person_id, self._event_time, self._event_type, self._id = args

        self._createdAt = datetime.now().isoformat()
        self._updatedAt = datetime.now().isoformat()

    def __repr__(self):
        if config.setting.module.detect["enter_exit"]:
            attributes = ", ".join(
                [f"'{k.strip('_')}': {repr(v)}" for k, v in self.__dict__.items()]
            )
            return f"{{{attributes}}}"
        else:
            return "None"

    def __str__(self):
        return self.__repr__()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value

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


class Gender(IGender):
    def __init__(self, *args, **kwargs):
        super().__init__()


        if kwargs:
            self._id = kwargs.get("id", -1)
            self._person_id = kwargs["person_id"]
            self._gender = kwargs["gender"]
            self._confidence = kwargs["confidence"]
        else:
            self._person_id, self._gender, self._confidence, self._id = args

        self._createdAt = datetime.now().isoformat()
        self._updatedAt = datetime.now().isoformat()

    def __repr__(self):
        if config.setting.module.detect["gender"]:
            attributes = ", ".join(
                [f"'{k.strip('_')}': {repr(v)}" for k, v in self.__dict__.items()]
            )
            return f"{{{attributes}}}"
        else:
            return "None"

    def __str__(self):
        return self.__repr__()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def confidence(self):
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        self._confidence = value

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


class Age(IAge):
    def __init__(self, *args, **kwargs):
        super().__init__()
        if kwargs:
            self._id = kwargs.get("id", -1)
            self._person_id = kwargs["person_id"]
            self._age_range = kwargs["age_range"]
            self._confidence = kwargs["confidence"]
        else:
            self._person_id, self._age_range, self._confidence, self._id = args

        self._createdAt = datetime.now().isoformat()
        self._updatedAt = datetime.now().isoformat()

    def __repr__(self):
        if config.setting.module.detect["age"]:
            attributes = ", ".join(
                [f"'{k.strip('_')}': {repr(v)}" for k, v in self.__dict__.items()]
            )
            return f"{{{attributes}}}"
        else:
            return "None"

    def __str__(self):
        return self.__repr__()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value

    @property
    def age_range(self):
        return self._age_range

    @age_range.setter
    def age_range(self, value):
        self._age_range = value

    @property
    def confidence(self):
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        self._confidence = value

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


class Movement(IMovement):
    def __init__(self, *args, **kwargs):
        super().__init__()

        if kwargs:
            self._id = kwargs.get("id", -1)
            self._person_id = kwargs["person_id"]
            self._movement_type = kwargs["movement_type"]
            self._start_time = kwargs["start_time"]
            self.end_time = kwargs["end_time"]
        else:
            self._person_id, self._age_range, self._confidence, self._id = args

        self._createdAt = datetime.now().isoformat()
        self._updatedAt = datetime.now().isoformat()

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

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value

    @property
    def movement_type(self):
        return self._movement_type

    @movement_type.setter
    def movement_type(self, value):
        self._movement_type = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value

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
