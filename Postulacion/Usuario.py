class Usuario:
    def __init__(self,Nombre,Documento,Telefono,Correo,Ubicacion):
        self.__Nombre=Nombre
        self.__Documento=Documento
        self.__Telefono=Telefono
        self.__Correo=Correo
        self.__Ubicacion=Ubicacion
    
    def setNombre(self,Nombre):
        self.__Nombre=Nombre
            
    def getNombre(self):
        return self.__Nombre
    
    def setDocumento(self,Documento):
        self.__Documento=Documento
        
    def getDocumento(self):
        return self.__Documento
    
    def setTelefono(self,Telefono):
        self.__Telefono=Telefono
        
    def getTelefono(self):
        return self.__Telefono
    
    def setCorreo(self,Correo):
        self.__Correo=Correo
        
    def getCorreo(self):
        return self.__Correo
    
    def setUbicacion(self,Ubicacion):
        self.__Ubicacion=Ubicacion
            
    def getUbicacion(self):
        return self.__Ubicacion
    