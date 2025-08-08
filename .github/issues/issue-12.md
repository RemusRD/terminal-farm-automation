# Issue #12: Validación de entrada con if/else 🟡

## 📋 Descripción
Los usuarios pueden introducir datos incorrectos (números negativos, opciones inexistentes, etc.). Necesitas implementar validación de entrada usando if/else para asegurar que el programa no se rompa con datos inválidos.

## 🎯 Objetivos de Aprendizaje
- Validar entrada del usuario con condicionales
- Manejar casos de error con if/elif/else
- Usar comparadores (>, <, ==, !=)
- Proveer feedback útil al usuario

## 📝 Tarea
1. Abre el archivo `main.py`
2. Implementa `validar_cantidad()`:
   - Verificar que sea un número
   - Verificar que sea positivo
   - Mostrar mensaje de error si es inválido
3. Implementa `validar_opcion_menu()`:
   - Verificar que la opción esté en el rango válido
   - Mostrar opciones disponibles si es inválida
4. Añade validación en las funciones que piden input del usuario

**Archivos a modificar:**
- `main.py`

## 🧪 Tests
```bash
pytest tests/test_control.py::test_issue_12_input_validation -v
```

### Casos de Prueba:
1. **Entrada:** Cantidad negativa (-5)
   **Salida esperada:** Error, solicitar entrada válida

2. **Entrada:** Opción de menú inválida (99)
   **Salida esperada:** Error, mostrar opciones válidas

3. **Entrada:** Texto en lugar de número
   **Salida esperada:** Error, solicitar número válido

4. **Entrada:** Datos válidos
   **Salida esperada:** Procesar normalmente

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 12
```

## 📚 Recursos
- [Curso Python Básico - Control Flow](https://github.com/midudev/curso-python/tree/main/02_flow_control)
- [Input Validation Patterns](https://docs.python.org/3/tutorial/controlflow.html)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Se validan cantidades positivas
- [ ] Se validan opciones de menú
- [ ] Se maneja entrada no numérica
- [ ] Se proporcionan mensajes de error claros
- [ ] El programa no se rompe con datos inválidos