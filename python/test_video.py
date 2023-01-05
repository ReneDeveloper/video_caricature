"""test_video.py"""
from class_caricature_video import CaricatureVideo
from class_config import Config

cfg = Config()
cfg.set_par('src_dir','C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura/')

v = CaricatureVideo(f"WIN_20221229_21_44_29_Pro.mp4")
#v = CaricatureVideo(f"2022-12-31 08-07-05_car.mkv")
#v = CaricatureVideo(f"2022-12-31 08-07-05_car_car.mkv")


