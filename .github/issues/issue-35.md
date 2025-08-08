# Issue #35: Sistema de Persistencia con JSON (🔴 Avanzado)

## Descripción
Implementa un sistema completo de persistencia usando JSON para guardar y cargar el estado del juego, configuraciones, estadísticas históricas y respaldos automáticos.

## Objetivos de Aprendizaje
- Serialización y deserialización JSON
- Manejo avanzado de archivos
- Versionado de datos
- Respaldos automáticos
- Migración de esquemas de datos

## Tareas Específicas

### Tarea 1: Sistema Base de Persistencia
En `src/persistence.py`, implementa el sistema base:
```python
import json
import os
from datetime import datetime
from pathlib import Path
import shutil
from typing import Dict, Any, Optional

class GamePersistence:
    """Sistema de persistencia para el estado del juego."""
    
    def __init__(self, data_dir="data/saves"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.current_version = "1.0"
        
    def save_game_state(self, farm_data: Dict[str, Any], filename: str = None) -> bool:
        """
        Guarda el estado completo del juego.
        
        Args:
            farm_data (dict): Datos de la granja
            filename (str): Nombre del archivo (opcional)
        
        Returns:
            bool: True si se guardó exitosamente
        """
        try:
            # TODO: Generar nombre si no se proporciona
            # TODO: Añadir metadatos (versión, timestamp)
            # TODO: Crear respaldo del archivo existente
            # TODO: Guardar datos con formato JSON bonito
            # TODO: Validar integridad después de guardar
            pass
        except Exception as e:
            # TODO: Logging del error
            return False
    
    def load_game_state(self, filename: str = "latest") -> Optional[Dict[str, Any]]:
        """
        Carga el estado del juego desde archivo.
        
        Args:
            filename (str): Nombre del archivo o "latest" para el más reciente
        
        Returns:
            dict: Datos cargados o None si hay error
        """
        try:
            # TODO: Determinar archivo a cargar
            # TODO: Verificar integridad del archivo
            # TODO: Cargar y parsear JSON
            # TODO: Verificar versión y migrar si es necesario
            # TODO: Validar estructura de datos
            pass
        except Exception as e:
            # TODO: Logging del error y recuperación
            return None
```

### Tarea 2: Serialización Avanzada de Objetos
Implementa serialización de objetos complejos:
```python
import json
from datetime import datetime, date
from decimal import Decimal

class FarmJSONEncoder(json.JSONEncoder):
    """Encoder personalizado para objetos de la granja."""
    
    def default(self, obj):
        """
        Convierte objetos no serializables a formato JSON.
        
        Args:
            obj: Objeto a serializar
        
        Returns:
            Representación serializable del objeto
        """
        # TODO: Manejar datetime
        if isinstance(obj, (datetime, date)):
            pass
        
        # TODO: Manejar Decimal
        elif isinstance(obj, Decimal):
            pass
        
        # TODO: Manejar objetos personalizados (Farmer, Crop, etc.)
        elif hasattr(obj, '__dict__'):
            pass
        
        # TODO: Manejar sets
        elif isinstance(obj, set):
            pass
        
        return super().default(obj)

def deserialize_farm_objects(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deserializa objetos complejos desde JSON.
    
    Args:
        data (dict): Datos desde JSON
    
    Returns:
        dict: Datos con objetos reconstituidos
    """
    # TODO: Recorrer estructura recursivamente
    # TODO: Reconvertir fechas desde strings
    # TODO: Recrear objetos personalizados
    # TODO: Manejar referencias entre objetos
    pass
```

### Tarea 3: Sistema de Respaldos Automáticos
Implementa respaldos automáticos con rotación:
```python
class BackupManager:
    """Gestor de respaldos automáticos."""
    
    def __init__(self, backup_dir="data/backups", max_backups=10):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        self.max_backups = max_backups
    
    def create_backup(self, source_file: Path) -> bool:
        """
        Crea un respaldo del archivo fuente.
        
        Args:
            source_file (Path): Archivo a respaldar
        
        Returns:
            bool: True si el respaldo se creó exitosamente
        """
        try:
            # TODO: Generar nombre de respaldo con timestamp
            # TODO: Copiar archivo a directorio de respaldos
            # TODO: Comprimir si es necesario
            # TODO: Rotar respaldos antiguos
            pass
        except Exception as e:
            return False
    
    def restore_backup(self, backup_name: str, target_file: Path) -> bool:
        """
        Restaura un respaldo específico.
        
        Args:
            backup_name (str): Nombre del respaldo
            target_file (Path): Archivo destino
        
        Returns:
            bool: True si se restauró exitosamente
        """
        # TODO: Implementar restauración de respaldo
        pass
    
    def list_backups(self) -> list:
        """Lista todos los respaldos disponibles."""
        # TODO: Listar archivos de respaldo con metadatos
        pass
    
    def cleanup_old_backups(self):
        """Elimina respaldos antiguos según política de retención."""
        # TODO: Mantener solo max_backups archivos más recientes
        pass
```

### Tarea 4: Migración de Esquemas de Datos
Implementa sistema de versionado y migración:
```python
class DataMigrator:
    """Maneja migración de datos entre versiones."""
    
    MIGRATIONS = {
        "0.9": "1.0",
        "1.0": "1.1",
        # Más migraciones futuras
    }
    
    def __init__(self):
        self.current_version = "1.1"
    
    def needs_migration(self, data_version: str) -> bool:
        """Verifica si los datos necesitan migración."""
        # TODO: Comparar versiones
        pass
    
    def migrate_data(self, data: Dict[str, Any], from_version: str) -> Dict[str, Any]:
        """
        Migra datos desde versión antigua a actual.
        
        Args:
            data (dict): Datos en formato antiguo
            from_version (str): Versión de origen
        
        Returns:
            dict: Datos migrados a versión actual
        """
        current_data = data.copy()
        version = from_version
        
        # TODO: Aplicar migraciones en secuencia
        while version != self.current_version:
            if version in self.MIGRATIONS:
                # TODO: Aplicar migración específica
                pass
            else:
                raise ValueError(f"No hay ruta de migración desde {version}")
        
        return current_data
    
    def migrate_v09_to_v10(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Migración específica de v0.9 a v1.0."""
        # TODO: Cambios específicos de esquema
        # Ejemplo: añadir nuevos campos, renombrar campos, etc.
        pass
    
    def migrate_v10_to_v11(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Migración específica de v1.0 a v1.1."""
        # TODO: Más cambios de esquema
        pass
```

### Tarea 5: Estadísticas Históricas Persistentes
Implementa almacenamiento de estadísticas a largo plazo:
```python
class HistoricalStatsManager:
    """Maneja estadísticas históricas persistentes."""
    
    def __init__(self, stats_file="data/historical_stats.json"):
        self.stats_file = Path(stats_file)
        self.stats = self.load_stats()
    
    def load_stats(self) -> Dict[str, Any]:
        """Carga estadísticas históricas."""
        # TODO: Cargar desde archivo o crear estructura vacía
        pass
    
    def save_stats(self):
        """Guarda estadísticas al archivo."""
        # TODO: Guardar stats con formato JSON
        pass
    
    def record_daily_stats(self, farm_state: Dict[str, Any]):
        """
        Registra estadísticas diarias.
        
        Args:
            farm_state (dict): Estado actual de la granja
        """
        today = datetime.now().strftime("%Y-%m-%d")
        
        # TODO: Calcular estadísticas del día
        daily_stats = {
            'date': today,
            'crops_planted': 0,
            'crops_harvested': 0,
            'income': 0,
            'expenses': 0,
            # TODO: Más estadísticas
        }
        
        # TODO: Añadir a historial
        # TODO: Guardar automáticamente
        pass
    
    def get_trends(self, metric: str, days: int = 30) -> Dict[str, Any]:
        """
        Calcula tendencias para una métrica específica.
        
        Args:
            metric (str): Métrica a analizar
            days (int): Número de días a considerar
        
        Returns:
            dict: Análisis de tendencias
        """
        # TODO: Obtener datos históricos
        # TODO: Calcular tendencias (crecimiento, promedio, etc.)
        # TODO: Detectar patrones estacionales
        pass
    
    def export_stats(self, format="json") -> str:
        """
        Exporta estadísticas en formato especificado.
        
        Args:
            format (str): Formato de exportación ("json", "csv")
        
        Returns:
            str: Ruta del archivo exportado
        """
        # TODO: Implementar exportación en múltiples formatos
        pass
```

## Criterios de Éxito
- [x] ✅ Sistema de guardado/carga funcional con JSON
- [x] ✅ Serialización de objetos complejos
- [x] ✅ Respaldos automáticos con rotación
- [x] ✅ Migración de datos entre versiones
- [x] ✅ Estadísticas históricas persistentes
- [x] ✅ Manejo robusto de errores de archivo
- [x] ✅ Validación de integridad de datos

## Archivos a Crear/Modificar
- `src/persistence.py` (nuevo archivo)
- `data/saves/` (directorio para partidas guardadas)
- `data/backups/` (directorio para respaldos)

## Pistas
- Usa `json.dumps(indent=2)` para JSON legible
- `Path.exists()` y `Path.is_file()` para verificar archivos
- `shutil.copy2()` preserva metadatos al copiar
- Usa `try/except` extensivamente para operaciones de archivo
- `datetime.isoformat()` para timestamps serializables

## Nivel de Dificultad: 🔴 Avanzado
**Tiempo estimado:** 80-100 minutos

## Tecnologías y Conceptos
- Serialización JSON avanzada
- Manejo de archivos y directorios
- Respaldos y recuperación
- Versionado de datos
- Migración de esquemas
- Estadísticas históricas