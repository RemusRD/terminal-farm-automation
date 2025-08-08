# Issue #34: Decoradores y Funciones Avanzadas (🔴 Avanzado)

## Descripción
Implementa un sistema de decoradores para optimizar y monitorear operaciones de la granja, incluyendo caché, logging automático, validación y control de acceso.

## Objetivos de Aprendizaje
- Decoradores y funciones de orden superior
- Functools y herramientas de función
- Metaprogramación básica
- Optimización con caché (memoización)
- Aspectos transversales (logging, timing)

## Tareas Específicas

### Tarea 1: Decoradores de Monitoreo
En `src/decorators.py`, implementa decoradores básicos:
```python
import functools
import time
import logging
from datetime import datetime

def timing_decorator(func):
    """Decorador que mide tiempo de ejecución."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            # TODO: Ejecutar función original
            # TODO: Calcular tiempo transcurrido
            # TODO: Logging del tiempo
            pass
        finally:
            # TODO: Cleanup si es necesario
            pass
    
    return wrapper

def log_farm_operations(level=logging.INFO):
    """Decorador parametrizado para logging de operaciones."""
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Log antes de ejecutar
            # TODO: Ejecutar función
            # TODO: Log después de ejecutar
            # TODO: Manejar excepciones en logging
            pass
        return wrapper
    
    return decorator

def validate_resources(required_resources):
    """Decorador que valida recursos antes de ejecutar operación."""
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # TODO: Verificar recursos requeridos
            # TODO: Lanzar excepción si insuficientes
            # TODO: Ejecutar función si recursos OK
            pass
        return wrapper
    
    return decorator
```

### Tarea 2: Sistema de Caché Inteligente
Implementa decoradores de optimización:
```python
def smart_cache(expire_seconds=300):
    """
    Caché inteligente que expira después del tiempo especificado.
    
    Args:
        expire_seconds (int): Segundos antes de que expire el caché
    """
    cache = {}
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Crear clave de caché basada en argumentos
            # TODO: Verificar si está en caché y no expirado
            # TODO: Ejecutar función si no está cacheado
            # TODO: Guardar resultado en caché con timestamp
            pass
        return wrapper
    
    return decorator

def memoize_expensive_calculations(func):
    """Memoización para cálculos costosos de la granja."""
    
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Implementar memoización
        # TODO: Manejo de argumentos mutables
        pass
    
    wrapper.cache_info = lambda: {
        'hits': 0, 
        'misses': 0, 
        'cache_size': len(cache)
    }
    wrapper.cache_clear = lambda: cache.clear()
    
    return wrapper
```

### Tarea 3: Decoradores de Control de Acceso
Implementa control de acceso basado en nivel de granjero:
```python
def requires_farmer_level(min_level):
    """
    Decorador que requiere un nivel mínimo de granjero.
    
    Args:
        min_level (int): Nivel mínimo requerido
    """
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # TODO: Verificar nivel del granjero
            # TODO: Lanzar excepción si nivel insuficiente
            # TODO: Ejecutar función si nivel OK
            pass
        return wrapper
    
    return decorator

def requires_season(valid_seasons):
    """
    Decorador que valida temporada para operaciones.
    
    Args:
        valid_seasons (list): Lista de temporadas válidas
    """
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # TODO: Verificar temporada actual
            # TODO: Validar contra temporadas válidas
            pass
        return wrapper
    
    return decorator

def rate_limit(max_calls_per_minute=60):
    """Decorador que limita la tasa de llamadas a una función."""
    
    calls = []
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.now()
            # TODO: Limpiar llamadas antiguas (más de 1 minuto)
            # TODO: Verificar si se excede el límite
            # TODO: Registrar llamada actual
            # TODO: Ejecutar función
            pass
        return wrapper
    
    return decorator
```

### Tarea 4: Composición de Decoradores
Crea funciones que usan múltiples decoradores:
```python
# En src/farm.py

class Farm:
    
    @timing_decorator
    @log_farm_operations(logging.INFO)
    @validate_resources({'water': 10, 'seeds': 1})
    @requires_farmer_level(5)
    @smart_cache(expire_seconds=120)
    def advanced_planting(self, crop_type, area_size, optimization_level="normal"):
        """
        Plantación avanzada con múltiples optimizaciones.
        
        Args:
            crop_type (str): Tipo de cultivo
            area_size (int): Tamaño del área a plantar
            optimization_level (str): Nivel de optimización
        
        Returns:
            dict: Resultado detallado de la plantación
        """
        # TODO: Implementar lógica de plantación avanzada
        # TODO: Aplicar optimizaciones según nivel
        pass
    
    @memoize_expensive_calculations
    @timing_decorator
    def calculate_optimal_crop_rotation(self, seasons=4, field_size=100):
        """
        Calcula rotación óptima de cultivos (cálculo costoso).
        
        Args:
            seasons (int): Número de temporadas a planificar
            field_size (int): Tamaño del campo
        
        Returns:
            dict: Plan de rotación optimizado
        """
        # TODO: Implementar algoritmo de optimización
        # Este sería un cálculo muy costoso en la realidad
        pass
    
    @rate_limit(max_calls_per_minute=10)
    @requires_season(['spring', 'summer'])
    def spray_pesticides(self, pesticide_type, area):
        """
        Aplicar pesticidas (operación limitada y estacional).
        
        Args:
            pesticide_type (str): Tipo de pesticida
            area (tuple): Área a tratar
        """
        # TODO: Implementar aplicación de pesticidas
        pass
```

### Tarea 5: Decorador de Clase para Singleton
Implementa un decorador de clase:
```python
def singleton(cls):
    """Decorador que convierte una clase en singleton."""
    
    instances = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class GameConfig:
    """Configuración global del juego (singleton)."""
    
    def __init__(self):
        self.settings = {}
        self.load_default_settings()
    
    def load_default_settings(self):
        """Carga configuración por defecto."""
        # TODO: Implementar carga de configuración
        pass
```

## Criterios de Éxito
- [x] ✅ Implementa decoradores de timing y logging
- [x] ✅ Sistema de caché funcional con expiración
- [x] ✅ Decoradores parametrizados funcionan correctamente
- [x] ✅ Control de acceso basado en nivel
- [x] ✅ Composición de múltiples decoradores
- [x] ✅ Decorador de clase (singleton) funciona

## Archivos a Crear/Modificar
- `src/decorators.py` (nuevo archivo)
- `src/farm.py` (añadir métodos decorados)

## Pistas
- `@functools.wraps(func)` preserva metadatos de función original
- Los decoradores parametrizados necesitan tres niveles de funciones
- Usa `time.time()` para medir tiempos de ejecución
- `functools.lru_cache` es una alternativa built-in para caché
- Los decoradores se aplican de abajo hacia arriba

## Nivel de Dificultad: 🔴 Avanzado
**Tiempo estimado:** 70-85 minutos

## Tecnologías y Conceptos
- Decoradores y metaprogramación
- Funciones de orden superior
- Caché y memoización
- Logging automático
- Control de acceso
- Optimización de rendimiento