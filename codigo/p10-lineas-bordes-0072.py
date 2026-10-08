# catherine eileen huerta rascon NC = 0072
import cv2
import numpy as np

# Cargar imagen
imagen = cv2.imread("pulpo.jpg")

# Verificar que la imagen exista
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes
bordes = cv2.Canny(gris, 50, 150)

# Detectar líneas mediante Hough
lineas = cv2.HoughLinesP(
    bordes,
    1,
    np.pi / 180,
    threshold=50,
    minLineLength=50,
    maxLineGap=10
)

# Crear copia de la imagen
resultado = imagen.copy()

# Dibujar líneas
if lineas is not None:
    # Reformatear la matriz a un arreglo 2D de forma (N, 4)
    lineas_planas = lineas.reshape(-1, 4)
    
    for x1, y1, x2, y2 in lineas_planas:
        cv2.line(
            resultado,
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            (0, 0, 255),
            2
        )

# Mostrar resultados
cv2.imshow("Imagen original del pulpo", imagen)
cv2.imshow("Bordes del pulpo", bordes)
cv2.imshow("Lineas detectadas", resultado)

# Guardar resultado en el archivo correcto
cv2.imwrite(
    "resultadopulpo_lineas.jpg",
    resultado
)

print("Deteccion de lineas terminada.")

if lineas is not None:
    print("Cantidad de segmentos detectados:", len(lineas))
else:
    print("No se detectaron lineas.")

print("Resultado guardado en:")
print("resultadopulpo_lineas.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("catherine eileen huerta rascon NC = 0072")