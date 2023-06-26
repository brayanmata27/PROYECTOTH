from sys import path 
path.append("c:\PROYECTOTH")
from requisicion import *
from buscador.Usuario import *
from postulacion.Empresa import *
from postulacion.Postulcaion import *
from postulacion.Educacion import *
from postulacion.Experiencia import *
ob1 = requisicion(2503, "Manual de Funciones", 2000000,"1 a 100", "Auxiliar de enfermeria",6,"laboral")
ob2 = Empresa (4, "Acarreos txt" ,1543, 332343322 , "acareos.sena.com" , "acareos expres")
ob3 = Postulacion (1028 , 10 , "10/20/2015" , "15/21/2016","2000000", "6 meses", "Indefinido")
ob4= Usuario ("Juana",53982512,"juana27@gmail.com",3222208389)
ob5 = Educacion ()
ob6 = Experiencia (2254 , 6 , "Chef" , "excelente")


print("ob1.gettipo_ponderacion")
print("ob1.geteducacion_req")