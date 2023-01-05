"""class_video_caricature.py"""
import os
import cv2
from class_config import Config
from class_caricature_frame import CaricatureFrame

cfg = Config()

class CaricatureVideo():
    """Procesa video"""
    def __init__(self,file__):
        """Inicializa"""
        self.file_ = file__
        print(f"Loading in : {cfg.get_par('src_dir')}")
        print(f"Transform to caricature : {file__}")
        self.generar_frame = cfg.get_par('generar_frame')
        self.procesa_video()

    def _log(self,var):
        """function _log"""
        print(f"CaricatureVideo:{var}")

    def create_dirs(self):
        """function _log"""
        if self.generar_frame:

            self._log(f"create_dirs:INICIO")
            out_file_folder = f'{self.file_}_out_folder' # to save video frame
            car_file_folder = f'{self.file_}_car_folder' # to save caricature frame
            self._log(f"create_dir:out_file_folder:{out_file_folder}")
            self._log(f"create_dir:car_file_folder:{car_file_folder}")
                        
            f1 = f"{cfg.get_par('src_dir')}{out_file_folder}"
            f2 = f"{cfg.get_par('src_dir')}{car_file_folder}"
            if os.path.exists(f1):
                print("El directorio existe")
            else:
                print("El directorio no existe")
                os.makedirs(f1)
                os.makedirs(f2)

            self._log(f"create_dirs:f1:CORRECTO:{f1}")
            #self._log(f"create_dirs:car_file_folder:CORRECTO:{car_file_folder}")

    def procesa_video(self):
        """function """
        out_ = "ok"
        self._log(f'DEBUG:procesa_video:{self.file_}')
        # Abrir el video
        ruta_src = cfg.get_par('src_dir')
        ruta_out = cfg.get_par('out_dir')
        ruta_car = cfg.get_par('car_dir')
        #C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura

        #foto = f"{ruta}woman2.jpeg"
        video_src = f"{ruta_src}{self.file_}"
        self._log(f'DEBUG:video_src:{video_src}')

        if self.generar_frame:
            self._log("generar frame")
            self.create_dirs()

        self._log(f'ARMAR EL VIDEO DESDE:{video_src}')
        video = cv2.VideoCapture(video_src)

        # Contar el número total de frames en el video
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        self._log(f'TOTAL FRAMES:{total_frames}')

        # Iterar sobre cada frame del video
        for i in range(total_frames):
            # Leer el frame actual
            self._log(f"DEBUG_VIDEO:Procesando frame: {i}")
            _, frame = video.read()
            str_i = str(i).rjust(5, '0')

            # Guardar el frame como una imagen
            file_name = f"frame{str_i}.jpg"
            ruta_out__ = f'{ruta_src}{self.file_}_out_folder/'
            self._log(f"DEBUG_VIDEO:file_out:{ruta_out__}")

            if self.generar_frame:
                self._log(f"Generar frame:{file_name}")
                self._log(f"Generar frame:en:{ruta_out__}")
                
                cv2.imwrite(f'{ruta_out__}{file_name}', frame)
                src_frame = f'{ruta_src}{self.file_}_out_folder/'
                car_frame = f'{ruta_src}{self.file_}_car_folder/'
                v = CaricatureFrame(src_frame,file_name,car_frame)

        # Cerrar el video
        video.release()

        # Crear el objeto de escritura de video
        #fourcc = cv2.VideoWriter_fourcc(*"X264")#H264  # X264
        fourcc = cv2.VideoWriter_fourcc(*'XVID')#"X264")#H264  # X264
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
        self._log(f'ARMAR EL VIDEO:{ruta_src}{self.file_}_car_folder/')
        src_car = f'{ruta_src}{self.file_}_car_folder/'
        for file in os.listdir(src_car):
            # Leer la imagen
            frame = cv2.imread(src_car + file)

            # Añadir la imagen al video
            video_out.write(frame)

        # Cerrar el video
        video_out.release()
        return out_
