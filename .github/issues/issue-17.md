# Issue #17: Game loop con while 🔵

## 📋 Descripción
Implementa el bucle principal del juego usando `while`. Este bucle debe mantener el juego corriendo hasta que el usuario decida salir, mostrando el menú y procesando opciones repetidamente.

## 🎯 Objetivos de Aprendizaje
- Dominar el bucle `while` para repetición condicional
- Entender variables de control de bucles
- Crear menús interactivos que se repitan
- Manejar la salida controlada de bucles
- Integrar input del usuario con bucles

## 📝 Tarea
1. Abre el archivo `main.py`
2. Encuentra los comentarios sobre el game loop principal
3. Implementa el bucle `while`:
   - Variable de control `jugando = True`
   - Mostrar menú en cada iteración
   - Procesar opción del usuario
   - Permitir salir cambiando `jugando = False`
4. Asegúrate de que el bucle sea eficiente y no infinito

**Archivos a modificar:**
- `main.py`

## 🧪 Tests
```bash
pytest tests/test_loops.py::test_issue_17_game_loop -v
```

### Casos de Prueba:
1. **Entrada:** Usuario selecciona opciones del menú y luego sale
   **Salida esperada:** Bucle se ejecuta múltiples veces y termina

2. **Entrada:** Usuario selecciona salir inmediatamente
   **Salida esperada:** Bucle termina en primera iteración

3. **Entrada:** Opciones inválidas seguidas de salida válida
   **Salida esperada:** Maneja errores y permite salir

## 💡 Ejemplo de Código
```python
def main():
    jugando = True
    
    while jugando:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "0":
            jugando = False
            print("¡Gracias por jugar!")
        else:
            procesar_opcion(opcion)
```

## 🔄 Flujo del Game Loop
```
┌─────────────────┐
│ Inicializar     │
│ jugando = True  │
└─────┬───────────┘
      │
      ▼
┌─────────────────┐
│ while jugando:  │◀─┐
│                 │  │
├─────────────────┤  │
│ Mostrar menú    │  │
├─────────────────┤  │
│ Obtener opción  │  │
├─────────────────┤  │
│ Procesar opción │  │
├─────────────────┤  │
│ ¿Continuar?     │──┘
└─────┬───────────┘
      │ No
      ▼
┌─────────────────┐
│ Fin del juego   │
└─────────────────┘
```

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 17
```

## 📚 Recursos
- [Python While Loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue)
- [Game Loop Patterns](https://gameprogrammingpatterns.com/game-loop.html)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Usa bucle `while` correctamente
- [ ] Variable de control funciona apropiadamente  
- [ ] Permite salir del juego sin errores
- [ ] Menú se muestra repetidamente
- [ ] No hay bucles infinitos
- [ ] Código es legible y bien estructurado