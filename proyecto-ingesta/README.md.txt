Proyecto de Ingesta y Procesamiento de Ventas

Este proyecto automatiza la gestión de datos de ventas desde su origen hasta su procesamiento final, asegurando la trazabilidad de cada paso.

Descripción
El sistema realiza dos funciones principales:

Ingesta: Mueve el archivo ventas.csv de la carpeta origen/ a data/raw/ para mantener un histórico de datos crudos.

Carga y Procesamiento: Lee los datos desde data/raw/, calcula el total de ventas (Cantidad × Precio), registra el proceso en una bitácora (logs) y guarda el resultado limpio en data/processed/.

Requisitos
Python 3.x

Librería pandas (pip install pandas)

Estructura del Proyecto
proyecto-ingesta/
 ├── origen/              # Coloca aquí tus archivos nuevos (.csv)
 ├── data/
 │    ├── raw/            # Datos originales (respaldos)
 │    └── processed/      # Resultados finales procesados
 ├── ingesta.py           # Script para mover/ingestar datos
 ├── carga.py             # Script para procesar y calcular datos
 └── README.md            # Este archivo


Instrucciones de Ejecución
Coloca tu archivo ventas.csv en la carpeta origen/.

Abre una terminal en la carpeta del proyecto y ejecuta:

DOS
python ingesta.py
Luego, ejecuta el procesamiento:

DOS
python carga.py
Los resultados estarán disponibles en data/processed/ventas_procesadas.csv