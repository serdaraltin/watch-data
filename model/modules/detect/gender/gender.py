import torch
import torchvision.transforms as transforms
from torch.autograd import Variable

from PIL import Image

from lib.baseline.model.DeepMAR import DeepMAR_ResNet50
from lib.baseline.utils.utils import load_state_dict
from config.config_manager import config
import os
from services.logging.logger import custom_logger

class PredGender():

    def __init__(self) -> None:
        try:
            model_name, model_type = config.setting.model.detect["gender"].values()

            custom_config = {
                "model": {
                    "resize": (224, 224),
                    "model_kwargs": {"last_conv_stride": 2, "num_att": 26},
                },
                "utils": {
                    "model_weight_file": os.path.join("modules/detect/gender/model", f"{model_name}.{model_type}"),
                },
                "load_model_weight": True,
                "mean": [0.485, 0.456, 0.406],
                "std": [0.229, 0.224, 0.225],
            }

            # dataset
            normalize = transforms.Normalize(mean=custom_config["mean"], std=custom_config["std"])
            self.test_transform = transforms.Compose(
                [
                    transforms.Resize(custom_config["model"]["resize"]),
                    transforms.ToTensor(),
                    normalize,
                ]
            )

            self.model = DeepMAR_ResNet50(**custom_config["model"]["model_kwargs"])

            if custom_config["load_model_weight"]:
                map_location = lambda storage, loc: storage
                ckpt = torch.load(custom_config["utils"]["model_weight_file"], map_location=map_location)
                self.model.load_state_dict(ckpt["state_dicts"][0])

            self.model.cuda()
            self.model.eval()

            custom_logger.info("Gender prediction model initialized successfully.")
        except Exception as e:
            custom_logger.error("Failed to initialize gender prediction model", exc_info=True)

    def predictions(self, frame, x1, y1, x2, y2):
        try:
            img = frame[y1:y2, x1:x2]
            pil_image = Image.fromarray(img)
            img_trans = self.test_transform(pil_image)
            img_trans = torch.unsqueeze(img_trans, dim=0)
            img_var = Variable(img_trans).cuda()
            # Make predictions
            score = self.model(img_var).data.cpu().numpy()
            gender_pred = "female" if score[0, 0] > 0.0 else "male"

            custom_logger.info(f"Gender prediction successful.\nFrame points: x1, y1, x2, y2 = {x1}, {y1}, {x2}, {y2}\n\n", exc_info=True)
            return gender_pred
        except Exception as e:
            custom_logger.error("Failed to make gender prediction", exc_info=True)
            return None