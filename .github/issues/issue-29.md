# Issue #29: Ordenamiento personalizado

## 🟣 Level 4: Lógica y Estructuras de Datos

### Descripción
Implementar sistemas de ordenamiento avanzado para cultivos, estadísticas y datos de granja usando algoritmos personalizados y criterios múltiples de clasificación.

### Objetivo de Aprendizaje
- Implementar algoritmos de ordenamiento clásicos
- Crear funciones de comparación personalizadas
- Trabajar con sorting multidimensional
- Optimizar performance de ordenamiento

### Tareas Específicas

1. **Algoritmos de ordenamiento básicos en `src/farm.py`:**
   ```python
   def ordenamiento_burbuja_cultivos(self, criterio='precio'):
       """
       Implementación de bubble sort para cultivos.
       Educativo pero ineficiente - O(n²).
       """
       
   def ordenamiento_seleccion_por_tiempo(self, cultivos):
       """
       Selection sort por tiempo de crecimiento.
       Útil para listas pequeñas - O(n²).
       """
       
   def ordenamiento_insercion_por_categoria(self, cultivos):
       """
       Insertion sort manteniendo orden por categoría.
       Eficiente para listas casi ordenadas - O(n²).
       """
   ```

2. **Algoritmos eficientes personalizados:**
   ```python
   def merge_sort_cultivos(self, cultivos, key_func, reverso=False):
       """
       Merge sort personalizado con función de clave.
       Estable y eficiente - O(n log n).
       """
       
   def quick_sort_por_rentabilidad(self, cultivos, inicio=0, fin=None):
       """
       Quick sort optimizado para rentabilidad.
       Promedio O(n log n), peor caso O(n²).
       """
       
   def heap_sort_por_prioridad(self, cultivos):
       """
       Heap sort para cultivos prioritarios.
       Garantizado O(n log n).
       """
   ```

3. **Ordenamiento multidimensional:**
   ```python
   class OrdenadorMultiple:
       def __init__(self):
           self.criterios = []
           
       def añadir_criterio(self, key_func, reverso=False, peso=1.0):
           """Añade criterio de ordenamiento con peso."""
           
       def ordenar_por_multiples_criterios(self, cultivos):
           """
           Ordena por múltiples criterios con pesos.
           Ejemplo: 40% rentabilidad + 30% rapidez + 30% experiencia
           """
           
       def ordenamiento_lexicografico(self, cultivos, criterios_orden):
           """
           Ordenamiento lexicográfico: primero por criterio1, 
           luego criterio2 en caso de empate, etc.
           """
   ```

4. **Sistemas de ranking avanzados:**
   ```python
   def crear_ranking_cultivos_inteligente(self, contexto_granja):
       """
       Crea ranking considerando contexto actual:
       - Temporada actual
       - Recursos disponibles  
       - Nivel del jugador
       - Objetivos a corto/largo plazo
       """
       
   def ordenar_por_compatibilidad(self, cultivos, cultivo_referencia):
       """
       Ordena cultivos por compatibilidad con uno de referencia.
       Considera: rotación de cultivos, alelopatía, uso de recursos.
       """
       
   def ranking_dinamico_mercado(self, precios_historicos):
       """
       Ordena por tendencias de mercado y predicciones.
       Usa datos históricos para proyectar rentabilidad futura.
       """
   ```

### Archivos Afectados
- `src/farm.py` (ordenamientos básicos)
- `src/sorting.py` (nuevo - algoritmos avanzados)
- `src/market.py` (integración con rankings)

### Tests Esperados
- Todos los algoritmos ordenan correctamente
- Ordenamiento múltiple funciona con varios criterios
- Performance es adecuada para cada algoritmo
- Ranking inteligente considera contexto
- Estabilidad de ordenamiento se mantiene

### Implementaciones Específicas
```python
# Ejemplo de merge sort personalizado
def merge_sort_personalizado(lista, key_func):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izq = merge_sort_personalizado(lista[:medio], key_func)
    der = merge_sort_personalizado(lista[medio:], key_func)
    
    return merge(izq, der, key_func)

# Comparador múltiple
def comparar_cultivos_multiple(c1, c2, criterios):
    for criterio, peso, reverso in criterios:
        val1 = criterio(c1) * peso
        val2 = criterio(c2) * peso
        
        if val1 != val2:
            if reverso:
                return val2 - val1
            return val1 - val2
    return 0

# Ranking inteligente con contexto
def calcular_score_contextual(cultivo, contexto):
    score = 0
    
    # Bonus por temporada
    if contexto['temporada'] in cultivo.temporadas:
        score += 20
    
    # Penalización por recursos insuficientes
    if cultivo.agua_requerida > contexto['agua_disponible']:
        score -= 30
        
    # Bonus por experiencia necesaria
    if contexto['nivel'] >= cultivo.nivel_requerido:
        score += 10
        
    return score
```

### Criterios de Éxito
- [ ] 3 algoritmos básicos implementados (O(n²))
- [ ] 3 algoritmos eficientes implementados (O(n log n))
- [ ] Clase OrdenadorMultiple funcional
- [ ] Sistema de ranking contextual
- [ ] Al menos 5 criterios de ordenamiento diferentes
- [ ] Tests de performance y correctitud
- [ ] Comparación de eficiencia entre algoritmos
- [ ] Documentación de complejidad temporal

### Dificultad: 🟣🟣🟣 Muy Alto
### Tiempo Estimado: 70-85 minutos
### Conceptos: Algoritmos de sorting, comparadores personalizados, ordenamiento múltiple, análisis de complejidad