# Issue #21: Función con parámetros y retorno 🔵

## 📋 Descripción
Crea una función completa que calcule la rentabilidad de diferentes cultivos. Esta función debe recibir parámetros, procesarlos, y retornar un resultado calculado. Aprenderás a diseñar funciones robustas con múltiples parámetros y valores de retorno.

## 🎯 Objetivos de Aprendizaje
- Definir funciones con múltiples parámetros
- Usar diferentes tipos de parámetros (obligatorios, opcionales, por defecto)
- Retornar diferentes tipos de datos
- Validar parámetros de entrada
- Documentar funciones profesionalmente

## 📝 Tarea
1. Crea una nueva función `calcular_rentabilidad()` en `src/crops.py`
2. La función debe recibir:
   - `precio` (float): Precio de venta del cultivo
   - `tiempo_crecimiento` (int): Días para crecer
   - `costo_mantenimiento` (float, opcional): Costo diario, por defecto 1.0
   - `incluir_estacional` (bool, opcional): Factor estacional, por defecto False
3. Calcular y retornar:
   - Ganancia neta por día
   - Tiempo de retorno de inversión
   - Clasificación de rentabilidad ("alta", "media", "baja")

**Archivos a modificar:**
- `src/crops.py`

## 🧪 Tests
```bash
pytest tests/test_loops.py::test_issue_21_function_params -v
```

### Casos de Prueba:
1. **Entrada:** precio=20, tiempo=5, costo=1.5
   **Salida esperada:** Dict con ganancia_diaria, tiempo_retorno, clasificacion

2. **Entrada:** Solo parámetros obligatorios
   **Salida esperada:** Usa valores por defecto correctamente

3. **Entrada:** Parámetros inválidos (precio negativo)
   **Salida esperada:** Maneja error graciosamente

## 💡 Ejemplo de Código
```python
def calcular_rentabilidad(precio, tiempo_crecimiento, 
                         costo_mantenimiento=1.0, 
                         incluir_estacional=False):
    """
    Calcula la rentabilidad de un cultivo.
    
    Args:
        precio (float): Precio de venta por unidad
        tiempo_crecimiento (int): Días necesarios para crecer
        costo_mantenimiento (float, optional): Costo diario. Default 1.0
        incluir_estacional (bool, optional): Factor estacional. Default False
    
    Returns:
        dict: Contiene ganancia_diaria, tiempo_retorno, clasificacion
        
    Raises:
        ValueError: Si precio o tiempo son negativos
    """
    # Validación de parámetros
    if precio < 0 or tiempo_crecimiento <= 0:
        raise ValueError("Precio y tiempo deben ser positivos")
    
    # Cálculos
    costo_total = costo_mantenimiento * tiempo_crecimiento
    ganancia_neta = precio - costo_total
    ganancia_diaria = ganancia_neta / tiempo_crecimiento
    
    # Factor estacional
    if incluir_estacional:
        ganancia_diaria *= 1.2  # 20% bonus
    
    # Clasificación
    if ganancia_diaria > 5:
        clasificacion = "alta"
    elif ganancia_diaria > 2:
        clasificacion = "media"  
    else:
        clasificacion = "baja"
    
    return {
        'ganancia_diaria': ganancia_diaria,
        'tiempo_retorno': tiempo_crecimiento,
        'clasificacion': clasificacion,
        'costo_total': costo_total
    }
```

## 📊 Tipos de Parámetros
```
┌─────────────────────────────────────┐
│ Tipos de Parámetros en Funciones   │
├─────────────────────────────────────┤
│                                     │
│ 1. Obligatorios (Positional)        │
│    def func(precio, tiempo):        │
│                                     │
│ 2. Por defecto (Default)            │
│    def func(precio, costo=1.0):     │
│                                     │
│ 3. Por palabra clave (Keyword)      │
│    func(precio=20, tiempo=5)        │
│                                     │
│ 4. Mixtos                           │
│    def func(precio, tiempo,         │
│             costo=1.0,              │
│             estacional=False):      │
│                                     │
└─────────────────────────────────────┘
```

## 🔍 Validación de Parámetros
```python
# Ejemplo de validación robusta
def calcular_rentabilidad(precio, tiempo_crecimiento, 
                         costo_mantenimiento=1.0, 
                         incluir_estacional=False):
    # Validar tipos
    if not isinstance(precio, (int, float)):
        raise TypeError("precio debe ser numérico")
    
    if not isinstance(tiempo_crecimiento, int):
        raise TypeError("tiempo_crecimiento debe ser entero")
    
    # Validar valores
    if precio < 0:
        raise ValueError("precio no puede ser negativo")
    
    if tiempo_crecimiento <= 0:
        raise ValueError("tiempo_crecimiento debe ser positivo")
    
    # Resto de la función...
```

## 💭 Sistema de Hints

Los hints están disponibles con:
```bash
python hints/get_hint.py 21
```

## 📚 Recursos
- [Python Function Parameters](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Default Arguments](https://realpython.com/python-kwargs-and-args/)

## ✅ Criterios de Éxito
- [ ] Todos los tests pasan
- [ ] Función acepta parámetros obligatorios y opcionales
- [ ] Usa valores por defecto correctamente
- [ ] Valida parámetros de entrada
- [ ] Retorna diccionario con resultados
- [ ] Incluye docstring completo con tipos
- [ ] Maneja errores con excepciones apropiadas
- [ ] Código es modular y reutilizable