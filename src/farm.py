"""Sistema de Granja - Contiene errores intencionales para aprender"""

class Farm:
    """Clase principal de la granja"""
    
    def __init__(self):
        # Issue #4: Faltan variables importantes de la granja
        self.nombre = "Mi Granja"
        # TODO: Añadir tamaño, nivel_agua, energia, dia
        
        # Issue #10: cultivos debería ser una lista, no un string
        self.cultivos = "tomate, maíz, zanahoria"
        
    def plantar_cultivo(self, tipo_cultivo, posicion):
        """Planta un cultivo en una posición"""
        # Issue #18: Esta función está incompleta
        pass
        
    def regar_cultivos(self):
        """Riega todos los cultivos que lo necesiten"""
        # Issue #9: Falta toda la lógica de riego
        # TODO: Verificar si hay agua
        # TODO: Verificar qué cultivos necesitan agua
        # TODO: Regar y reducir nivel de agua
        print("Regando cultivos...")
        
    def cosechar(self):
        """Cosecha cultivos listos"""
        # Issue #16: Necesita un bucle for para revisar todos los cultivos
        # TODO: Implementar bucle de cosecha
        pass
        
    def pasar_dia(self):
        """Avanza un día en el juego"""
        # Issue #19: Función incompleta
        # TODO: Incrementar contador de días
        # TODO: Actualizar estado de cultivos
        # TODO: Resetear energía
        pass
        
    def mostrar_estado(self):
        """Muestra el estado actual de la granja"""
        # Issue #1: Prints mal formateados
        print Estado de la Granja:
        print("Cultivos:", self.cultivos)