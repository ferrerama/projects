import os

def encontrar_archivos(nombre_parcial):
    archivos_encontrados = []
    directorio_raiz = "C:\\"
    nombre_parcial_lower = nombre_parcial.lower()
    for ruta_actual, directorios, archivos in os.walk(directorio_raiz):
        for archivo in archivos:
            if nombre_parcial_lower in archivo.lower():
                ruta_completa = os.path.join(ruta_actual, archivo)
                archivos_encontrados.append(ruta_completa)              
    return archivos_encontrados

if __name__ == "__main__":
    nombre_a_buscar = "onedrive.exe"   
    print(f"Buscando archivos que contienen '{nombre_a_buscar}' en todo el PC. Esto puede tardar unos minutos...")
    resultados = encontrar_archivos(nombre_a_buscar)

    if resultados:
        print("\nArchivos encontrados:")
        for archivo in resultados:
            print(f"- {archivo}")
    else:
        print(f"\nNo se encontraron archivos que contengan '{nombre_a_buscar}'.")