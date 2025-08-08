# Issue #18: Función plantar_cultivo 🔵

## 📋 Descripción
Implementa la función `plantar_cultivo()` que permite plantar cultivos en la granja. Esta función debe validar que se puede plantar, actualizar la lista de cultivos, y manejar los recursos necesarios.

## 🎯 Objetivos de Aprendizaje
- Definir funciones con parámetros
- Usar parámetros para configurar el comportamiento
- Implementar validación dentro de funciones
- Modificar el estado del objeto
- Documentar funciones con docstrings

## 📝 Tarea
1. Abre el archivo `src/farm.py`
2. Encuentra la función `plantar_cultivo()` incompleta
3. Implementa la función completa:
   - Recibir parámetros: `tipo_cultivo` y `posicion`
   - Validar que hay espacio disponible
   - Validar que hay recursos (energia, agua, dinero)
   - Crear el cultivo y añadirlo a la lista
   - Actualizar recursos consumidos
   - Retornar resultado de la operación
4. Añade docstring descriptivo con parámetros y return

**Archivos a modificar:**
- `src/farm.py`

## 🧪 Tests
```bash
pytest tests/test_loops.py::test_issue_18_plant_function -v
```

### Casos de Prueba:
1. **Entrada:** Cultivo válido y posición libre
   **Salida esperada:** True, cultivo añadido, recursos reducidos

2. **Entrada:** Sin suficientes recursos
   **Salida esperada:** False, mensaje de error, sin cambios

3. **Entrada:** Posición ocupada
   **Salida esperada:** False, mensaje de error, sin plantación

## 💡 Ejemplo de Código
```python
def plantar_cultivo(self, tipo_cultivo, posicion):
    """
    Planta un cultivo en la posición especificada.
    
    Args:
        tipo_cultivo (str): Tipo de cultivo a plantar
        posicion (tuple): Coordenadas (x, y) donde plantar
    
    Returns:
        bool: True si se plantó exitosamente, False si no
    """
    # Validaciones aquí
    if self.energia < 10:
        return False
    
    # Lógica de plantación
    # ...
    
    return True
```

## 🌱 Flujo de Plantación
```
┌─────────────────┐
│ Recibir         │
│ parámetros      │
└─────┬───────────┘
      │
      ▼
┌─────────────────┐
│ ¿Hay recursos?  │
└─────┬─────┬─────┘
      │No   │Si
      │     ▼
      │ ┌─────────────────┐
      │ │ ¿Posición libre?│
      │ └─────┬─────┬─────┘
      │       │No   │Si
      │       │     ▼
      │       │ ┌─────────────────┐
      │       │ │ Crear cultivo   │
      │       │ │ Reducir energía │
      │       │ │ Añadir a lista  │
      │       │ └─────┬───────────┘
      │       │       │
      ▼       ▼       ▼
┌─────────────────────────┐
│ Retornar resultado      │
│ (True/False + mensaje)  │
└─────────────────────────┘
```

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 18
```

## 📚 Recursos
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Function Parameters](https://realpython.com/python-kwargs-and-args/)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Función acepta parámetros correctos
- [ ] Valida recursos antes de plantar
- [ ] Añade cultivo a la lista cuando es exitoso
- [ ] Retorna valores apropiados (True/False)
- [ ] Incluye docstring completo
- [ ] Maneja errores graciosamente
- [ ] Actualiza estado de la granja correctamente