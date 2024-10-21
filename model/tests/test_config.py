import unittest
from config import Config, Preset

class TestConfig(unittest.TestCase):
    def setUp(self):
        # Config sinifi ornegini olusturma
        self.config = Config()

    def test_config_loading(self):
        """Config sinifinin dogru bir sekilde yuklenip yuklenmedigini test et"""
        self.assertIsInstance(self.config, Config)

    def test_network_settings(self):
        """Ag ayarlarinin dogru bir sekilde yuklenip yuklenmedigini test et"""
        self.assertIn('host', self.config.setting.network.__dict__)
        self.assertIn('port', self.config.setting.network.__dict__)

    def test_model_settings(self):
        """Model ayarlarinin dogru bir sekilde yuklenip yuklenmedigini test et"""
        self.assertIn('name', self.config.setting.model.__dict__)
        self.assertIn('type', self.config.setting.model.__dict__)

    def test_debug_settings(self):
        """Debug ayarlarinin dogru bir sekilde yuklenip yuklenmedigini test et"""
        self.assertIn('debug', self.config.setting.__dict__)

    def test_device_settings(self):
        """Cihaz ayarlarinin dogru bir sekilde yuklenip yuklenmedigini test et"""
        self.assertEqual(self.config.setting.device, 'gpu')

    def test_processing_settings(self):
        """Islem ayarlarinin dogru bir sekilde yuklenip yuklenmedigini test et"""
        self.assertIn('source', self.config.setting.processing.__dict__)

class TestPreset(unittest.TestCase):
    def setUp(self):
        # Preset sinifi ornegini olusturma
        self.preset = Preset()

    def test_preset_file_paths(self):
        """Preset icindeki dosya yollarinin dogru ayarlanip ayarlanmadigini test et"""
        self.assertEqual(self.preset.file.config, 'config.json')

    def test_preset_folder_paths(self):
        """Preset icindeki klasor yollarinin dogru ayarlanip ayarlanmadigini test et"""
        self.assertEqual(self.preset.folder.config, 'config/json')

    def test_preset_response_types(self):
        """Preset icindeki yanit tiplerinin dogru ayarlanip ayarlanmadigini test et"""
        self.assertIn('info', self.preset.preset['response_types'])

    def test_preset_additional_folders(self):
        """Preset icindeki ek klasor yollarinin dogru ayarlanip ayarlanmadigini test et"""
        self.assertIn('log', self.preset.folder.__dict__)



