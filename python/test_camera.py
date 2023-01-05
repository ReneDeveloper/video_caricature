"""test_camera.py"""


import cv2

# Abre la cámara
cap = cv2.VideoCapture(0)

# Define el codec y cree el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while True:
    # Lee el siguiente frame
    ret, frame = cap.read()

    # Si hay un frame válido, lo procesa y lo guarda
    if ret:
        # Procesa el frame
        out.write(frame)

        # Muestra el frame
        cv2.imshow('frame', frame)

    # Si se presiona la tecla 'q', termina el bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpia
cap.release()
out.release()
cv2.destroyAllWindows()