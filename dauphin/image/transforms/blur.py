from PIL import ImageFilter

from dauphin.image.transforms.transform import DauphinTransform


class Blur(DauphinTransform):
    def __init__(self, name=None, prob=1.0, level=0):
        super().__init__(name, prob, level)

    def transform(self, pil_img, label, **kwargs):
        return pil_img.filter(ImageFilter.BLUR), label
