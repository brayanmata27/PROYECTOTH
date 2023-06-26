from Usuario import*
class Empresa (Usuario):
    def __init__(self,Id:int, nombre:str, documento:int, telefono:int, correo:str,ubicacion:str):
        Usuario.__init__(self,nombre, documento, telefono, correo, ubicacion)
        self.__Id=id

    
        
