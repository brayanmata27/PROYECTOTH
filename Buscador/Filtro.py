from Busqueda import *
from Ocupacion import *
class Filtro():
    def __init__(self,Area_Trabajo,Area_Ocupacion,Tipo_contrato,Tipo_Jornada):
        self.__Area_Trabajo=Area_Trabajo
        self.__Area_Ocupacion=Area_Ocupacion
        self.__Tipo_Contrato=Tipo_contrato
        self.__Tipo_Joornada=Tipo_Jornada
        
    def setArea_Trabajo(self,Area_Trabajo):
        self.__Area_Trabajo=Area_Trabajo
        
    def getArea_Trabajo(self):
        return self.__Area_Trabajo
    
    def setArea_Ocupacion(self,Area_Ocupacion):
        self.__Area_Ocupacion=Area_Ocupacion
        
    def getArea_Ocupaion(self):
        return self.__Area_Ocupacion
    
    def setTipo_Contrato(self,Tipo_Contrato):
        self.__Tipo_Contrato=Tipo_Contrato
        
    def getTipo_Contrato(self):
        return self.__Tipo_Contrato
    
    def setTipo_Jornada(self,Tipo_Jornada):
        self.__Tipo_Jornada=Tipo_Jornada
        
    def getTipo_Jornada(self):
        return self.__Tipo_Jornada
        
