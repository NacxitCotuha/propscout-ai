import cv2
from ultralytics import YOLO

def main():
    # Cargamos el modelo nano (se descargará automáticamente la primera vez)
    model = YOLO("yolov8n.pt")

    # Abrir la cámara web (0 suele ser la integrada, 1 o 2 si es externa)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return

    print("Presiona 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Realizar detección
        # stream=True ayuda a que sea más fluido
        results = model(frame, stream=True)

        for r in results:
            # Dibujar los cuadros de detección en el frame
            annotated_frame = r.plot()
            cv2.imshow("PropScout AI - Prueba de Cámara", annotated_frame)

        # Salir si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()