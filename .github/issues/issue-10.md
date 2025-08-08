# Issue #10: Lista de cultivos 🟡

## 📋 Descripción
La granja necesita un sistema para gestionar múltiples cultivos. Actualmente `self.cultivos = None` no permite almacenar varios cultivos. Necesitas cambiar esto a una lista para poder añadir, quitar y gestionar múltiples cultivos.

## 🎯 Objetivos de Aprendizaje
- Entender qué son las listas en Python
- Inicializar listas vacías y con elementos
- Diferencia entre None y lista vacía []
- Preparar estructura de datos para gestión de cultivos

## 📝 Tarea
1. Abre el archivo `src/farm.py`
2. Encuentra donde se inicializa `self.cultivos = None`
3. Cámbialo a una lista vacía: `self.cultivos = []`
4. Verifica que la función `plantar_cultivo()` usa append() para añadir cultivos
5. Asegúrate de que otras funciones trabajen con listas

**Archivos a modificar:**
- `src/farm.py`

## 🧪 Tests
```bash
pytest tests/test_control.py::test_issue_10_crop_list -v
```

### Casos de Prueba:
1. **Entrada:** Crear nueva granja
   **Salida esperada:** self.cultivos es una lista vacía []

2. **Entrada:** Plantar varios cultivos
   **Salida esperada:** Todos los cultivos se almacenan en la lista

3. **Entrada:** Acceder a cultivos por índice
   **Salida esperada:** Se puede acceder con cultivos[0], cultivos[1], etc.

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 10
```

## 📚 Recursos
- [Curso Python Básico - Lists](https://github.com/midudev/curso-python/tree/main/03_lists)
- [Python Lists Documentation](https://docs.python.org/3/tutorial/introduction.html#lists)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] self.cultivos es una lista, no None
- [ ] Se pueden plantar múltiples cultivos
- [ ] La lista se inicializa vacía []
- [ ] Las funciones funcionan con la nueva estructura