"""test_video.py"""
from class_caricature_video import CaricatureVideo
from class_config import Config

cfg = Config()
v = CaricatureVideo(f"{cfg.get_par('src_dir')}WIN_20221229_16_42_51_Pro.mp4")