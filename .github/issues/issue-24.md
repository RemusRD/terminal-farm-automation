# Issue #24: Algoritmo de mejor cultivo

## 🟣 Level 4: Lógica y Estructuras de Datos

### Descripción
Implementar un algoritmo inteligente que determine el mejor cultivo para plantar basándose en múltiples criterios: rentabilidad, temporada actual, recursos disponibles y preferencias del jugador.

### Objetivo de Aprendizaje
- Crear algoritmos de optimización
- Trabajar con múltiples criterios de decisión
- Implementar lógica de negocio compleja
- Usar funciones lambda y sorting personalizado

### Tareas Específicas

1. **Implementar en `src/market.py` la función `encontrar_mejor_cultivo()`:**
   ```python
   def encontrar_mejor_cultivo(granja, criterio='rentabilidad', temporada_actual='primavera'):
       """
       Encuentra el mejor cultivo basándose en criterios múltiples.
       
       Args:
           granja: Objeto granja con recursos actuales
           criterio: 'rentabilidad', 'rapido', 'experiencia', 'equilibrado'
           temporada_actual: Temporada actual del juego
       
       Returns:
           dict: Información del mejor cultivo y puntuación
       """
   ```

2. **Algoritmos de scoring por criterio:**
   - **Rentabilidad**: `(precio - costo) / tiempo_crecimiento`
   - **Rápido**: `1 / tiempo_crecimiento * 100`
   - **Experiencia**: `experiencia / tiempo_crecimiento`
   - **Equilibrado**: Promedio ponderado de todos los criterios

3. **Factores adicionales a considerar:**
   - Disponibilidad en temporada actual
   - Nivel requerido vs nivel del jugador
   - Recursos disponibles (agua, energía)
   - Espacio en la granja

4. **Implementar función de comparación personalizada:**
   ```python
   def comparar_cultivos(cultivo1, cultivo2, criterio, contexto):
       # Lógica de comparación avanzada
   ```

### Archivo Afectado
- `src/market.py`

### Tests Esperados
- Algoritmo selecciona correctamente por cada criterio
- Filtra cultivos no disponibles en temporada
- Considera restricciones de nivel y recursos
- Maneja casos edge (sin cultivos disponibles)

### Ejemplo de Uso
```python
granja = Farm(nivel=5, agua=50, energia=80)
mejor = encontrar_mejor_cultivo(granja, 'rentabilidad', 'verano')
print(f"Mejor cultivo: {mejor['nombre']}")
print(f"Puntuación: {mejor['score']:.2f}")
print(f"Razón: {mejor['justificacion']}")
```

### Criterios de Éxito
- [ ] Función `encontrar_mejor_cultivo()` implementada
- [ ] 4 criterios de optimización funcionando
- [ ] Considera todos los factores limitantes
- [ ] Incluye justificación de la decisión
- [ ] Tests cubren todos los casos
- [ ] Documentación clara del algoritmo

### Dificultad: 🟣🟣 Alto
### Tiempo Estimado: 60-75 minutos
### Conceptos: Algoritmos, optimización, sorting, lambda functions