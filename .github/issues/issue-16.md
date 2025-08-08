# Issue #16: Bucle de cosecha con for 🔵

## 📋 Descripción
Implementa un bucle `for` para automatizar la cosecha de todos los cultivos listos en la granja. Debes recorrer la lista de cultivos, verificar cuáles están listos para cosechar, y contabilizar la cantidad total cosechada.

## 🎯 Objetivos de Aprendizaje
- Dominar el bucle `for` con listas
- Entender la iteración sobre elementos
- Usar contadores para tracking de datos
- Aplicar condicionales dentro de bucles
- Trabajar con métodos de objetos en bucles

## 📝 Tarea
1. Abre el archivo `src/automation.py`
2. Encuentra la función `cosechar_todos()` en la clase `Automatizador`
3. Implementa el bucle de cosecha:
   - Usar `for cultivo in self.granja.cultivos:`
   - Verificar si cada cultivo está listo (`cultivo.puede_cosechar()`)
   - Cosechar los cultivos listos
   - Contar cuántos se cosecharon
   - Retornar el total cosechado
4. También implementa `plantar_hilera()` usando `for` con `range()`

**Archivos a modificar:**
- `src/automation.py`

## 🧪 Tests
```bash
pytest tests/test_loops.py::test_issue_16_harvest_loop -v
```

### Casos de Prueba:
1. **Entrada:** Granja con 5 cultivos, 3 listos para cosechar
   **Salida esperada:** Retorna 3, inventario actualizado

2. **Entrada:** Granja sin cultivos listos
   **Salida esperada:** Retorna 0, sin cambios

3. **Entrada:** Lista vacía de cultivos
   **Salida esperada:** Retorna 0 sin errores

## 💡 Ejemplo de Código
```python
def cosechar_todos(self):
    cosechados = 0
    for cultivo in self.granja.cultivos:
        if cultivo.puede_cosechar():
            # Lógica de cosecha aquí
            cosechados += 1
    return cosechados
```

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 16
```

## 📚 Recursos
- [Python For Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Iterating over Lists](https://realpython.com/python-for-loop/)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Usa bucle `for` para iterar sobre cultivos
- [ ] Cuenta correctamente cultivos cosechados
- [ ] Maneja listas vacías sin errores
- [ ] Implementa `plantar_hilera()` con `range()`
- [ ] Código es legible y bien comentado