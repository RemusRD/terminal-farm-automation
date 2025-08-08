# Issue #14: Comparación de cultivos 🟡

## 📋 Descripción
Necesitas un sistema para comparar cultivos y ayudar al jugador a tomar decisiones. Implementa funciones que comparen cultivos por diferentes criterios usando operadores de comparación y lógica condicional.

## 🎯 Objetivos de Aprendizaje
- Usar operadores de comparación (>, <, >=, <=, ==, !=)
- Implementar funciones de comparación personalizadas
- Combinar múltiples criterios de comparación
- Crear rankings y recomendaciones

## 📝 Tarea
1. Abre el archivo `src/crops.py`
2. Implementa `comparar_por_precio(cultivo1, cultivo2)`:
   - Devolver cuál cultivo es más rentable
3. Implementa `comparar_por_tiempo(cultivo1, cultivo2)`:
   - Devolver cuál cultivo crece más rápido
4. Crea `recomendar_mejor_cultivo(cultivos, criterio)`:
   - Encontrar el mejor cultivo según criterio dado
5. Implementa `es_mas_rentable(cultivo1, cultivo2)`:
   - Comparar rentabilidad (precio/tiempo)

**Archivos a modificar:**
- `src/crops.py`

## 🧪 Tests
```bash
pytest tests/test_control.py::test_issue_14_crop_comparison -v
```

### Casos de Prueba:
1. **Entrada:** Comparar tomate ($15) vs maíz ($10)
   **Salida esperada:** Tomate es más rentable

2. **Entrada:** Comparar tiempo: trigo (5 días) vs lechuga (2 días)
   **Salida esperada:** Lechuga crece más rápido

3. **Entrada:** Recomendar mejor cultivo por rentabilidad
   **Salida esperada:** Cultivo con mayor precio/tiempo

4. **Entrada:** Lista de cultivos, criterio "precio"
   **Salida esperada:** Cultivo más caro

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 14
```

## 📚 Recursos
- [Curso Python Básico - Control Flow](https://github.com/midudev/curso-python/tree/main/02_flow_control)
- [Python Comparison Operators](https://docs.python.org/3/library/stdtypes.html#comparisons)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Comparación por precio funciona
- [ ] Comparación por tiempo funciona
- [ ] Sistema de recomendaciones funciona
- [ ] Cálculo de rentabilidad es correcto
- [ ] Manejo de casos edge (cultivos iguales)