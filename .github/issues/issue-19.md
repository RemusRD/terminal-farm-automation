# Issue #19: Función pasar_dia 🔵

## 📋 Descripción
Implementa la función `pasar_dia()` que simula el paso del tiempo en la granja. Esta función debe actualizar el estado de todos los cultivos, resetear recursos diarios, y manejar eventos automáticos.

## 🎯 Objetivos de Aprendizaje
- Implementar funciones sin parámetros que modifican estado
- Usar funciones para organizar lógica compleja
- Combinar bucles y funciones
- Actualizar múltiples variables de estado
- Crear funciones que coordinan otras operaciones

## 📝 Tarea
1. Abre el archivo `src/farm.py`
2. Encuentra la función `pasar_dia()` incompleta
3. Implementa la funcionalidad completa:
   - Incrementar contador `self.dia`
   - Resetear energía a 100
   - Actualizar estado de todos los cultivos (usar bucle)
   - Reducir nivel de agua por evaporación
   - Calcular ingresos diarios si hay cultivos para vender
   - Retornar resumen del día

**Archivos a modificar:**
- `src/farm.py`

## 🧪 Tests
```bash
pytest tests/test_loops.py::test_issue_19_day_function -v
```

### Casos de Prueba:
1. **Entrada:** Granja con cultivos en diferentes estados
   **Salida esperada:** Día incrementado, cultivos actualizados, energía restaurada

2. **Entrada:** Granja sin cultivos
   **Salida esperada:** Solo variables básicas actualizadas

3. **Entrada:** Cultivos listos para cosechar
   **Salida esperada:** Resumen incluye información de cosecha

## 💡 Ejemplo de Código
```python
def pasar_dia(self):
    """
    Simula el paso de un día en la granja.
    
    Returns:
        dict: Resumen de las actividades del día
    """
    # Incrementar día
    self.dia += 1
    
    # Resetear recursos
    self.energia = 100
    
    # Actualizar cultivos
    cultivos_listos = 0
    for cultivo in self.cultivos:
        cultivo.crecer_un_dia()
        if cultivo.puede_cosechar():
            cultivos_listos += 1
    
    # Crear resumen
    resumen = {
        'dia': self.dia,
        'cultivos_listos': cultivos_listos,
        # ...más información
    }
    
    return resumen
```

## 📅 Ciclo Diario
```
┌─────────────────┐
│ Inicio del día  │
└─────┬───────────┘
      │
      ▼
┌─────────────────┐
│ Incrementar día │
│ self.dia += 1   │
└─────┬───────────┘
      │
      ▼
┌─────────────────┐
│ Resetear        │
│ recursos        │
│ energia = 100   │
└─────┬───────────┘
      │
      ▼
┌─────────────────┐
│ Para cada       │◀─┐
│ cultivo:        │  │
│ - crecer()      │  │
│ - verificar()   │──┘
└─────┬───────────┘
      │
      ▼
┌─────────────────┐
│ Efectos         │
│ ambientales     │
│ (evaporación)   │
└─────┬───────────┘
      │
      ▼
┌─────────────────┐
│ Generar         │
│ resumen del día │
└─────────────────┘
```

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 19
```

## 📚 Recursos
- [Python Functions Return Values](https://realpython.com/python-return-statement/)
- [Working with Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Incrementa correctamente el día
- [ ] Resetea energía a valor completo
- [ ] Actualiza todos los cultivos usando bucle
- [ ] Maneja evaporación de agua
- [ ] Retorna resumen informativo
- [ ] No modifica cultivos incorrectamente
- [ ] Función es reutilizable y eficiente