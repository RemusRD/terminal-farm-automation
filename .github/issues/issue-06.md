# Issue #6: Formateo de strings 🟢

## 📋 Descripción
Los mensajes del juego necesitan mostrar información dinámica como nombres, números y estadísticas de la granja. Es necesario implementar formateo de strings para crear mensajes informativos y personalizados.

## 🎯 Objetivos de Aprendizaje
- Usar f-strings para formateo moderno de strings
- Combinar texto y variables en mensajes
- Formatear números con decimales específicos
- Crear mensajes dinámicos e informativos

## 📝 Tarea
1. Crea una función `mostrar_estadisticas_granja(granja)` en `main.py`
2. La función debe mostrar información formateada de la granja:
   - Nombre de la granja
   - Día actual
   - Nivel de agua (con formato "XX/100")
   - Energía (como porcentaje)
   - Número de cultivos
3. Usa f-strings para el formateo

**Ejemplo de salida esperada:**
```
🌾 GRANJA: Mi Granja Feliz
📅 DÍA: 5
💧 AGUA: 75/100
⚡ ENERGÍA: 85%
🌱 CULTIVOS: 3 plantados
```

**Archivos a modificar:**
- `main.py`

## 🧪 Tests
```bash
pytest tests/test_basics.py::test_issue_6_string_formatting -v
```

### Casos de Prueba:
1. **Entrada:** Granja con valores específicos
   **Salida esperada:** Formato de mensaje correcto con f-strings

2. **Entrada:** Diferentes valores de estadísticas
   **Salida esperada:** Mensajes dinámicos apropiados

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 6
```

## 📚 Recursos
- [Curso Python Básico](https://github.com/midudev/curso-python/tree/main/01_basic)
- [F-strings Documentation](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Se usan f-strings para formateo
- [ ] Los mensajes son claros y informativos
- [ ] El formateo de números es correcto