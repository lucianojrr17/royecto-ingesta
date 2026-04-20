import shutil
import logging
import os
import pandas as pd

# Configurar logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ejecutar_ingesta():
    # Asegúrate de que este archivo exista en tu carpeta 'origen'
    origen = "origen/ventas.csv" 
    destino = "data/raw/ventas.csv"
    
    logging.info("Iniciando proceso de ingesta...")
    
    try:
        # Crear carpetas si no existen
        os.makedirs("data/raw", exist_ok=True)
        
        # Copiar el archivo
        shutil.copy(origen, destino)
        
        # Leer el archivo copiado para contar registros (Trazabilidad)
        df = pd.read_csv(destino)
        logging.info(f"Éxito: Archivo copiado. Total de registros: {len(df)}")
        
    except Exception as e:
        logging.error(f"Error en la ingesta: {e}")

if __name__ == "__main__":
    ejecutar_ingesta()