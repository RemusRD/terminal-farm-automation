# Issue #2: Tipos de variables correctos 🟢

## 📋 Descripción
En la clase `Cultivo` en `src/crops.py`, las variables están definidas con tipos incorrectos. Los números están como strings, los booleanos como texto, causando problemas en los cálculos y comparaciones.

## 🎯 Objetivos de Aprendizaje
- Entender los tipos de datos básicos en Python (int, float, bool, str)
- Distinguir entre números y strings
- Comprender cuándo usar cada tipo de dato
- Aprender sobre booleanos True/False

## 📝 Tarea
1. Abre el archivo `src/crops.py`
2. Encuentra la clase `Cultivo` y su método `__init__`
3. Corrige los tipos de datos de las siguientes variables:
   - `tiempo_crecimiento` debe ser `int` (número entero)
   - `precio` debe ser `float` (número decimal)
   - `necesita_agua` debe ser `bool` (True/False)
   - `dias_plantado` debe ser `int` (número entero)

**Archivos a modificar:**
- `src/crops.py`

## 🧪 Tests
```bash
pytest tests/test_basics.py::test_issue_2_variable_types -v
```

### Casos de Prueba:
1. **Entrada:** `Cultivo("tomate")`
   **Salida esperada:** Todas las variables con tipos correctos

2. **Entrada:** `isinstance(cultivo.tiempo_crecimiento, int)`
   **Salida esperada:** `True`

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 2
```

## 📚 Recursos
- [Curso Python Básico](https://github.com/midudev/curso-python/tree/main/01_basic)
- [Python Data Types](https://docs.python.org/3/library/stdtypes.html)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] `tiempo_crecimiento` es de tipo int
- [ ] `precio` es de tipo float
- [ ] `necesita_agua` es de tipo bool
- [ ] `dias_plantado` es de tipo int