"""class_frame_caricature.py"""

from argparse import ArgumentParser
import cv2
import numpy as np
from matplotlib import pylab as pyl
from class_config import Config

cfg = Config()

class CaricatureFrame():
    """Procesa video"""
    def __init__(self,src__,file__,car__):
        """Inicializa"""
        self.src__ = src__
        self.file_ = file__
        self.car__ = car__

        if self.src__==None:
            self.src__ = cfg.get_par('src_dir')

        if self.car__==None:
            self.car__ = self.src__

        self._log(f"Loading in : {self.src__}")

        self._log(f"Transform to caricature : {file__}")
        self.procesa_frame()

    def _log(self,var):
        """function _log"""
        print(f"CaricatureFrame:{var}")

    def procesa_frame(self):
        """function """
        out_ = "ok"
        # imports

        # pasar del filtro bilateral
        BI_LATERAL_FILTER_STEPS = 2#40 works

        # pasar downsampling y upsampling
        DOWNSAMPLING_UPSAMPLING_STEPS = 2

        # ruta de la imagen.
        foto = f"{self.src__}{self.file_}"
        self._log(f"Abrir la foto:{foto}")
        image = pyl.imread(foto)

        # ancho y alto.
        width, height = image.shape[:2]

        # modificando la copia.
        copia = np.copy(image)

        # Primero, reducimos tamanio para operaciones mas rapidas.
        for _ in range(DOWNSAMPLING_UPSAMPLING_STEPS):
            copia = cv2.pyrDown(copia)

        # filtro bi lateral : difuminando detalles de  imagen -->BI_LATERAL_FILTER_STEPS

        for _ in range(BI_LATERAL_FILTER_STEPS):
            copia = cv2.bilateralFilter(copia, d=9, sigmaColor=.1, sigmaSpace=.01)

        # Restauramos la imagen a su tamanio original.
        for _ in range(DOWNSAMPLING_UPSAMPLING_STEPS):
            copia = cv2.pyrUp(copia)

        # Convertimos la imagen original en escala de grises, y la difuminamos.
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        blur = cv2.medianBlur(gray, 7)

        # Detectamos y realzamos los bordes de la imagen.
        edges = cv2.adaptiveThreshold((255 * blur).astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                        blockSize=9, C=2)
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

        # La imagen caricaturizada sera la combinacion de la imagen difuminada con los bordes realzados en el paso anterior.
        cartoonized_image = cv2.bitwise_and(copia, edges)

        # Dibujamos la imagen original junto con su caricatura.
        fig = pyl.figure(figsize=(20, 10))
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=.05, wspace=.05)

        for i, title, img in zip(range(1, 3), ['Original', 'Caricatura'], [image, cartoonized_image]):
            pyl.subplot(120 + i)
            pyl.imshow(img)
            pyl.axis('off')
            pyl.title(title, size=20)

        #pyl.show()
        # Guardamos la imagen
        generar_frame = cfg.get_par('generar_frame')
        if generar_frame:
            #ruta_car = cfg.get_par('car_dir')
            name_car = f"__caricature__{self.file_}"
            cv2.imwrite(f'{self.car__}{name_car}', cartoonized_image)
            self._log(f"guardar la cartoonized_image:{self.car__}{name_car}")

        return out_