"""class_frame_caricature.py"""
from class_config import Config

cfg = Config()

class CaricatureFrame():
	"""Procesa video"""
	def __init__(self,file__):
		"""Inicializa"""
		self.file_ = file__
		self._log(f"Loading in : {cfg.get_par('src_dir')}")
		self._log(f"Transform to caricature : {file__}")
		self.procesa_frame()

	def _log(self,var):
		"""function _log"""
		print(f"CaricatureFrame:{var}")

	def procesa_frame(self):
		"""function """
		out_ = "ok"
		return out_