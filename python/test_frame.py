"""test_frame.py"""
from class_caricature_frame import CaricatureFrame
from class_config import Config

cfg = Config()
v = CaricatureFrame(f"{cfg.get_par('src_dir')}WIN_20221229_16_43_00_Pro.jpg")