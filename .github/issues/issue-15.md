# Issue #15: Estado del juego con booleanos 🟡

## 📋 Descripción
El juego necesita trackear varios estados usando variables booleanas: si la granja está operativa, si es de noche, si hay una tormenta, etc. Implementa un sistema de estados que afecte las acciones disponibles en el juego.

## 🎯 Objetivos de Aprendizaje
- Usar variables booleanas para estados del juego
- Implementar lógica condicional basada en estados
- Combinar múltiples condiciones booleanas
- Manejar transiciones de estado

## 📝 Tarea
1. Abre el archivo `src/farm.py`
2. Añade variables de estado en `__init__`:
   - `self.es_dia = True`
   - `self.hay_tormenta = False`
   - `self.granja_operativa = True`
3. Implementa `cambiar_a_noche()` y `cambiar_a_dia()`
4. Implementa `iniciar_tormenta()` y `terminar_tormenta()`
5. Modifica acciones para verificar estados:
   - Solo plantar de día
   - No regar durante tormenta
   - Solo cosechar si granja está operativa

**Archivos a modificar:**
- `src/farm.py`
- `main.py` (actualizar menús según estado)

## 🧪 Tests
```bash
pytest tests/test_control.py::test_issue_15_game_state_booleans -v
```

### Casos de Prueba:
1. **Entrada:** Intentar plantar de noche
   **Salida esperada:** No permitido, mostrar mensaje

2. **Entrada:** Regar durante tormenta
   **Salida esperada:** No permitido, esperar que pare

3. **Entrada:** Cosechar con granja no operativa
   **Salida esperada:** Error, reparar granja primero

4. **Entrada:** Cambiar de día a noche
   **Salida esperada:** Estado actualizado, acciones limitadas

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 15
```

## 📚 Recursos
- [Curso Python Básico - Booleans](https://github.com/midudev/curso-python/tree/main/02_flow_control)
- [Python Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Estados booleanos funcionan correctamente
- [ ] Transiciones de estado son válidas
- [ ] Acciones respetan restricciones de estado
- [ ] Mensajes informativos sobre limitaciones
- [ ] Combinaciones de estados funcionan (noche + tormenta)