# Issue #22: Range y enumerate en bucles 🔵

## 📋 Descripción
Domina las funciones `range()` y `enumerate()` para crear bucles más eficientes y flexibles. Aprenderás a generar secuencias numéricas personalizadas y a obtener tanto índices como valores al iterar.

## 🎯 Objetivos de Aprendizaje
- Usar `range()` con diferentes parámetros (start, stop, step)
- Aplicar `enumerate()` para obtener índices automáticamente
- Combinar `range()` y `enumerate()` en situaciones prácticas
- Crear bucles más legibles y eficientes
- Iterar con control preciso sobre índices

## 📝 Tarea
1. Crea nuevas funciones en `src/automation.py`:
   - `plantar_patron()`: Usa `range()` con step para plantar en patrón
   - `inspeccionar_cultivos()`: Usa `enumerate()` para mostrar posición e información
   - `regar_por_intervalos()`: Combina `range()` con step para riego espaciado
2. Implementa diferentes usos de `range()`:
   - `range(n)`: Secuencia simple
   - `range(start, stop)`: Con inicio y fin
   - `range(start, stop, step)`: Con paso personalizado

**Archivos a modificar:**
- `src/automation.py`

## 🧪 Tests
```bash
pytest tests/test_loops.py::test_issue_22_range_enumerate -v
```

### Casos de Prueba:
1. **Función `plantar_patron()`:** Planta cada 3 posiciones usando `range(0, 20, 3)`
   **Salida esperada:** Cultivos en posiciones 0, 3, 6, 9, 12, 15, 18

2. **Función `inspeccionar_cultivos()`:** Usa `enumerate()` para mostrar índice y cultivo
   **Salida esperada:** Lista con (índice, información_cultivo)

3. **Función `regar_por_intervalos()`:** Riega cada N cultivos
   **Salida esperada:** Solo riega cultivos en posiciones específicas

## 💡 Ejemplo de Código
```python
def plantar_patron(self, tipo_cultivo, inicio=0, fin=20, intervalo=2):
    """
    Planta cultivos en un patrón usando range() con step.
    
    Args:
        tipo_cultivo: Tipo de cultivo a plantar
        inicio: Posición inicial 
        fin: Posición final
        intervalo: Espaciado entre cultivos
    """
    plantados = []
    
    for posicion in range(inicio, fin, intervalo):
        if self.granja.puede_plantar_en(posicion):
            cultivo = self.granja.plantar_cultivo(tipo_cultivo, posicion)
            plantados.append((posicion, cultivo))
    
    return plantados

def inspeccionar_cultivos(self):
    """
    Inspecciona cultivos usando enumerate() para obtener índices.
    
    Returns:
        list: Lista de (índice, estado_cultivo)
    """
    reporte = []
    
    for indice, cultivo in enumerate(self.granja.cultivos):
        estado = {
            'posicion_en_lista': indice,
            'nombre': cultivo.nombre,
            'dias_crecimiento': cultivo.dias_plantado,
            'puede_cosechar': cultivo.puede_cosechar()
        }
        reporte.append((indice, estado))
    
    return reporte

def regar_por_intervalos(self, intervalo=2):
    """
    Riega cultivos saltando intervalos usando enumerate().
    
    Args:
        intervalo: Cada cuántos cultivos regar
    """
    regados = 0
    
    for indice, cultivo in enumerate(self.granja.cultivos):
        if indice % intervalo == 0:  # Cada 'intervalo' cultivos
            if cultivo.necesita_agua:
                cultivo.regar()
                regados += 1
    
    return regados
```

## 📈 Usos de Range
```
┌─────────────────────────────────────┐
│ Diferentes formas de usar range()   │
├─────────────────────────────────────┤
│                                     │
│ range(5)          → 0,1,2,3,4       │
│ range(2, 8)       → 2,3,4,5,6,7     │
│ range(0, 10, 2)   → 0,2,4,6,8       │
│ range(10, 0, -1)  → 10,9,8,7,6,5,4,3,2,1 │
│ range(1, 20, 3)   → 1,4,7,10,13,16,19│
│                                     │
└─────────────────────────────────────┘

Parámetros:
• start: número inicial (opcional, default=0)
• stop: número final (obligatorio, no incluido)
• step: incremento (opcional, default=1)
```

## 🔢 Enumerate vs Range
```python
# Sin enumerate - manual
for i in range(len(cultivos)):
    cultivo = cultivos[i]
    print(f"Posición {i}: {cultivo.nombre}")

# Con enumerate - automático  
for i, cultivo in enumerate(cultivos):
    print(f"Posición {i}: {cultivo.nombre}")

# Con enumerate y start
for i, cultivo in enumerate(cultivos, start=1):
    print(f"Cultivo #{i}: {cultivo.nombre}")
```

## 🎯 Casos Prácticos
```python
# Plantar en patrón alternado
for pos in range(0, 100, 2):  # Solo posiciones pares
    plantar_en(pos)

# Inspeccionar cada 5 cultivos
for i, cultivo in enumerate(cultivos):
    if i % 5 == 0:
        inspeccionar_detalladamente(cultivo)

# Riego por zonas
for fila in range(0, alto_granja, 3):  # Cada 3 filas
    for col in range(0, ancho_granja, 2):  # Cada 2 columnas
        regar_posicion(fila, col)
```

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 22
```

## 📚 Recursos
- [Python Range Function](https://docs.python.org/3/library/functions.html#func-range)
- [Python Enumerate](https://docs.python.org/3/library/functions.html#enumerate)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Usa `range()` con 1, 2 y 3 parámetros
- [ ] Implementa `enumerate()` correctamente
- [ ] Combina ambas funciones cuando es apropiado
- [ ] Crea patrones con `step` personalizado
- [ ] Maneja índices automáticamente con `enumerate()`
- [ ] Código es más legible que alternativas manuales
- [ ] Funciones son eficientes y bien documentadas