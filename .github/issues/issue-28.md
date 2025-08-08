# Issue #28: Algoritmo de búsqueda

## 🟣 Level 4: Lógica y Estructuras de Datos

### Descripción
Implementar algoritmos de búsqueda avanzados para encontrar cultivos, optimizar rutas de riego, detectar patrones de crecimiento y realizar búsquedas inteligentes en la base de datos de la granja.

### Objetivo de Aprendizaje
- Implementar algoritmos de búsqueda clásicos
- Optimizar búsquedas con diferentes estrategias
- Trabajar con búsqueda en espacios bidimensionales
- Crear sistemas de indexación y caching

### Tareas Específicas

1. **Implementar búsquedas básicas en `src/farm.py`:**
   ```python
   def busqueda_lineal_cultivo(self, criterio_func):
       """
       Búsqueda lineal con función de criterio personalizada.
       Ejemplo: buscar primer cultivo que cumpla condición.
       """
       
   def busqueda_binaria_por_precio(self, precio_objetivo):
       """
       Búsqueda binaria en cultivos ordenados por precio.
       Requiere mantener lista ordenada.
       """
       
   def buscar_por_multiples_criterios(self, **criterios):
       """
       Búsqueda con múltiples filtros aplicados secuencialmente.
       Ejemplo: temporada='verano', precio_max=50, categoria='fruta'
       """
   ```

2. **Algoritmo de búsqueda espacial (pathfinding):**
   ```python
   class BuscadorRutas:
       def __init__(self, granja_mapa):
           self.mapa = granja_mapa
           self.cache_rutas = {}
           
       def encontrar_ruta_optima(self, inicio, destino, criterio='distancia'):
           """
           Encuentra la mejor ruta considerando obstáculos.
           Criterios: 'distancia', 'eficiencia_agua', 'tiempo'
           """
           
       def busqueda_bfs_area_riego(self, centro, radio):
           """
           Búsqueda en anchura para área circular de riego.
           """
           
       def busqueda_dfs_cultivos_conectados(self, posicion_inicial):
           """
           Búsqueda en profundidad para cultivos del mismo tipo conectados.
           """
   ```

3. **Sistema de indexación inteligente:**
   ```python
   class IndiceCultivos:
       def __init__(self):
           self.indices = {
               'por_precio': {},      # Precio -> [cultivos]
               'por_temporada': {},   # Temporada -> [cultivos] 
               'por_categoria': {},   # Categoria -> [cultivos]
               'por_tiempo': {},      # Tiempo -> [cultivos]
               'combinado': {}        # (temp, cat) -> [cultivos]
           }
           
       def construir_indices(self, cultivos):
           """Construye todos los índices para búsqueda rápida."""
           
       def busqueda_indexada(self, criterios):
           """Usa índices para búsqueda O(1)."""
   ```

4. **Algoritmos de pattern matching:**
   ```python
   def detectar_patron_crecimiento(self, historial_cultivo):
       """
       Detecta patrones en el crecimiento usando algoritmo KMP.
       Identifica ciclos, anomalías, tendencias.
       """
       
   def buscar_secuencia_plantacion(self, patron_deseado):
       """
       Busca secuencia específica de plantación en el historial.
       Ejemplo: ['tomate', 'lechuga', 'tomate'] repetido.
       """
   ```

### Archivos Afectados
- `src/farm.py` (búsquedas básicas)
- `src/search.py` (nuevo - algoritmos avanzados)
- `src/pathfinding.py` (nuevo - búsqueda espacial)

### Tests Esperados
- Búsqueda lineal encuentra elementos correctos
- Búsqueda binaria funciona en listas ordenadas
- Algoritmos de pathfinding encuentran rutas óptimas
- Índices aceleran búsquedas significativamente
- Pattern matching detecta secuencias correctamente

### Algoritmos a Implementar
```python
# 1. Búsqueda Lineal
def busqueda_lineal(lista, criterio):
    for i, elemento in enumerate(lista):
        if criterio(elemento):
            return i, elemento
    return -1, None

# 2. Búsqueda Binaria
def busqueda_binaria(lista_ordenada, objetivo, key_func):
    izq, der = 0, len(lista_ordenada) - 1
    while izq <= der:
        medio = (izq + der) // 2
        valor = key_func(lista_ordenada[medio])
        if valor == objetivo:
            return medio
        elif valor < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

# 3. BFS para área de riego
def bfs_area_riego(mapa, centro, radio):
    queue = [centro]
    visitados = set([centro])
    area = []
    
    while queue:
        pos = queue.pop(0)
        if distancia(pos, centro) <= radio:
            area.append(pos)
            for vecino in obtener_vecinos(pos):
                if vecino not in visitados:
                    visitados.add(vecino)
                    queue.append(vecino)
    return area
```

### Criterios de Éxito
- [ ] 4 algoritmos de búsqueda básica implementados
- [ ] Sistema de pathfinding con BFS y DFS
- [ ] Clase IndiceCultivos con 5 tipos de índices
- [ ] Algoritmo de pattern matching funcionando
- [ ] Cache de rutas para optimización
- [ ] Tests cubren todos los algoritmos
- [ ] Comparación de performance entre métodos
- [ ] Documentación de complejidad temporal

### Dificultad: 🟣🟣🟣 Muy Alto
### Tiempo Estimado: 80-95 minutos
### Conceptos: Algoritmos de búsqueda, pathfinding, indexación, pattern matching, optimización