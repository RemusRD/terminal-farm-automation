# Issue #30: Cálculo de estadísticas

## 🟣 Level 4: Lógica y Estructuras de Datos

### Descripción
Implementar un sistema completo de análisis estadístico para la granja que calcule métricas avanzadas, tendencias, correlaciones y genere insights inteligentes sobre el rendimiento agrícola.

### Objetivo de Aprendizaje
- Implementar cálculos estadísticos avanzados
- Analizar tendencias y patrones en datos
- Crear métricas de performance personalizadas
- Generar insights automáticos

### Tareas Específicas

1. **Estadísticas básicas en `src/farm.py`:**
   ```python
   def calcular_estadisticas_basicas(self, datos):
       """
       Calcula media, mediana, moda, desviación estándar, varianza.
       
       Returns:
           dict: {
               'media': float,
               'mediana': float,
               'moda': float,
               'desviacion_estandar': float,
               'varianza': float,
               'rango': tuple(min, max)
           }
       """
       
   def distribucion_cultivos(self):
       """
       Analiza distribución de cultivos por categoría, temporada, etc.
       """
   ```

2. **Análisis de tendencias temporales:**
   ```python
   class AnalizadorTendencias:
       def __init__(self, historial_datos):
           self.datos = historial_datos
           
       def calcular_tendencia_lineal(self, serie_temporal):
           """
           Calcula pendiente y R² de tendencia lineal.
           """
           
       def detectar_estacionalidad(self, datos_por_temporada):
           """
           Identifica patrones estacionales en producción/ganancias.
           """
           
       def proyectar_crecimiento(self, dias_futuros=30):
           """
           Proyecta crecimiento basado en tendencias históricas.
           """
   ```

3. **Métricas de performance avanzadas:**
   ```python
   def calcular_roi_por_cultivo(self):
       """
       Return on Investment por cada tipo de cultivo.
       ROI = (Ganancia - Inversión) / Inversión * 100
       """
       
   def eficiencia_temporal(self):
       """
       Ganancia por unidad de tiempo para cada cultivo.
       """
       
   def indice_diversificacion(self):
       """
       Índice Herfindahl para medir diversificación de cultivos.
       Más bajo = más diversificado
       """
       
   def ratio_sostenibilidad(self):
       """
       Balance entre uso de recursos y regeneración.
       """
   ```

4. **Análisis de correlaciones:**
   ```python
   def matriz_correlacion(self, variables):
       """
       Calcula correlación entre diferentes métricas:
       - Agua usada vs productividad
       - Precio cultivo vs tiempo crecimiento  
       - Temporada vs ganancia
       """
       
   def encontrar_cultivos_complementarios(self):
       """
       Identifica cultivos que funcionan bien juntos
       basándose en correlaciones positivas.
       """
   ```

5. **Generador de insights automático:**
   ```python
   def generar_insights_inteligentes(self):
       """
       Analiza estadísticas y genera recomendaciones automáticas:
       - Cultivo más rentable por temporada
       - Problemas de eficiencia detectados
       - Oportunidades de optimización
       - Predicciones de mercado
       """
       
   def alertas_performance(self):
       """
       Detecta anomalías y genera alertas:
       - Caída súbita en productividad
       - Uso excesivo de recursos
       - Oportunidades de mercado
       """
   ```

### Archivos Afectados
- `src/farm.py` (estadísticas básicas)
- `src/statistics.py` (nuevo - análisis avanzado)
- `src/insights.py` (nuevo - generación de insights)
- `data/statistics.json` (almacenamiento de métricas)

### Tests Esperados
- Cálculos estadísticos son matemáticamente correctos
- Análisis de tendencias detecta patrones reales
- ROI y métricas de performance calculan bien
- Correlaciones identifican relaciones verdaderas
- Insights generados son relevantes y útiles

### Fórmulas a Implementar
```python
# Estadísticas básicas
def media(datos):
    return sum(datos) / len(datos)

def desviacion_estandar(datos):
    promedio = media(datos)
    return (sum((x - promedio) ** 2 for x in datos) / len(datos)) ** 0.5

# ROI
def roi_cultivo(ganancia, inversion):
    return ((ganancia - inversion) / inversion) * 100

# Correlación de Pearson
def correlacion_pearson(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(a * b for a, b in zip(x, y))
    sum_x2 = sum(a ** 2 for a in x)
    sum_y2 = sum(a ** 2 for a in y)
    
    numerador = n * sum_xy - sum_x * sum_y
    denominador = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2)) ** 0.5
    
    return numerador / denominador if denominador != 0 else 0

# Índice de diversificación Herfindahl
def indice_herfindahl(proporciones):
    return sum(p**2 for p in proporciones)
```

### Ejemplo de Uso
```python
# Generar reporte estadístico completo
estadisticas = granja.calcular_estadisticas_basicas(granja.ganancias_diarias)
tendencias = AnalizadorTendencias(granja.historial).calcular_tendencia_lineal()
insights = granja.generar_insights_inteligentes()

print(f"Ganancia promedio: {estadisticas['media']:.2f}")
print(f"Tendencia: {'📈 Subiendo' if tendencias['pendiente'] > 0 else '📉 Bajando'}")
print(f"Insight principal: {insights[0]['descripcion']}")
```

### Criterios de Éxito
- [ ] 5 estadísticas básicas implementadas correctamente
- [ ] Análisis de tendencias funciona con datos temporales
- [ ] Al menos 4 métricas de performance calculadas
- [ ] Matriz de correlación funcional
- [ ] Generador de insights produce recomendaciones útiles
- [ ] Tests verifican precisión matemática
- [ ] Visualización básica de estadísticas
- [ ] Documentación de todas las fórmulas usadas

### Dificultad: 🟣🟣🟣 Muy Alto
### Tiempo Estimado: 85-100 minutos
### Conceptos: Estadística descriptiva, análisis de tendencias, correlaciones, métricas de performance, machine learning básico