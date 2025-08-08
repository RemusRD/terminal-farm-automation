# Issue #9: Sistema de riego con condicionales 🟡

## 📋 Descripción
El sistema de riego de la granja necesita lógica condicional. Los cultivos solo deben ser regados si hay agua disponible Y si realmente necesitan agua. Esto requiere usar operadores lógicos y sentencias if/else.

## 🎯 Objetivos de Aprendizaje
- Entender la lógica condicional con if/elif/else
- Usar operadores lógicos (and, or, not)
- Validar condiciones antes de ejecutar acciones
- Manejar recursos limitados con condicionales

## 📝 Tarea
1. Abre el archivo `src/automation.py`
2. Encuentra la función `regar_cultivos()`
3. Implementa la lógica condicional:
   - Verificar que hay agua disponible (nivel_agua > 0)
   - Solo regar cultivos que necesiten agua
   - Reducir el nivel de agua por cada cultivo regado
   - Mostrar mensajes informativos
4. Testea el sistema plantando y regando cultivos

**Archivos a modificar:**
- `src/automation.py`

## 🧪 Tests
```bash
pytest tests/test_control.py::test_issue_9_irrigation_system -v
```

### Casos de Prueba:
1. **Entrada:** Granja con agua y cultivos que necesitan riego
   **Salida esperada:** Cultivos regados, agua reducida

2. **Entrada:** Granja sin agua
   **Salida esperada:** No se riega nada, mensaje de error

3. **Entrada:** Cultivos que no necesitan agua
   **Salida esperada:** Se saltan esos cultivos

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 9
```

## 📚 Recursos
- [Curso Python Básico - Control Flow](https://github.com/midudev/curso-python/tree/main/02_flow_control)
- [Python If-Else Documentation](https://docs.python.org/3/tutorial/controlflow.html)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Se verifica que hay agua antes de regar
- [ ] Solo se riegan cultivos que lo necesitan
- [ ] El nivel de agua se reduce correctamente
- [ ] Se muestran mensajes apropiados