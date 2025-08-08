# Issue #7: Operaciones aritméticas básicas 🟢

## 📋 Descripción
El juego necesita realizar varios cálculos matemáticos: calcular costos de semillas, ganancias de venta, consumo de recursos, y estadísticas de rendimiento. Es fundamental implementar operaciones aritméticas correctas.

## 🎯 Objetivos de Aprendizaje
- Realizar operaciones básicas: suma, resta, multiplicación, división
- Usar operadores de asignación: `+=`, `-=`, `*=`, `/=`
- Calcular porcentajes y promedios
- Manejar división entera y módulo

## 📝 Tarea
1. Implementa las siguientes funciones en `main.py`:

```python
def calcular_costo_semillas(cantidad, precio_unitario):
    """Calcula el costo total de comprar semillas"""
    # Tu código aquí
    pass

def calcular_eficiencia(cultivos_cosechados, cultivos_plantados):
    """Calcula el porcentaje de eficiencia de la granja"""
    # Tu código aquí
    pass

def actualizar_recursos(granja, agua_usada, energia_usada):
    """Actualiza los recursos de la granja restando lo usado"""
    # Tu código aquí
    pass

def calcular_ganancia_diaria(ventas_totales, gastos_totales):
    """Calcula la ganancia neta del día"""
    # Tu código aquí
    pass
```

**Archivos a modificar:**
- `main.py`

## 🧪 Tests
```bash
pytest tests/test_basics.py::test_issue_7_arithmetic_operations -v
```

### Casos de Prueba:
1. **Entrada:** `calcular_costo_semillas(5, 2.5)`
   **Salida esperada:** `12.5`

2. **Entrada:** `calcular_eficiencia(8, 10)`
   **Salida esperada:** `80.0` (porcentaje)

3. **Entrada:** `actualizar_recursos(granja, 10, 15)`
   **Salida esperada:** Recursos actualizados correctamente

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 7
```

## 📚 Recursos
- [Curso Python Básico](https://github.com/midudev/curso-python/tree/main/01_basic)
- [Python Arithmetic Operators](https://docs.python.org/3/library/operator.html)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Las operaciones matemáticas son correctas
- [ ] Se usan operadores de asignación apropiados
- [ ] Los cálculos de porcentajes funcionan bien