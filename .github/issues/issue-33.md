# Issue #33: Manejo de Excepciones (🔴 Avanzado)

## Descripción
Implementa un sistema robusto de manejo de excepciones para operaciones críticas de la granja, incluyendo excepciones personalizadas y manejo de errores elegante.

## Objetivos de Aprendizaje
- Try/except/finally blocks
- Excepciones personalizadas
- Propagación de errores
- Logging de errores
- Validación de entrada robusta

## Tareas Específicas

### Tarea 1: Excepciones Personalizadas
En `src/exceptions.py`, crea excepciones específicas de la granja:
```python
class FarmError(Exception):
    """Excepción base para errores de granja."""
    pass

class InsufficientResourcesError(FarmError):
    """Se lanza cuando no hay suficientes recursos."""
    
    def __init__(self, resource, required, available):
        self.resource = resource
        self.required = required
        self.available = available
        super().__init__(f"Recursos insuficientes: {resource}. "
                        f"Requerido: {required}, Disponible: {available}")

class WeatherError(FarmError):
    """Se lanza cuando el clima impide una operación."""
    
    def __init__(self, weather_condition, operation):
        self.weather_condition = weather_condition
        self.operation = operation
        super().__init__(f"No se puede {operation} durante {weather_condition}")

class CropError(FarmError):
    """Se lanza para errores relacionados con cultivos."""
    pass

class SeasonError(CropError):
    """Se lanza cuando se intenta plantar fuera de temporada."""
    
    def __init__(self, crop, current_season, valid_seasons):
        self.crop = crop
        self.current_season = current_season
        self.valid_seasons = valid_seasons
        super().__init__(f"{crop} no se puede plantar en {current_season}. "
                        f"Temporadas válidas: {', '.join(valid_seasons)}")
```

### Tarea 2: Manejo Robusto en Operaciones de Granja
En `src/farm.py`, añade manejo de excepciones:
```python
def plant_crop_safely(self, crop_type, position, quantity=1):
    """
    Planta cultivos con manejo completo de excepciones.
    
    Args:
        crop_type (str): Tipo de cultivo
        position (tuple): Posición (x, y)
        quantity (int): Cantidad a plantar
    
    Returns:
        dict: Resultado con éxito/error y detalles
    """
    result = {
        'success': False,
        'planted': 0,
        'errors': [],
        'warnings': []
    }
    
    try:
        # TODO: Validar entrada
        # TODO: Verificar recursos
        # TODO: Verificar temporada
        # TODO: Verificar clima
        # TODO: Plantar cultivos
        
        result['success'] = True
        result['planted'] = quantity
        
    except ValueError as e:
        # Manejo de errores de validación
        pass
    except InsufficientResourcesError as e:
        # Manejo de recursos insuficientes
        pass
    except SeasonError as e:
        # Manejo de temporada incorrecta
        pass
    except WeatherError as e:
        # Manejo de clima adverso
        pass
    except CropError as e:
        # Otros errores de cultivos
        pass
    except Exception as e:
        # Manejo de errores inesperados
        pass
    finally:
        # Código que siempre se ejecuta (logging, limpieza)
        pass
    
    return result
```

### Tarea 3: Validación con Excepciones
Implementa validadores que lanzan excepciones específicas:
```python
def validate_farm_operation(operation_type, **kwargs):
    """
    Valida parámetros de operación y lanza excepciones específicas.
    
    Args:
        operation_type (str): Tipo de operación
        **kwargs: Parámetros específicos de la operación
    
    Raises:
        ValueError: Para parámetros inválidos
        InsufficientResourcesError: Para recursos insuficientes
        SeasonError: Para operaciones fuera de temporada
        WeatherError: Para clima inadecuado
    """
    # TODO: Implementar validaciones específicas por operación
    pass

def safe_file_operation(operation, filename, *args, **kwargs):
    """
    Ejecuta operaciones de archivo con manejo de excepciones.
    
    Args:
        operation (callable): Función a ejecutar
        filename (str): Nombre del archivo
        *args, **kwargs: Argumentos para la operación
    
    Returns:
        tuple: (success: bool, result: any, error: str)
    """
    try:
        # TODO: Ejecutar operación con archivos
        pass
    except FileNotFoundError:
        # Archivo no encontrado
        pass
    except PermissionError:
        # Sin permisos
        pass
    except IOError:
        # Error de entrada/salida
        pass
    except Exception as e:
        # Error inesperado
        pass
```

### Tarea 4: Logging de Errores
Implementa sistema de logging para errores:
```python
import logging
from datetime import datetime

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/farm_errors.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def log_farm_error(error, context=None):
    """
    Registra errores de granja con contexto.
    
    Args:
        error (Exception): La excepción ocurrida
        context (dict): Contexto adicional del error
    """
    # TODO: Implementar logging estructurado
    pass

def create_error_report():
    """
    Crea reporte de errores desde logs.
    
    Returns:
        dict: Estadísticas de errores y recomendaciones
    """
    # TODO: Analizar logs y generar reporte
    pass
```

## Criterios de Éxito
- [x] ✅ Define excepciones personalizadas jerárquicas
- [x] ✅ Maneja diferentes tipos de errores apropiadamente
- [x] ✅ Usa try/except/finally correctamente
- [x] ✅ Implementa logging de errores
- [x] ✅ Proporciona mensajes de error útiles al usuario
- [x] ✅ El programa no se crashea ante errores esperados

## Archivos a Crear/Modificar
- `src/exceptions.py` (nuevo archivo)
- `src/farm.py` (modificar métodos existentes)
- `logs/` (directorio para logs)

## Pistas
- Las excepciones personalizadas heredan de `Exception` o subclases
- `try/except/finally`: finally siempre se ejecuta
- Usa logging en lugar de print para errores
- `isinstance(error, TipoError)` para verificar tipos de excepción
- Propaga errores críticos, maneja errores recuperables

## Nivel de Dificultad: 🔴 Avanzado
**Tiempo estimado:** 50-65 minutos

## Tecnologías y Conceptos
- Manejo de excepciones
- Excepciones personalizadas
- Logging
- Validación robusta
- Control de flujo con errores