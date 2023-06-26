from Usuario import*

class Aspirante (Usuario):
    def __init__(self, Id: int, Nombre: str, Documento:int, Telefono: int, Correo: str):
        Usuario.__init__(self,Id, Nombre, Telefono, Correo)
        self.__tipo = []
        self.__name_institucion = []
        self.__titulacion = []
        self.__fecha_fin = []
        self.__fecha_inicio_ex = []
        self.__fecha_fin_ex = []
        self.__name_empresa = []
        self.__funciones = []
        self.__cargo = []