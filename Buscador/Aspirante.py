from Usuario import *
class Aspirante(Usuario):
    def __init__(self,id_Aspirante,Contraseña,Ocupacion):
        Usuario.__init__(self,)
        self.__Contraseña=Contraseña
        self.__Ocupacion=Ocupacion
        
    