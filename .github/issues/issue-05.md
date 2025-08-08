# Issue #5: Input del usuario 🟢

## 📋 Descripción
El juego necesita interactuar con el usuario para recibir comandos y datos. Actualmente no hay manera de que el usuario proporcione información al programa, como el nombre de la granja o las acciones a realizar.

## 🎯 Objetivos de Aprendizaje
- Usar la función `input()` para recibir datos del usuario
- Mostrar mensajes claros al usuario
- Manejar la entrada del usuario como strings
- Crear interacción básica en consola

## 📝 Tarea
1. Abre el archivo `main.py`
2. Añade uso de `input()` para recibir información del usuario:
   - Pedir el nombre de la granja al usuario
   - Mostrar un mensaje de bienvenida personalizado
   - Guardar la entrada en una variable
3. Asegúrate de que los mensajes sean claros y amigables

**Ejemplo de implementación:**
```python
nombre_granja = input("¿Cómo quieres llamar a tu granja? ")
print(f"¡Bienvenido a {nombre_granja}!")
```

**Archivos a modificar:**
- `main.py`

## 🧪 Tests
```bash
pytest tests/test_basics.py::test_issue_5_user_input -v
```

### Casos de Prueba:
1. **Entrada:** Revisar que `main.py` contenga `input(`
   **Salida esperada:** La función `input()` debe estar presente

2. **Entrada:** Ejecutar el programa
   **Salida esperada:** Debe pedir información al usuario

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 5
```

## 📚 Recursos
- [Curso Python Básico](https://github.com/midudev/curso-python/tree/main/01_basic)
- [Input Function](https://docs.python.org/3/library/functions.html#input)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] El código usa `input()` para recibir datos
- [ ] Los mensajes al usuario son claros
- [ ] El programa es interactivo