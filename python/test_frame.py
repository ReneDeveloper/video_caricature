"""test_frame.py"""
from class_caricature_frame import CaricatureFrame
from class_config import Config

#cfg = Config()
#cfg.set_par('src_dir',)
#cfg.set_par('car_dir',)
src = 'C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura/'
car = 'C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura/demos/'
foto = f"caricatura_2.jpg"
v = CaricatureFrame(src,foto,car)

