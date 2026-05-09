import cv2
import os
import time

def main():
    # Crear carpeta si no existe
    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    print("Capturador de Datos iniciado. Presiona 'S' para guardar foto, 'Q' para salir.")

    while True:
        ret, frame = cap.read()
        cv2.imshow("Recolector de Datos", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            filename = f"{output_dir}/img_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Foto guardada: {filename}")
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()