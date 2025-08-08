# Issue #8: Comentarios y documentación 🟢

## 📋 Descripción
El código actual carece de comentarios explicativos y documentación. Es importante añadir comentarios claros y docstrings para explicar qué hace cada función y cómo funciona el juego.

## 🎯 Objetivos de Aprendizaje
- Escribir comentarios útiles con `#`
- Crear docstrings para funciones con `"""`
- Documentar código complejo y lógica de negocio
- Seguir buenas prácticas de documentación

## 📝 Tarea
1. Añade comentarios explicativos en `main.py` y `src/farm.py`:
   - Comentarios de una línea para explicar código complejo
   - Comentarios de bloque para secciones importantes
   
2. Añade docstrings a todas las funciones:
   - Descripción de qué hace la función
   - Parámetros que recibe
   - Valor que retorna
   - Ejemplo de uso si es necesario

**Ejemplo de docstring:**
```python
def plantar_cultivo(tipo_cultivo, cantidad):
    """
    Planta un cultivo en la granja.
    
    Args:
        tipo_cultivo (str): El tipo de cultivo a plantar
        cantidad (int): Cantidad de semillas a plantar
    
    Returns:
        bool: True si se plantó exitosamente, False si no hay espacio
    
    Ejemplo:
        >>> plantar_cultivo("tomate", 5)
        True
    """
    # Tu código aquí
```

**Archivos a modificar:**
- `main.py`
- `src/farm.py`
- `src/crops.py`

## 🧪 Tests
```bash
pytest tests/test_basics.py::test_issue_8_comments_documentation -v
```

### Casos de Prueba:
1. **Entrada:** Revisar archivos de código
   **Salida esperada:** Funciones con docstrings apropiados

2. **Entrada:** Código complejo
   **Salida esperada:** Comentarios explicativos presentes

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 8
```

## 📚 Recursos
- [Curso Python Básico](https://github.com/midudev/curso-python/tree/main/01_basic)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [Python Comments Guide](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Todas las funciones tienen docstrings
- [ ] Código complejo tiene comentarios explicativos
- [ ] La documentación es clara y útil