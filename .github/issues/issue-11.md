# Issue #11: Métodos de lista 🟡

## 📋 Descripción
Ahora que tienes una lista de cultivos, necesitas implementar las operaciones básicas: añadir cultivos con `append()`, quitar cultivos con `remove()`, ordenar cultivos por precio, y obtener información como la longitud de la lista.

## 🎯 Objetivos de Aprendizaje
- Usar métodos de lista: append(), remove(), sort()
- Entender len() para obtener tamaño de lista
- Usar operador 'in' para verificar pertenencia
- Ordenar listas con funciones key

## 📝 Tarea
1. Abre el archivo `src/farm.py`
2. Implementa `plantar_cultivo()` usando `self.cultivos.append(cultivo)`
3. Implementa `quitar_cultivo()` usando `self.cultivos.remove(cultivo)`
4. Crea `ordenar_cultivos_por_precio()` usando `self.cultivos.sort()`
5. Implementa `contar_cultivos()` usando `len(self.cultivos)`
6. Crea `tiene_cultivo()` usando el operador `in`

**Archivos a modificar:**
- `src/farm.py`

## 🧪 Tests
```bash
pytest tests/test_control.py::test_issue_11_list_methods -v
```

### Casos de Prueba:
1. **Entrada:** Plantar cultivo "tomate"
   **Salida esperada:** Lista contiene 1 elemento

2. **Entrada:** Quitar cultivo existente
   **Salida esperada:** Cultivo eliminado de la lista

3. **Entrada:** Ordenar cultivos por precio
   **Salida esperada:** Lista ordenada de menor a mayor precio

4. **Entrada:** Verificar si tiene cultivo específico
   **Salida esperada:** True si existe, False si no

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 11
```

## 📚 Recursos
- [Curso Python Básico - Lists](https://github.com/midudev/curso-python/tree/main/03_lists)
- [Python List Methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] append() añade cultivos correctamente
- [ ] remove() elimina cultivos existentes
- [ ] sort() ordena la lista por precio
- [ ] len() devuelve el número correcto de elementos
- [ ] Operador 'in' funciona para verificar pertenencia