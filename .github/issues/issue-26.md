# Issue #26: Comprensión de listas

## 🟣 Level 4: Lógica y Estructuras de Datos

### Descripción
Implementar funciones avanzadas de análisis de granja utilizando comprensiones de listas (list comprehensions) para realizar operaciones complejas de filtrado, mapeo y agregación de datos.

### Objetivo de Aprendizaje
- Dominar list comprehensions avanzadas
- Implementar filtrado y transformación eficiente
- Crear análisis de datos complejos
- Optimizar código con Python idiomático

### Tareas Específicas

1. **Implementar funciones en `src/farm.py` usando list comprehensions:**
   ```python
   def obtener_cultivos_listos_cosecha(self):
       """Retorna lista de cultivos listos para cosechar."""
       return [cultivo for cultivo in self.cultivos if cultivo.esta_listo()]
   
   def calcular_valor_total_granja(self):
       """Calcula valor total usando comprehension."""
       return sum([cultivo.precio for cultivo in self.cultivos if cultivo.esta_listo()])
   ```

2. **Análisis avanzado con comprehensions anidadas:**
   ```python
   def analizar_produccion_por_categoria(self):
       """
       Retorna diccionario con producción por categoría.
       Usa comprehensions anidadas y condiciones múltiples.
       """
       categorias = ['verdura', 'fruta', 'grano', 'especial']
       return {
           categoria: {
               'cantidad': len([c for c in self.cultivos if c.categoria == categoria]),
               'valor_total': sum([c.precio for c in self.cultivos 
                                 if c.categoria == categoria and c.esta_listo()]),
               'promedio_dias': sum([c.dias_crecimiento for c in self.cultivos 
                                   if c.categoria == categoria]) / 
                               max(1, len([c for c in self.cultivos if c.categoria == categoria]))
           }
           for categoria in categorias
       }
   ```

3. **Funciones de filtrado inteligente:**
   ```python
   def cultivos_por_criterios(self, **kwargs):
       """
       Filtra cultivos usando múltiples criterios.
       Ejemplo: cultivos_por_criterios(temporada='verano', precio_min=20, nivel_max=5)
       """
   
   def generar_reporte_eficiencia(self):
       """
       Genera reporte usando comprehensions y funciones built-in.
       Incluye: más rentable, más rápido, mejor por temporada.
       """
   ```

4. **Transformaciones complejas:**
   ```python
   def crear_mapa_precios_mercado(self, fluctuacion=0.1):
       """Crea diccionario de precios con fluctuación aleatoria."""
       return {
           cultivo.nombre: {
               'precio_base': cultivo.precio,
               'precio_actual': cultivo.precio * (1 + random.uniform(-fluctuacion, fluctuacion)),
               'tendencia': 'subida' if random.random() > 0.5 else 'bajada'
           }
           for cultivo in self.cultivos
       }
   ```

### Archivos Afectados
- `src/farm.py` (funciones de análisis)
- `src/market.py` (análisis de mercado)

### Tests Esperados
- Todas las comprehensions funcionan correctamente
- Filtros múltiples aplican bien
- Cálculos agregados son exactos
- Comprehensions anidadas retornan estructura correcta
- Performance es eficiente

### Ejemplos de Comprensiones a Implementar
```python
# Básicas
cultivos_caros = [c for c in cultivos if c.precio > 50]

# Con condición múltiple
cultivos_verano_rentables = [c for c in cultivos 
                           if 'verano' in c.temporadas and c.precio/c.tiempo > 5]

# Con transformación
nombres_mayusculas = [c.nombre.upper() for c in cultivos]

# Anidadas
matriz_compatibilidad = [[c1.nombre for c1 in cultivos 
                         if c1.categoria == c2.categoria] 
                        for c2 in cultivos]

# Con diccionarios
mapa_precios = {c.nombre: c.precio for c in cultivos if c.esta_disponible()}
```

### Criterios de Éxito
- [ ] Al menos 8 funciones implementadas con list comprehensions
- [ ] Uso correcto de filtros múltiples
- [ ] Implementación de comprehensions anidadas
- [ ] Análisis de datos complejos funcionando
- [ ] Tests verifican exactitud de los cálculos
- [ ] Código es eficiente y legible
- [ ] Documentación clara de cada función

### Dificultad: 🟣🟣 Alto
### Tiempo Estimado: 50-65 minutos
### Conceptos: List comprehensions, filtrado avanzado, transformación de datos, análisis