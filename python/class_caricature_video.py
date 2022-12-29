"""class_video_caricature.py"""
from class_config import Config

cfg = Config()

class CaricatureVideo():
	"""Procesa video"""
	def __init__(self,file__):
		"""Inicializa"""
		self.file_ = file__
		print(f"Loading in : {cfg.get_par('src_dir')}")
		print(f"Transform to caricature : {file__}")

	def _log(self,var):
		"""function _log"""
		print(f"CaricatureVideo:{var}")

	def procesa_video(self):
		"""function """
		out_ = "ok"
		return out_
