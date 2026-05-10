import os
import shutil

def organizar_mi_carpeta(ruta_objetivo):
    categorias = {
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Musica': ['.mp3', '.wav', '.flac'],
        'Comprimidos': ['.zip', '.rar', '.7z'],
        'Instaladores': ['.exe', '.msi', '.dmg']
    }

    for archivo in os.listdir(ruta_objetivo):
        ruta_archivo = os.path.join(ruta_objetivo, archivo)

        if os.path.isdir(ruta_archivo):
            continue

        nombre, extension = os.path.splitext(archivo)
        extension = extension.lower()

        encontrado = False
        for carpeta_destino, extensiones in categorias.items():
            if extension in extensiones:
                ruta_carpeta_destino = os.path.join(ruta_objetivo, carpeta_destino)
                if not os.path.exists(ruta_carpeta_destino):
                    os.makedirs(ruta_carpeta_destino)
                
                shutil.move(ruta_archivo, os.path.join(ruta_carpeta_destino, archivo))
                print(f"✅ Movido: {archivo} -> {carpeta_destino}")
                encontrado = True
                break
        
        if not encontrado:
            print(f"ℹ️ El archivo {archivo} no tiene una categoría definida.")

if __name__ == "__main__":
    carpeta_a_organizar = "./PruebaDesorden"
    
    if os.path.exists(carpeta_a_organizar):
        print("--- Iniciando organización ---")
        organizar_mi_carpeta(carpeta_a_organizar)
        print("--- Proceso terminado ---")
    else:
        print(f"❌ Error: La carpeta '{carpeta_a_organizar}' no existe.")
        print("Por favor, crea una carpeta llamada 'PruebaDesorden' para probar.")