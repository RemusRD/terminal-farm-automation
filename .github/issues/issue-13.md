# Issue #13: Sistema de temporadas 🟡

## 📋 Descripción
La granja necesita un sistema de temporadas que afecte el crecimiento de cultivos. Diferentes cultivos crecen mejor en diferentes temporadas. Implementa lógica condicional para determinar qué cultivos pueden plantarse según la temporada actual.

## 🎯 Objetivos de Aprendizaje
- Usar condicionales complejas con múltiples condiciones
- Implementar lógica de negocio con if/elif/else
- Trabajar con enumeraciones o constantes
- Combinar lógica booleana para decisiones complejas

## 📝 Tarea
1. Abre el archivo `src/farm.py`
2. Añade una variable `self.temporada` en `__init__`
3. Implementa `cambiar_temporada(nueva_temporada)`:
   - Validar que la temporada sea válida
   - Actualizar la temporada actual
4. Modifica `puede_plantar_cultivo(cultivo)`:
   - Verificar si el cultivo es apropiado para la temporada
   - Considerar cultivos todo-temporada
5. Añade efectos de temporada en el crecimiento

**Archivos a modificar:**
- `src/farm.py`
- `src/crops.py` (añadir temporada a cultivos)

## 🧪 Tests
```bash
pytest tests/test_control.py::test_issue_13_seasons_system -v
```

### Casos de Prueba:
1. **Entrada:** Plantar tomate en verano
   **Salida esperada:** Permitido (tomate es de verano)

2. **Entrada:** Plantar calabaza en primavera
   **Salida esperada:** No permitido (calabaza es de otoño)

3. **Entrada:** Cambiar temporada a invierno
   **Salida esperada:** Solo cultivos de invierno disponibles

4. **Entrada:** Cultivo todo-temporada
   **Salida esperada:** Permitido en cualquier temporada

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 13
```

## 📚 Recursos
- [Curso Python Básico - Control Flow](https://github.com/midudev/curso-python/tree/main/02_flow_control)
- [Python Enums](https://docs.python.org/3/library/enum.html)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Sistema de temporadas funciona correctamente
- [ ] Solo se pueden plantar cultivos apropiados
- [ ] Se puede cambiar de temporada
- [ ] Cultivos todo-temporada funcionan
- [ ] Mensajes informativos sobre restricciones