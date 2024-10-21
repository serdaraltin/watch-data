import unittest
from model import (
    Person,
    EnterExit,
    Gender,
    Age,
    Movement,
)
from datetime import datetime, timedelta


class TestPersonConcreteClass(unittest.TestCase):
    def setUp(self):
        self.person_args = (101, datetime.now(), "label_1", 0.9, 1)
        self.person_kwargs = {
            "id": 2,
            "camera_id": 102,
            "detection_time": datetime.now(),
            "label": "label_2",
            "confidence": 0.95,
        }

        self.person_with_args = Person(*self.person_args)
        self.person_with_kwargs = Person(**self.person_kwargs)

    def test_id_setter_getter(self):
        # ID ozelliginin setter ve getter metodlarini kontrol et# 
        self.person_with_args.id = 2
        self.assertEqual(self.person_with_args.id, 2)

    def test_camera_id_setter_getter(self):
        # Camera ID ozelliginin setter ve getter metodlarini kontrol et# 
        self.person_with_args.camera_id = 102
        self.assertEqual(self.person_with_args.camera_id, 102)

    def test_detection_time_setter_getter(self):
        # Detection Time ozelliginin setter ve getter metodlarini kontrol et# 
        new_time = datetime.now()
        self.person_with_args.detection_time = new_time
        self.assertEqual(self.person_with_args.detection_time, new_time)

    def test_label_setter_getter(self):
        # Label ozelliginin setter ve getter metodlarini kontrol et# 
        self.person_with_args.label = "label_2"
        self.assertEqual(self.person_with_args.label, "label_2")

    def test_confidence_setter_getter(self):
        # Confidence ozelliginin setter ve getter metodlarini kontrol et# 
        self.person_with_args.confidence = 0.8
        self.assertEqual(self.person_with_args.confidence, 0.8)

    def test_created_at_setter_getter(self):
        # CreatedAt ozelliginin setter ve getter metodlarini kontrol et# 
        new_date = datetime(2022, 1, 1)
        self.person_with_args.createdAt = new_date
        self.assertEqual(self.person_with_args.createdAt, new_date)

    def test_repr(self):
        person_with_args = self.person_with_args
        
        # __repr__ çıktısının beklenen formatı
        expected_repr = f"Person(camera_id={person_with_args.camera_id}, detection_time={repr(person_with_args.detection_time)}, label='{person_with_args.label}', confidence={person_with_args.confidence}, id={person_with_args.id}, createdAt={repr(person_with_args.createdAt)}, updatedAt={repr(person_with_args.updatedAt)})"

        # Gerçek __repr__ çıktısını kontrol et
        self.assertEqual(repr(person_with_args), expected_repr)



class TestEnterExitConcreteClass(unittest.TestCase):
    def setUp(self):
        self.current_time = datetime.now()
        self.enter_exit_args = (10, self.current_time, "enter", 1)
        self.enter_exit_kwargs = {
            "person_id": 11,
            "event_time": self.current_time,
            "event_type": "exit",
            "id": 2,
        }

        self.enter_exit_with_args = EnterExit(*self.enter_exit_args)
        self.enter_exit_with_kwargs = EnterExit(**self.enter_exit_kwargs)

    def test_initialization_with_args(self):
        # Argumanlarla baslatma isleminin kontrolu# 
        self.assertEqual(self.enter_exit_with_args.person_id, self.enter_exit_args[0])
        self.assertEqual(self.enter_exit_with_args.event_type, self.enter_exit_args[2])
        self.assertIsInstance(self.enter_exit_with_args.event_time, datetime)
        self.assertEqual(self.enter_exit_with_args.id, self.enter_exit_args[3])

    def test_initialization_with_kwargs(self):
        # Sözlük kullanarak baslatma isleminin kontrolu# 
        for key, value in self.enter_exit_kwargs.items():
            self.assertEqual(getattr(self.enter_exit_with_kwargs, key), value)

    def test_id_setter_getter(self):
        # ID özelliğinin setter ve getter metodlarını kontrol et# 
        self.enter_exit_with_args.id = 3
        self.assertEqual(self.enter_exit_with_args.id, 3)

    def test_person_id_setter_getter(self):
        # Person ID özelliğinin setter ve getter metodlarını kontrol et# 
        self.enter_exit_with_args.person_id = 12
        self.assertEqual(self.enter_exit_with_args.person_id, 12)

    def test_event_time_setter_getter(self):
        # Event Time özelliğinin setter ve getter metodlarını kontrol et# 
        new_time = datetime.now()
        self.enter_exit_with_args.event_time = new_time
        self.assertEqual(self.enter_exit_with_args.event_time, new_time)

    def test_event_type_setter_getter(self):
        # Event Type özelliğinin setter ve getter metodlarını kontrol et# 
        self.enter_exit_with_args.event_type = "stay"
        self.assertEqual(self.enter_exit_with_args.event_type, "stay")

    def test_created_at_setter_getter(self):
        # CreatedAt özelliğinin setter ve getter metodlarını kontrol et# 
        new_date = datetime(2022, 1, 1)
        self.enter_exit_with_args.createdAt = new_date
        self.assertEqual(self.enter_exit_with_args.createdAt, new_date)

    def test_updated_at_setter_getter(self):
        # UpdatedAt özelliğinin setter ve getter metodlarını kontrol et# 
        new_date = datetime(2022, 1, 2)
        self.enter_exit_with_args.updatedAt = new_date
        self.assertEqual(self.enter_exit_with_args.updatedAt, new_date)

    def test_repr(self):
        # __repr__ metodunun dogru ciktiyi verip vermedigini kontrol et# 
        expected_repr = (f"{{'person_id': 10, 'event_time': {repr(self.enter_exit_with_args.event_time)}, " +
                         f"'event_type': 'enter', 'id': 1, 'createdAt': {repr(self.enter_exit_with_args.createdAt)}, " +
                         f"'updatedAt': {repr(self.enter_exit_with_args.updatedAt)}}}")
        self.assertEqual(repr(self.enter_exit_with_args), expected_repr)


class TestGenderConcreteClass(unittest.TestCase):

    def setUp(self):
        # Ornek veri ile sinifin baslangic durumunu ayarla
        self.gender_instance = Gender(person_id=1, gender='M', confidence=0.95)

    def test_initialization_with_kwargs(self):
        # Keyword argumanlari ile baslangic durumunu kontrol et
        self.assertEqual(self.gender_instance.person_id, 1)
        self.assertEqual(self.gender_instance.gender, 'M')
        self.assertEqual(self.gender_instance.confidence, 0.95)
        self.assertIsInstance(self.gender_instance.createdAt, datetime)
        self.assertIsInstance(self.gender_instance.updatedAt, datetime)

    def test_initialization_with_args(self):
        # Pozisyonel argumanlar ile baslangic durumunu kontrol et
        instance = Gender(2, 'F', 0.90, 3)
        self.assertEqual(instance.person_id, 2)
        self.assertEqual(instance.gender, 'F')
        self.assertEqual(instance.confidence, 0.90)
        self.assertEqual(instance.id, 3)

    def test_id_property(self):
        # id ozelliginin setter ve getter metodlarini kontrol et
        self.gender_instance.id = 10
        self.assertEqual(self.gender_instance.id, 10)

    def test_person_id_property(self):
        # person_id ozelliginin setter ve getter metodlarini kontrol et
        self.gender_instance.person_id = 5
        self.assertEqual(self.gender_instance.person_id, 5)

    def test_gender_property(self):
        # gender ozelliginin setter ve getter metodlarini kontrol et
        self.gender_instance.gender = 'F'
        self.assertEqual(self.gender_instance.gender, 'F')

    def test_confidence_property(self):
        # confidence ozelliginin setter ve getter metodlarini kontrol et
        self.gender_instance.confidence = 0.85
        self.assertEqual(self.gender_instance.confidence, 0.85)

    def test_created_at_property(self):
        # createdAt ozelliginin setter ve getter metodlarini kontrol et
        new_date = datetime(2024, 1, 1)
        self.gender_instance.createdAt = new_date
        self.assertEqual(self.gender_instance.createdAt, new_date)

    def test_updated_at_property(self):
        # updatedAt ozelliginin setter ve getter metodlarini kontrol et
        new_date = datetime(2024, 1, 2)
        self.gender_instance.updatedAt = new_date
        self.assertEqual(self.gender_instance.updatedAt, new_date)

    def test_repr(self):
        # __repr__ metodunun dogru calistigini kontrol et
        representation = repr(self.gender_instance)
        self.assertIn("'person_id': 1", representation)
        self.assertIn("'gender': 'M'", representation)
        self.assertIn("'confidence': 0.95", representation)


class TestAgeConcreteClass(unittest.TestCase):

    def setUp(self):
        # Ornek veri ile sinifin baslangic durumunu ayarla
        self.age_instance = Age(person_id=1, age_range='18-25', confidence=0.95)

    def test_initialization_with_kwargs(self):
        # Keyword argumanlari ile baslangic durumunu kontrol et
        self.assertEqual(self.age_instance.person_id, 1)
        self.assertEqual(self.age_instance.age_range, '18-25')
        self.assertEqual(self.age_instance.confidence, 0.95)
        self.assertIsInstance(self.age_instance.createdAt, datetime)
        self.assertIsInstance(self.age_instance.updatedAt, datetime)

    def test_initialization_with_args(self):
        # Pozisyonel argumanlar ile baslangic durumunu kontrol et
        instance = Age(2, '26-33', 0.90, 3)
        self.assertEqual(instance.person_id, 2)
        self.assertEqual(instance.age_range, '26-33')
        self.assertEqual(instance.confidence, 0.90)
        self.assertEqual(instance.id, 3)

    def test_id_property(self):
        # id ozelliginin setter ve getter metodlarini kontrol et
        self.age_instance.id = 10
        self.assertEqual(self.age_instance.id, 10)

    def test_person_id_property(self):
        # person_id ozelliginin setter ve getter metodlarini kontrol et
        self.age_instance.person_id = 5
        self.assertEqual(self.age_instance.person_id, 5)

    def test_age_range_property(self):
        # age_range ozelliginin setter ve getter metodlarini kontrol et
        self.age_instance.age_range = '34-41'
        self.assertEqual(self.age_instance.age_range, '34-41')

    def test_confidence_property(self):
        # confidence ozelliginin setter ve getter metodlarini kontrol et
        self.age_instance.confidence = 0.80
        self.assertEqual(self.age_instance.confidence, 0.80)

    def test_created_at_property(self):
        # createdAt ozelliginin setter ve getter metodlarini kontrol et
        new_date = datetime(2024, 1, 1)
        self.age_instance.createdAt = new_date
        self.assertEqual(self.age_instance.createdAt, new_date)

    def test_updated_at_property(self):
        # updatedAt ozelliginin setter ve getter metodlarini kontrol et
        new_date = datetime(2024, 1, 2)
        self.age_instance.updatedAt = new_date
        self.assertEqual(self.age_instance.updatedAt, new_date)

    def test_repr(self):
        # __repr__ metodunun dogru calistigini kontrol et
        representation = repr(self.age_instance)
        self.assertIn("'person_id': 1", representation)
        self.assertIn("'age_range': '18-25'", representation)
        self.assertIn("'confidence': 0.95", representation)


class TestMovementConcreteClass(unittest.TestCase):

    def setUp(self):
        # Ornek veri ile sinifin baslangic durumunu ayarla
        self.movement_instance = Movement(person_id=1, movement_type='walk', start_time=datetime.now(), end_time=datetime.now())

    def test_initialization_with_kwargs(self):
        # Keyword argumanlari ile baslangic durumunu kontrol et
        self.assertEqual(self.movement_instance.person_id, 1)
        self.assertEqual(self.movement_instance.movement_type, 'walk')
        self.assertIsInstance(self.movement_instance.start_time, datetime)
        self.assertIsInstance(self.movement_instance.end_time, datetime)
        self.assertIsInstance(self.movement_instance.createdAt, datetime)
        self.assertIsInstance(self.movement_instance.updatedAt, datetime)

    def test_id_property(self):
        # id ozelliginin setter ve getter metodlarini kontrol et
        self.movement_instance.id = 10
        self.assertEqual(self.movement_instance.id, 10)

    def test_person_id_property(self):
        # person_id ozelliginin setter ve getter metodlarini kontrol et
        self.movement_instance.person_id = 5
        self.assertEqual(self.movement_instance.person_id, 5)

    def test_movement_type_property(self):
        # movement_type ozelliginin setter ve getter metodlarini kontrol et
        self.movement_instance.movement_type = 'run'
        self.assertEqual(self.movement_instance.movement_type, 'run')

    def test_start_time_property(self):
        # start_time ozelliginin setter ve getter metodlarini kontrol et
        new_start_time = datetime(2024, 1, 1, 12, 0)
        self.movement_instance.start_time = new_start_time
        self.assertEqual(self.movement_instance.start_time, new_start_time)

    def test_end_time_property(self):
        # end_time ozelliginin setter ve getter metodlarini kontrol et
        new_end_time = datetime(2024, 1, 1, 13, 0)
        self.movement_instance.end_time = new_end_time
        self.assertEqual(self.movement_instance.end_time, new_end_time)

    def test_created_at_property(self):
        # createdAt ozelliginin setter ve getter metodlarini kontrol et
        new_date = datetime(2024, 1, 1)
        self.movement_instance.createdAt = new_date
        self.assertEqual(self.movement_instance.createdAt, new_date)

    def test_updated_at_property(self):
        # updatedAt ozelliginin setter ve getter metodlarini kontrol et
        new_date = datetime(2024, 1, 2)
        self.movement_instance.updatedAt = new_date
        self.assertEqual(self.movement_instance.updatedAt, new_date)

    def test_repr(self):
        # __repr__ metodunun dogru calistigini kontrol et
        representation = repr(self.movement_instance)
        self.assertIn("'person_id': 1", representation)
        self.assertIn("'movement_type': 'walk'", representation)