import cv2
import os
import glob

def main():
    input_path = "data/importar/*.jpg" # Donde pones tus fotos crudas
    output_path = "data/raw/"
    os.makedirs(output_path, exist_ok=True)

    fotos = glob.glob(input_path)
    print(f"Se encontraron {len(fotos)} fotos para procesar.")

    for i, foto_path in enumerate(fotos):
        img = cv2.imread(foto_path)
        if img is not None:
            # Puedes redimensionarlas aquí para que YOLO las procese mejor (ej. 640x640)
            img_resized = cv2.resize(img, (640, 640))
            new_name = f"{output_path}/external_{i}.jpg"
            cv2.imwrite(new_name, img_resized)
    
    print("Proceso terminado.")

if __name__ == "__main__":
    main()