class requisicion:
    def __init__(self,id_requisicion,manual_funciones,salario,tipo_ponderacion):
        self.__id_requisicion = id_requisicion
        self.__manual_funciones = manual_funciones
        self.__tipo_ponderacion = tipo_ponderacion
        self.__salario=salario
        self.__requisitos_edu = None
        self.__vacantes = None
        self.__dependencia = None 


def setmanual_funciones (self,name:str,manual_funciones:str):
     for i in self.__manual_funciones:
        if name == i:
            indice = self.__manual_funciones.index(i)
            self.__tipo.pop(indice)
            self.__tipo.insert(indice)

def getmanual_funciones(self):
    return self.__manual_funciones

def setfecha_solicitud (self,fecha_solicitud:str):
    self.__fecha_solicitud = fecha_solicitud

def settipo_ponderacion (self,name:str,tipo_ponderacion:str):
    for i in self.__tipo_ponderacion:
        if name == i:
            indice = self.__tipo_ponderacion.index(i)
            self.__tipo.pop(indice)
            self.__tipo.insert(indice)
        
def gettipo_ponderacion (self):
    return self.__tipo_ponderacion 

def settipo_salario (self,tipo_salario:str):
    self.__tipo_salario =tipo_salario

def gettipo_salario(self):
    return self.__horario_laboral

def setsalario (self,salario:str,antiguo:str, nuevo:str):
    for i in self.__salario:
        if antiguo == i:
            indice = self.__salario.index(i)
            self.__salario.pop(indice)
            self.__salario.insert(indice, nuevo )

def seteducacion_req (self,educacion):
    self.__educacion_req = educacion

def geteducacion_req (self):
    self.__educacion_req

def setvacantes (self,vacantes):
    self.__vacantes= vacantes

def getvacantes (self):
    self.__vacantes


