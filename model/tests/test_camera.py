import unittest
from model import Camera
from datetime import datetime

class TestCamera(unittest.TestCase):

    def test_constructor(self):
        camera = Camera(id=1, label='Test Camera')
        self.assertEqual(camera.id, 1)
        self.assertEqual(camera.label, 'Test Camera')

    def test_setters_and_getters(self):
        camera = Camera()
        camera.id = 2
        camera.label = 'Updated Camera'
        self.assertEqual(camera.id, 2)
        self.assertEqual(camera.label, 'Updated Camera')

    def test_to_json(self):
        camera = Camera(id=3, label='JSON Camera')
        json_data = camera.to_json()
        self.assertEqual(json_data['id'], 3)
        self.assertEqual(json_data['label'], 'JSON Camera')

    def test_from_json(self):
        camera = Camera()
        json_data = {'id': 4, 'label': 'From JSON'}
        camera.from_json(json_data)
        self.assertEqual(camera.id, 4)
        self.assertEqual(camera.label, 'From JSON')

    def test_repr(self):
        camera = Camera(id=5, label='Repr Test')
        self.assertIn("'id': 5", repr(camera))
        self.assertIn("'label': 'Repr Test'", repr(camera))

    def test_str(self):
        camera = Camera(id=6, label='Str Test')
        self.assertIn("'id': 6", str(camera))
        self.assertIn("'label': 'Str Test'", str(camera))
