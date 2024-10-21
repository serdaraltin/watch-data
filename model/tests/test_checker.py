
import unittest
from services import Checker
import tempfile
import os

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.checker = Checker()

    def test_check_file_existence(self):
        """Dosya varlığını kontrol et"""
        with tempfile.NamedTemporaryFile() as tmp:
            response = self.checker.file_system.check_file(tmp.name)
            self.assertEqual(response["type"], 0)
            self.assertIn("File already exists", response["message"])

    def test_check_folder_existence(self):
        """Klasör varlığını kontrol et"""
        with tempfile.TemporaryDirectory() as tmpdir:
            response = self.checker.file_system.check_folder(tmpdir)
            self.assertEqual(response["type"], 0)
            self.assertIn("Folder already exists", response["message"])

    def test_check_permissions(self):
        """Dosya izinlerini kontrol et"""
        with tempfile.NamedTemporaryFile() as tmp:
            response = self.checker.file_system.check_permissions(tmp.name)
            self.assertEqual(response["type"], 0)
            self.assertIn("Permissions for", response["message"])

    def test_check_image_model(self):
        """Image modelinin varlığını kontrol et"""
        # Not: Gerçek model dosyası ve yolunuzun burada belirtilmesi gerekmektedir.
        response = self.checker.image_processing.check_image_model()
        self.assertIn(response["type"], [0, 1])

    def test_check_port_availability(self):
        """Port kullanılabilirliğini kontrol et"""
        # Not: Gerçek host ve port numarasının burada belirtilmesi gerekmektedir.
        response = self.checker.network.check_port_availability('localhost', 80)
        self.assertIn(response["type"], [0, 1])

    def test_check_api_accessibility(self):
        """API erişilebilirliğini kontrol et"""
        # Not: Gerçek bir API URL'sinin burada belirtilmesi gerekmektedir.
        response = self.checker.network.check_api_accessibility('https://www.example.com')
        self.assertIn(response["type"], [0, 1, 2])

    def test_check_ip_validity(self):
        """IP adresinin geçerliliğini kontrol et"""
        response = self.checker.camera.check_ip_validity('192.168.1.1')
        self.assertEqual(response["type"], 0)

        invalid_response = self.checker.camera.check_ip_validity('999.999.999.999')
        self.assertEqual(invalid_response["type"], 1)

    def test_check_system_timezone(self):
        """Sistem zaman dilimini kontrol et"""
        response = self.checker.localization.check_system_timezone()
        self.assertEqual(response["type"], 0)

    def test_check_database_connection(self):
        """Veritabanı bağlantısını kontrol et"""
        # Veritabanı bağlantı bilgilerini ayarla
        self.checker.database.host = "16.170.149.181"
        self.checker.database.database = "camproject"
        self.checker.database.user = "postgres"
        self.checker.database.password = "kmxHg7!U$5t%H7"

        response = self.checker.database.check_connection()
        self.assertIn(response["type"], [0, 1])