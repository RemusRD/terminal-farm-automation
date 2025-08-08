# Issue #31: Parser de datos CSV (🔴 Avanzado)

## Descripción
Implementa un parser para leer datos de mercado desde el archivo `data/prices.csv` y proporcionar análisis de precios históricos.

## Objetivos de Aprendizaje
- Lectura y escritura de archivos CSV
- Manipulación de datos tabulares
- Análisis de datos y tendencias
- Manejo de diferentes tipos de datos (fechas, números)

## Tareas Específicas

### Tarea 1: Parser CSV Básico
En `src/market.py`, implementa la función `load_price_data()`:
```python
def load_price_data(csv_file="data/prices.csv"):
    """
    Carga datos de precios desde archivo CSV.
    
    Returns:
        list: Lista de diccionarios con datos de mercado
    """
    # TODO: Implementar parser CSV
    pass
```

### Tarea 2: Análisis de Tendencias
Implementa la función `analyze_price_trends()`:
```python
def analyze_price_trends(crop_name, days=30):
    """
    Analiza tendencias de precios para un cultivo específico.
    
    Args:
        crop_name (str): Nombre del cultivo
        days (int): Número de días a analizar
    
    Returns:
        dict: Análisis con promedio, tendencia y proyección
    """
    # TODO: Calcular estadísticas de precios
    pass
```

### Tarea 3: Exportar Reportes
Implementa la función `export_market_report()`:
```python
def export_market_report(filename="reports/market_analysis.csv"):
    """
    Exporta reporte de análisis de mercado a CSV.
    
    Args:
        filename (str): Nombre del archivo de salida
    """
    # TODO: Generar y exportar reporte
    pass
```

## Criterios de Éxito
- [x] ✅ La función lee correctamente el archivo CSV
- [x] ✅ Maneja diferentes tipos de datos (fechas, precios)
- [x] ✅ Calcula estadísticas básicas (promedio, máximo, mínimo)
- [x] ✅ Identifica tendencias (subida, bajada, estable)
- [x] ✅ Exporta reportes en formato CSV

## Archivos a Modificar
- `src/market.py`
- `data/prices.csv` (usar datos existentes)

## Pistas
- Usa el módulo `csv` de Python para leer archivos
- `datetime.strptime()` para convertir fechas
- Calcula tendencias comparando precio actual vs promedio histórico
- Usa `with open()` para manejo seguro de archivos

## Nivel de Dificultad: 🔴 Avanzado
**Tiempo estimado:** 45-60 minutos

## Tecnologías y Conceptos
- Archivo I/O (entrada/salida)
- Módulo CSV
- Análisis de datos
- Manejo de fechas
- Estadísticas básicas