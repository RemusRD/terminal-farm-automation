# Issue #20: Bucles anidados para regar zona 🔵

## 📋 Descripción
Implementa bucles anidados (`for` dentro de `for`) para regar una zona rectangular específica de la granja. Debes iterar por filas y columnas para cubrir toda el área seleccionada.

## 🎯 Objetivos de Aprendizaje
- Dominar bucles anidados (nested loops)
- Entender coordenadas 2D (x, y)
- Iterar sobre áreas rectangulares
- Usar `range()` con parámetros de inicio y fin
- Optimizar operaciones por zonas

## 📝 Tarea
1. Abre el archivo `src/automation.py`
2. Encuentra la función `regar_zona()` en la clase `Automatizador`
3. Implementa bucles anidados:
   - Bucle exterior para filas (y): `for y in range(y_inicio, y_fin + 1)`
   - Bucle interior para columnas (x): `for x in range(x_inicio, x_fin + 1)`
   - Para cada posición (x, y), verificar si hay cultivo
   - Regar si el cultivo necesita agua
   - Contar total de cultivos regados
4. Maneja casos donde no hay suficiente agua

**Archivos a modificar:**
- `src/automation.py`

## 🧪 Tests
```bash
pytest tests/test_loops.py::test_issue_20_nested_loops -v
```

### Casos de Prueba:
1. **Entrada:** Zona 3x3 con varios cultivos que necesitan agua
   **Salida esperada:** Riega cultivos en la zona, agua reducida

2. **Entrada:** Zona que excede los límites de la granja
   **Salida esperada:** Solo riega dentro de límites válidos

3. **Entrada:** Sin agua suficiente para toda la zona
   **Salida esperada:** Riega hasta donde alcance el agua

## 💡 Ejemplo de Código
```python
def regar_zona(self, x_inicio, x_fin, y_inicio, y_fin):
    """
    Riega una zona rectangular usando bucles anidados.
    
    Args:
        x_inicio, x_fin: Rango de columnas
        y_inicio, y_fin: Rango de filas
    
    Returns:
        int: Número de cultivos regados
    """
    regados = 0
    
    for y in range(y_inicio, y_fin + 1):
        for x in range(x_inicio, x_fin + 1):
            if self.granja.nivel_agua > 0:
                cultivo = self.granja.get_cultivo_en(x, y)
                if cultivo and cultivo.necesita_agua:
                    cultivo.regar()
                    self.granja.nivel_agua -= 1
                    regados += 1
    
    return regados
```

## 🗺️ Visualización de Zona
```
Granja 5x5 - Regar zona (1,1) a (3,3):

  0 1 2 3 4
0 · · · · ·
1 · █ █ █ ·  ← y_inicio = 1
2 · █ █ █ ·
3 · █ █ █ ·  ← y_fin = 3
4 · · · · ·
  ↑     ↑
x_inicio x_fin
  = 1   = 3

Bucles anidados:
- Bucle externo: y = 1, 2, 3
- Bucle interno: x = 1, 2, 3
- Total posiciones: 9
```

## 🔄 Flujo de Bucles Anidados
```
┌─────────────────────┐
│ for y in range(...) │◀──┐
└─────┬───────────────┘   │
      │                   │
      ▼                   │
┌─────────────────────┐   │
│ for x in range(...) │◀─┐│
└─────┬───────────────┘  ││
      │                  ││
      ▼                  ││
┌─────────────────────┐  ││
│ ¿Hay cultivo en     │  ││
│ posición (x,y)?     │  ││
└─────┬─────┬─────────┘  ││
      │No   │Si          ││
      │     ▼            ││
      │ ┌─────────────────┐ ││
      │ │ ¿Necesita agua? │ ││
      │ └─────┬─────┬─────┘ ││
      │       │No   │Si   ││
      │       │     ▼     ││
      │       │ ┌─────────┐ ││
      │       │ │ Regar   │ ││
      │       │ └─────────┘ ││
      ▼       ▼       ▼   ││
┌─────────────────────────┐ ││
│ Siguiente x ────────────┘ │
└───────────────────────────┘ │
┌─────────────────────────────┐ │
│ Siguiente y ────────────────┘
└─────────────────────────────┘
```

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 20
```

## 📚 Recursos
- [Nested Loops](https://realpython.com/python-nested-loops/)
- [Python Range Function](https://docs.python.org/3/library/functions.html#func-range)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Usa bucles anidados correctamente
- [ ] Maneja coordenadas 2D apropiadamente
- [ ] Riega solo cultivos que necesitan agua
- [ ] Respeta límites de agua disponible
- [ ] Cuenta cultivos regados correctamente
- [ ] Valida límites de la granja
- [ ] Código es eficiente y legible