# Issue #27: Diccionarios anidados

## 🟣 Level 4: Lógica y Estructuras de Datos

### Descripción
Crear un sistema completo de gestión de datos de granja utilizando diccionarios profundamente anidados para almacenar información jerárquica compleja sobre cultivos, temporadas, regiones y estadísticas.

### Objetivo de Aprendizaje
- Trabajar con estructuras de datos complejas y anidadas
- Navegar y manipular diccionarios multinivel
- Implementar sistemas de configuración avanzados
- Manejar datos jerárquicos eficientemente

### Tareas Específicas

1. **Crear estructura de datos principal en `src/farm.py`:**
   ```python
   DATOS_GRANJA_COMPLETOS = {
       'configuracion': {
           'general': {
               'nombre_granja': '',
               'nivel': 1,
               'experiencia': 0,
               'monedas': 1000
           },
           'recursos': {
               'agua': {'actual': 100, 'maximo': 100, 'regeneracion_diaria': 20},
               'energia': {'actual': 100, 'maximo': 100, 'regeneracion_diaria': 100},
               'fertilizante': {'actual': 50, 'precio_unitario': 5}
           }
       },
       'regiones': {
           'norte': {
               'clima': 'templado',
               'fertilidad': 0.8,
               'cultivos_plantados': {},
               'mejoras': ['riego_automatico', 'invernadero'],
               'temporadas_optimas': ['primavera', 'otoño']
           },
           # Añadir sur, este, oeste con características únicas
       },
       'estadisticas': {
           'por_temporada': {
               'primavera': {'cultivos_cosechados': 0, 'ganancia_total': 0},
               # Añadir verano, otoño, invierno
           },
           'por_cultivo': {
               # Se llena dinámicamente
           },
           'historico': {
               'mejor_dia': {'fecha': '', 'ganancia': 0},
               'peor_dia': {'fecha': '', 'perdida': 0},
               'cultivo_favorito': ''
           }
       }
   }
   ```

2. **Implementar funciones de navegación profunda:**
   ```python
   def obtener_valor_anidado(diccionario, ruta, default=None):
       """
       Obtiene valor usando ruta como 'configuracion.recursos.agua.actual'
       """
       
   def establecer_valor_anidado(diccionario, ruta, valor):
       """
       Establece valor en estructura anidada usando ruta.
       """
       
   def fusionar_diccionarios_profundo(dict1, dict2):
       """
       Fusiona diccionarios recursivamente manteniendo estructura.
       """
   ```

3. **Sistema de estadísticas avanzadas:**
   ```python
   def actualizar_estadisticas_cultivo(self, cultivo_nombre, accion, valor=1):
       """
       Actualiza estadísticas anidadas por cultivo y acción.
       Estructura: estadisticas.por_cultivo.{nombre}.{accion}.{temporada}
       """
       
   def generar_reporte_completo(self):
       """
       Genera reporte navegando toda la estructura anidada.
       """
   ```

4. **Configuración dinámica por región:**
   ```python
   def configurar_region(self, region, configuraciones):
       """
       Modifica configuraciones de región específica.
       
       Ejemplo:
       configurar_region('norte', {
           'clima': 'arido',
           'mejoras': ['riego_automatico', 'proteccion_solar'],
           'modificadores': {'crecimiento': 0.9, 'consumo_agua': 1.5}
       })
       """
   ```

### Archivos Afectados
- `src/farm.py` (estructura principal)
- `src/crops.py` (integración con cultivos)
- `data/` (archivos de configuración JSON)

### Tests Esperados
- Navegación de estructuras profundas funciona
- Funciones de get/set anidado correctas
- Estadísticas se actualizan en la estructura correcta
- Configuraciones por región aplican bien
- Serialización/deserialización de JSON

### Ejemplo de Estructura Completa
```python
# Acceso a datos profundamente anidados
nivel_agua_norte = granja['regiones']['norte']['recursos']['agua']['actual']

# Actualización de estadísticas complejas
granja['estadisticas']['por_temporada']['verano']['por_cultivo']['tomate']['cosechas'] += 1

# Configuración jerárquica
granja['regiones']['sur']['modificadores']['clima']['temperatura'] = 'alto'
granja['regiones']['sur']['modificadores']['clima']['humedad'] = 'bajo'
```

### Criterios de Éxito
- [ ] Estructura DATOS_GRANJA_COMPLETOS completa con 4 niveles de anidación
- [ ] 4 regiones configuradas con características únicas
- [ ] Funciones de navegación profunda implementadas
- [ ] Sistema de estadísticas multinivel funcional
- [ ] Configuración dinámica por región
- [ ] Tests cubren todos los niveles de anidación
- [ ] Serialización a JSON sin errores
- [ ] Documentación clara de la estructura

### Dificultad: 🟣🟣 Alto
### Tiempo Estimado: 65-80 minutos
### Conceptos: Diccionarios anidados, navegación de estructuras, datos jerárquicos, configuración dinámica