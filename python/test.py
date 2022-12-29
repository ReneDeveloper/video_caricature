from class_config import Config

cfg = Config()

import cv2

# Abrir el video
ruta = cfg.get_par('src_dir')
#C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura

#foto = f"{ruta}woman2.jpeg"
video_src = f"{ruta}WIN_20221229_18_25_38_Pro.mp4"

video = cv2.VideoCapture(video_src)

# Contar el número total de frames en el video
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Iterar sobre cada frame del video
for i in range(total_frames):
    # Leer el frame actual
    print(f"Procesando frame: {i}")
    _, frame = video.read()

    # Guardar el frame como una imagen
    cv2.imwrite(f"{ruta}/frame{i}.png", frame)

# Cerrar el video
video.release()

