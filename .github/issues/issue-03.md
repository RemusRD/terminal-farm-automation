# Issue #3: Conversión de tipos 🟢

## 📋 Descripción
La función `calcular_ganancia` en `main.py` recibe strings como parámetros pero necesita hacer operaciones matemáticas. Es necesario convertir los tipos de datos antes de realizar los cálculos.

## 🎯 Objetivos de Aprendizaje
- Usar funciones de conversión de tipos: `int()`, `float()`, `str()`
- Entender cuándo y por qué convertir tipos
- Manejar entrada de usuario (que siempre son strings)
- Realizar operaciones matemáticas con tipos correctos

## 📝 Tarea
1. Abre el archivo `main.py`
2. Encuentra la función `calcular_ganancia(precio_texto, cantidad_texto)`
3. Convierte los parámetros string a números:
   - `precio_texto` debe convertirse a `float`
   - `cantidad_texto` debe convertirse a `int`
4. Realiza el cálculo multiplicando precio por cantidad
5. Retorna el resultado como número (no string)

**Archivos a modificar:**
- `main.py`

## 🧪 Tests
```bash
pytest tests/test_basics.py::test_issue_3_type_conversion -v
```

### Casos de Prueba:
1. **Entrada:** `calcular_ganancia("10.5", "3")`
   **Salida esperada:** `31.5` (tipo float)

2. **Entrada:** `calcular_ganancia("25.0", "2")`
   **Salida esperada:** `50.0` (tipo float)

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 3
```

## 📚 Recursos
- [Curso Python Básico](https://github.com/midudev/curso-python/tree/main/01_basic)
- [Type Conversion Functions](https://docs.python.org/3/library/functions.html#int)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] La función retorna un número, no un string
- [ ] Los cálculos son matemáticamente correctos
- [ ] Se usan `float()` e `int()` apropiadamente