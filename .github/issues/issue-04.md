# Issue #4: Variables de la granja 🟢

## 📋 Descripción
La clase `Farm` en `src/farm.py` está incompleta. Faltan variables importantes que debe tener una granja para funcionar correctamente en nuestro juego de simulación de agricultura.

## 🎯 Objetivos de Aprendizaje
- Definir atributos de instancia con `self`
- Entender el método `__init__` (constructor)
- Inicializar variables con valores apropiados
- Planificar las propiedades que necesita un objeto

## 📝 Tarea
1. Abre el archivo `src/farm.py`
2. Encuentra la clase `Farm` y su método `__init__`
3. Añade las siguientes variables de instancia:
   - `self.tamaño = 10` (tamaño de la granja en parcelas)
   - `self.nivel_agua = 100` (nivel de agua disponible)
   - `self.energia = 100` (energía del granjero)
   - `self.dia = 1` (día actual del juego)

**Archivos a modificar:**
- `src/farm.py`

## 🧪 Tests
```bash
pytest tests/test_basics.py::test_issue_4_farm_variables -v
```

### Casos de Prueba:
1. **Entrada:** `Farm()`
   **Salida esperada:** Instancia con todas las variables definidas

2. **Entrada:** `granja.tamaño`
   **Salida esperada:** `10`

3. **Entrada:** `granja.nivel_agua`
   **Salida esperada:** `100`

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 4
```

## 📚 Recursos
- [Curso Python Básico](https://github.com/midudev/curso-python/tree/main/01_basic)
- [Python Classes](https://docs.python.org/3/tutorial/classes.html)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] La granja tiene variable `tamaño`
- [ ] La granja tiene variable `nivel_agua`
- [ ] La granja tiene variable `energia`
- [ ] La granja tiene variable `dia`