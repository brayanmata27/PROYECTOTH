class Experiencia:
    datos=[]
    def __init__(self,Nombre_empresa:str,Duracion:int,Cargo:str,Funciones:str):
        self.__nombre_empresa=Nombre_empresa
        self.__duracion=Duracion
        self.__cargo=Cargo
        self.__funciones=Funciones

    def setNombreE(self,nombre_empresa):
        self.__nombre_empresa=nombre_empresa
    #print(datos)

    def setDuracion(self,duracion):
        self.__duracion=[]

    def setCargo(self,cargo):
        self.__cargo=[]

    def setFunciones(self,funciones):
        self.__funciones=[]

    def getNnombreE(self):
        return self.__nombre_empresa
    
    def getDuracion(self):
        return self.__duracion
    
    def getCargo(self):
        return self.__cargo
    
    def getFunciones(self):
        return self.__funciones
    
#print(lista)

    
    