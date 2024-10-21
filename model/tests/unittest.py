import os
from test import  preset

class Config:
    def __init__(self):
        self.preset = preset
        
    def __repr__(self) -> str:
        pass
    
    def get_config_path(self):
        return os.path.join(preset.folder.config, preset.file.config)
    
    def read_preset(self):
        return self.preset