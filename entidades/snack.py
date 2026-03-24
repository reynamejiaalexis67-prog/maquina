from enums.precio import TipoProducto

class Maquina:
    
    def __init__(self,nombre:str,precio:float,cantidad:int,tipo:TipoProducto):
        
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        self.tipo=tipo
        
        
        
    def vender (self):
        if self.cantidad>0:
            
        
           self.cantidad-=1
        else: 
            print(" no se puede vender nada")
        
    
        