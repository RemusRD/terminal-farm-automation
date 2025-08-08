"""Sistema de Mercado - Compra y venta de productos"""

class Mercado:
    """Maneja las transacciones del mercado"""
    
    def __init__(self):
        # Issue #23: Deberían ser diccionarios
        self.precios = "tomate:15, maíz:25, zanahoria:10"
        
    def calcular_precio(self, cultivo, cantidad):
        """Calcula el precio total de venta"""
        # Issue #3: Error de tipos - strings en lugar de números
        precio_unitario = "15"  # Debería obtener del diccionario
        total = precio_unitario * cantidad  # Error: no se puede multiplicar string
        return total
        
    def vender_cultivo(self, cultivo, cantidad):
        """Vende cultivos en el mercado"""
        # Issue #3: Necesita conversión de tipos
        ganancia = self.calcular_precio(cultivo, str(cantidad))
        return ganancia
        
    def comprar_semillas(self, tipo, cantidad):
        """Compra semillas del mercado"""
        # Issue #3 y #9: Falta conversión y lógica
        # TODO: Verificar si hay suficiente dinero
        # TODO: Calcular costo total
        # TODO: Reducir dinero y añadir semillas
        pass
        
    def mejor_cultivo_para_vender(self):
        """Encuentra el cultivo más rentable"""
        # Issue #24: Implementar algoritmo de búsqueda
        # TODO: Iterar sobre todos los cultivos
        # TODO: Calcular ganancia/tiempo para cada uno
        # TODO: Retornar el mejor
        pass
        
    def actualizar_precios(self):
        """Actualiza precios desde archivo CSV"""
        # Issue #31: Leer y parsear archivo CSV
        # TODO: Abrir data/prices.csv
        # TODO: Leer líneas
        # TODO: Actualizar diccionario de precios
        pass
        
    def mostrar_precios(self):
        """Muestra los precios actuales"""
        # Issue #1: Print mal formateado
        print === PRECIOS DEL MERCADO ===
        print(self.precios)