import os
import pandas as pd
import logging

# Configuración de trazabilidad
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def procesar_datos():
    ruta_archivo = "data/raw/ventas.csv"
    
    # Registro de inicio
    logging.info("Iniciando proceso de carga...")
    
    try:
        # Intentar leer el archivo
        df = pd.read_csv(ruta_archivo)
        
        # Registrar cantidad de registros
        cantidad = len(df)
        logging.info(f"Éxito: Archivo cargado. Total de registros: {cantidad}")
        
        # Procesamiento: Calcular total
        df['total'] = df['cantidad'] * df['precio']
        resultado = df['total'].sum()
        
        # Registrar resultado
        logging.info(f"Procesamiento exitoso. El total de ventas es: {resultado}")
        
        # Guardar en carpeta processed
        os.makedirs("data/processed", exist_ok=True)
        df.to_csv("data/processed/ventas_procesadas.csv", index=False)
        logging.info("Archivo procesado guardado en data/processed/ventas_procesadas.csv")
        
    except Exception as e:
        # Registro de error
        logging.error(f"Error durante el proceso: {e}")

if __name__ == "__main__":
    procesar_datos()