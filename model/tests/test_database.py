import unittest
import os
from database import SQLiteConnector


class TestSQLiteConnector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Test için geçici bir veritabanı oluştur
        cls.database_path = 'temp_test.db'
        cls.connector = SQLiteConnector(database_path=cls.database_path)

    def setUp(self):
        # Her test öncesi veritabanı bağlantısını başlat
        self.connector.connect()

    def test_connection(self):
        """Veritabanı bağlantısının başarılı olduğunu test et"""
        self.assertIsNotNone(self.connector.connection)

    def test_insert(self):
        """Veritabanına kayıt ekleme işleminin başarılı olduğunu test et"""
        data = {'name': 'Test Name', 'value': 'Test Value'}
        self.connector.insert(data)
        # Ekleme sonrası veriyi kontrol et
        result = self.connector.select({'name': 'Test Name'})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Test Name')  # Sütun index'ine göre erişim


    def test_update(self):
        """Veritabanında güncelleme işleminin başarılı olduğunu test et"""
        self.connector.update({'name': 'Test Name'}, {'value': 'Updated Value'})
        # Güncelleme sonrası veriyi kontrol et
        result = self.connector.select({'name': 'Test Name'})
        self.assertEqual(result[0][2], 'Updated Value')  # 'value' sütunu için index 2

    def test_delete(self):
        """Veritabanından kayıt silme işleminin başarılı olduğunu test et"""
        self.connector.delete({'name': 'Test Name'})
        # Silme sonrası veriyi kontrol et
        result = self.connector.select({'name': 'Test Name'})
        self.assertEqual(len(result), 0)

    def test_select(self):
        """Veritabanından kayıt seçme işleminin başarılı olduğunu test et"""
        # Önce test verisi ekleyelim
        self.connector.insert({'name': 'Another Test', 'value': 'Another Value'})
        # Seçme işlemini kontrol et
        result = self.connector.select({'name': 'Another Test'})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'Another Test')  # 'name' sütunu için index 1


    def tearDown(self):
        # Her test sonrası veritabanı bağlantısını kapat
        self.connector.close()

    @classmethod
    def tearDownClass(cls):
        # Testler bittikten sonra geçici veritabanını sil
        os.remove(cls.database_path)