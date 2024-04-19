"""test_frame.py"""
from class_caricature_frame import CaricatureFrame
from class_config import Config
import cv2
import numpy as np

#cfg = Config()
#cfg.set_par('src_dir',)
#cfg.set_par('car_dir',)

src = 'C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura/'
car = 'C:/RSILVA_BASIC_BOTS/TEST_IMAGENES_caticatura/demos/'

def test1():
    foto = f"caricatura_2.jpg"
    v = CaricatureFrame(src,foto,car)

def test2():
	# Cargar la imagen
	img = cv2.imread(f"{src}caricatura_5.jpg")

	# Convertir la imagen a un espacio de color HSV
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Definir el rango de tonos de piel
	lower_skin = (0, 20, 70)
	upper_skin = (20, 255, 255)

	# Crear una máscara para seleccionar solo los tonos de piel
	skin_mask = cv2.inRange(img_hsv, lower_skin, upper_skin)

	# Crear una imagen en blanco y negro con solo los tonos de piel seleccionados
	skin_img = cv2.bitwise_and(img, img, mask=skin_mask)

	# Cambiar el color de la piel a un tono deseado
	skin_img[np.where((skin_img==[0,0,0]).all(axis=2))] = [255, 0, 0] # rojo

	# Guardar la imagen resultante
	cv2.imwrite("tu_imagen_con_color_de_piel_cambiado.jpg", skin_img)

def test3():

	# Cargar la imagen
	img = cv2.imread(f"{src}caricatura_5.jpg")

	# Convertir la imagen a un espacio de color HSV
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Definir el rango de tonos de piel
	lower_skin = (0, 20, 70)
	upper_skin = (20, 255, 255)

	# Crear una máscara para seleccionar solo los tonos de piel
	skin_mask = cv2.inRange(img_hsv, lower_skin, upper_skin)

	# Aplicar un suavizado gaussiano para suavizar la máscara
	skin_mask = cv2.GaussianBlur(skin_mask, (3, 3), 0)

	# Crear una imagen en blanco y negro con solo los tonos de piel seleccionados
	skin_img = cv2.bitwise_and(img, img, mask=skin_mask)

	# Calcular el histograma de color para los tonos de piel seleccionados
	skin_hist = cv2.calcHist([skin_img], [0], skin_mask, [256], [0, 256])

	# Normalizar el histograma
	skin_hist = skin_hist / skin_hist.sum()

	# Calcular el histograma cumulativo para los tonos de piel
	skin_cdf = np.cumsum(skin_hist)

	# Calcular el límite superior para los tonos de piel
	skin_limit = skin_cdf[-2]

	# Crear una imagen de salida
	output_img = img.copy()

	# Recorrer cada pixel de la imagen de salida
	for i in range(output_img.shape[0]):
	    for j in range(output_img.shape[1]):
	        # Si el pixel está dentro del rango de tonos de piel
	        if skin_mask[i, j] == 255:
	            # Si el valor del pixel en el canal H es menor que el límite superior
	            if output_img[i, j, 0] < skin_limit * 255:
	                # Cambiar el color del pixel a un tono deseado
	                output_img[i, j] = (0, 0, 255) # rojo

	# Guardar la imagen resultante
	cv2.imwrite("imagen_modificada.jpg", output_img)





def test4():

	# Cargar imagen
	img = cv2.imread(f"{src}caricatura_5.jpg")

	# Definir límites para tonos de piel
	lower_skin = np.array([0, 20, 70], dtype=np.uint8)
	upper_skin = np.array([20, 255, 255], dtype=np.uint8)

	# Convertir imagen a espacio de color HSV
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Aplicar límites para tonos de piel
	skin_mask = cv2.inRange(hsv_img, lower_skin, upper_skin)

	# Crear imagen de salida
	output_img = img.copy()

	# Recorrer pixeles de imagen
	for i in range(img.shape[0]):
	    for j in range(img.shape[1]):
	        # Si el pixel se encuentra dentro de los límites de tonos de piel
	        if skin_mask[i, j] != 0:
	            # No hacer cambio de color
	            output_img[i, j] = img[i, j]

	# Mostrar imagen de salida
	#cv2.imshow("Skin Color Detection", output_img)
	cv2.imwrite("imagen_modificada.jpg", output_img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()



# Cargar imagen
img = cv2.imread(f"{src}caricatura_5.jpg")


# Convertir imagen a espacio de color HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convertir imagen a formato de datos para K-means
img_data = hsv_img.reshape((-1, 3))
img_data = np.float32(img_data)

# Define el número de clusters y aplicar K-means
k = 5
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, labels, colors = cv2.kmeans(img_data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Crear imagen de salida
output_img = img.copy()

# Recorrer pixeles de imagen
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        # Asignar el nuevo tono de piel según el cluster al que pertenece el pixel
        output_img[i, j] = colors[labels[i*img.shape[1] + j]].astype(np.uint8)

# Mostrar imagen de salida

cv2.imwrite("imagen_modificada.jpg", output_img)
