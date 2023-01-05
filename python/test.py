from class_config import Config
from class_caricature_frame import CaricatureFrame

cfg = Config()

import cv2

# Abrir el video
ruta_src = cfg.get_par('src_dir')
ruta_out = cfg.get_par('out_dir')
ruta_car = cfg.get_par('car_dir')
#C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura

#foto = f"{ruta}woman2.jpeg"
video_src = f"{ruta_src}2022-12-31 08-07-05.mp4"



video = cv2.VideoCapture(video_src)

# Contar el número total de frames en el video
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Iterar sobre cada frame del video
for i in range(total_frames):
    # Leer el frame actual
    print(f"Procesando frame: {i}")
    _, frame = video.read()
    str_i = str(i).rjust(5, '0')
    # Guardar el frame como una imagen
    file_out = f"{ruta_out}frame{str_i}.jpg"
    file_name = f"frame{str_i}.jpg"
    cv2.imwrite(file_out, frame)
    v = CaricatureFrame(file_name)

# Cerrar el video
video.release()

import cv2
import os

# Crear el objeto de escritura de video
#fourcc = cv2.VideoWriter_fourcc(*"X264")#H264  # X264
fourcc = cv2.VideoWriter_fourcc(*'XVID')

video_out = cv2.VideoWriter("video_car.mkv", fourcc, 20.0, (1280, 720))

#extension of file = test.mkv
#codec . = CV_FOURCC(*'X264)

#fourcc = cv.VideoWriter_fourcc(*'XVID')
#out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

#instalar https://www.divx.com/ #no funciona
# Instalar codec: https://www.winxdvd.com/convertidor-de-video-es/hevc-codec.htm #

# o https://github.com/cisco/openh264/releases
#Failed to load OpenH264 library: openh264-1.8.0-win64.dll

#how to: https://stackoverflow.com/questions/57312811/anaconda-cannot-find-openh264-library
#http://ciscobinary.openh264.org/openh264-1.8.0-win64.dll.bz2

# Iterar sobre las imágenes en la carpeta "frames"
for file in os.listdir(ruta_car):
    # Leer la imagen
    frame = cv2.imread(ruta_car + file)

    # Añadir la imagen al video
    video_out.write(frame)

# Cerrar el video
video_out.release()
