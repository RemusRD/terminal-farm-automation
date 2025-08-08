# Issue #23: Diccionario de cultivos

## 🟣 Level 4: Lógica y Estructuras de Datos

### Descripción
Crear un diccionario completo que almacene información detallada sobre diferentes cultivos de la granja. Este diccionario será la base de datos central para todos los cultivos disponibles.

### Objetivo de Aprendizaje
- Trabajar con diccionarios y estructuras de datos anidadas
- Organizar información de forma eficiente
- Acceder y manipular datos complejos

### Tareas Específicas

1. **Crear diccionario base en `src/crops.py`:**
   ```python
   CULTIVOS_DB = {
       'tomate': {
           'precio': 25,
           'tiempo_crecimiento': 4,
           'temporadas': ['primavera', 'verano'],
           'agua_requerida': 3,
           'experiencia': 10,
           'categoria': 'verdura',
           'descripcion': 'Tomate jugoso perfecto para ensaladas',
           'nivel_requerido': 1
       },
       # Añadir al menos 8 cultivos más
   }
   ```

2. **Implementar funciones de utilidad:**
   - `obtener_cultivo(nombre)`: Retorna información del cultivo
   - `cultivos_por_temporada(temporada)`: Filtra por temporada
   - `cultivos_por_categoria(categoria)`: Filtra por categoría
   - `cultivos_disponibles(nivel_jugador)`: Filtra por nivel

3. **Categorías a incluir:**
   - Verduras (tomate, lechuga, zanahoria)
   - Frutas (manzana, fresa, uva)
   - Granos (trigo, maíz, arroz)
   - Especiales (ginseng, trufa, flor dorada)

### Archivo Afectado
- `src/crops.py`

### Tests Esperados
- Diccionario contiene al menos 9 cultivos
- Cada cultivo tiene todos los campos requeridos
- Funciones de filtrado funcionan correctamente
- Validación de datos correcta

### Criterios de Éxito
- [ ] Diccionario CULTIVOS_DB completamente definido
- [ ] Al menos 9 cultivos con información completa
- [ ] 4 funciones de utilidad implementadas
- [ ] Tests pasan correctamente
- [ ] Documentación clara de cada cultivo

### Dificultad: 🟣 Intermedio-Alto
### Tiempo Estimado: 45-60 minutos
### Conceptos: Diccionarios, estructuras anidadas, filtrado de datos