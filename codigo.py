import sqlite3
import pandas as pd

from abc import abstractmethod,ABC
from dataclasses import dataclass
from typing import Optional,Dict,List,Union,Type

@dataclass   
class ConcursoDatos:   
            Escuelas_Disponibles=["Josue Pais Garcia","Rafael Orejon Forment","Frank Pais Garcia"]
            Concursos_Disponibles=[
                "Español Literatura",
                "Fisica",
                "Geografia",
                "Quimica",
                "Matematica",
                "Historia"
            ]
            Fechas_De_Concurso=["18/1/2025","22/1/2025","24/1/2025","26/1/2025","29/1/2025","1/2/2025"]
            Escuela_1=[5,7,8,3,2,7,8]
            Escuela_2=[8,4,5,8,3,6,7]
            Escuela_3=[10,4,5,7,4,9,7]
            #Numero de participantes contenido en una lista con varios obj dependiendo 
            # del numero del concurso,  
            # y la escuela que corresponda
            Numero_de_Particpantes=[
                #Escuela[Indice] = Numero de estudiantes dependiendo el indice del numero del concurso 
                {
                  'Concurso_1':[Escuela_1[0] + Escuela_2[0] + Escuela_3[0]]
                },
                {
                  'Concurso_2':[Escuela_1[0] + Escuela_2[0] + Escuela_3[0]]
                },
                {
                  'Concurso_3':[Escuela_1[2] + Escuela_2[2] + Escuela_3[2]]
                },
                {
                  'Concurso_4':[Escuela_1[2] + Escuela_2[2] + Escuela_3[2]]
                },
                {
                  'Concurso_5':[Escuela_1[4] + Escuela_2[4] + Escuela_3[4]]
                },
                {
                  'Concurso_6':[Escuela_1[5] + Escuela_2[5] + Escuela_3[5]] 
                }       
            ]
    

class Concursante(ConcursoDatos,ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.nombre:str=input("Diganos su nombre para inscribirlo: ")
        self.apellido:str=input("Cual es su apellido: ")
        self.concurso:str=input("Diganos el nombre  del concurso en que desea inscribirse: ")
        self.escuela:str=input("De que escuela es usted: ")    
    @abstractmethod 
    def _Registrarse(self)->None:
          numero_De_escuelas=ValidarDatos()._ValidarEscuela()
          if  numero_De_escuelas != 0 | numero_De_escuelas != 1 | numero_De_escuelas !=2:    
            for i_concurso in ConcursoDatos().Concursos_Disponibles:  
             while self.concurso.lower() != i_concurso.lower():
               print("No ahi ningun concurso con ese nombre")
               return
             while self.concurso.lower() == i_concurso.lower():
              print("Te hemos inscrito en la lista")
              concurso_fecha=ConcursoDatos().Fechas_De_Concurso
              caract_concurso_Fecha=len(ConcursoDatos().Fechas_De_Concurso)
              if caract_concurso_Fecha == 0:
                  return [concurso_fecha[0],self.concurso,Concursante.Numero_de_Particpantes[0][f'Concurso_{caract_concurso_Fecha+1}'][numero_De_escuelas]]
              elif caract_concurso_Fecha ==1:
                  return [concurso_fecha[1],self.concurso,Concursante.Numero_de_Particpantes[1][f'Concurso_{caract_concurso_Fecha+1}'][numero_De_escuelas]]
              elif caract_concurso_Fecha ==2:
                  return [concurso_fecha[2],self.concurso,Concursante.Numero_de_Particpantes[2][f'Concurso_{caract_concurso_Fecha+1}'][numero_De_escuelas]]
              elif caract_concurso_Fecha ==3:
                  return [concurso_fecha[3],self.concurso,Concursante.Numero_de_Particpantes[3][f'Concurso_{caract_concurso_Fecha+1}'][numero_De_escuelas]]
              elif caract_concurso_Fecha ==4:
                  return [concurso_fecha[4] ,self.concurso,Concursante.Numero_de_Particpantes[4][f'Concurso_{caract_concurso_Fecha+1}'][numero_De_escuelas]]
              elif caract_concurso_Fecha ==5:
                  return [concurso_fecha[5],self.concurso,Concursante.Numero_de_Particpantes[5][f'Concurso_{caract_concurso_Fecha+1}'][numero_De_escuelas]]
              else :
                  return "No se pudo retornar  ningun valor"
          else:
                print("Lo sentimos no tenemos vacantes para esa escuela")            
           
       
    @abstractmethod
    def _GuardarDatos(self)->None:
        with sqlite3.connect("base_de_datos.db") as coon:
                datos_del_concurso=self._Registrarse()
                fecha=datos_del_concurso[0]
                concurso=datos_del_concurso[1]
                Participantes=datos_del_concurso[2]
                
            
                datos=coon.cursor()
                datos.execute(f'''INSERT INTO Estudiante (Nombre,Apellido,Escuela) VALUES
                                 ("{self.nombre}","{self.apellido}","{self.escuela}")
                              ''')
                datos.execute('SELECT * FROM Estudiante')
                res=pd.DataFrame(datos)
                ClaveOrdenada=res.sort_values(4,ascending=False)
                ClaveForanea=ClaveOrdenada[4]
                datos.execute(f'''
                            INSERT INTO Concursos (Inscripcion_ID,Fecha_de_Concurso,Numero_de_Participantes) VALUES
                            ("{ClaveForanea}","{Validar("str")}","{fecha}","{concurso}","{Participantes}")
                              ''')          
                datos.fetchall()                
class ValidarDatos(Concursante):
      
    def _ValidarEscuela(self)->int:
              numero_De_escuelas:int
              for i_escuela in ConcursoDatos().Escuelas_Disponibles:
                 if self.escuela == i_escuela: 
                    if self.escuela == "Josue Pais Garcia":
                       numero_De_escuelas = 0
                    elif self.escuela ==  "Rafael Orejon Forment":
                       numero_De_escuelas = 1
                    elif self.escuela ==  "Frank Pais Garcia":
                        numero_De_escuelas =2
                 else: 
                   print("Escuela no disponible")     
                 return numero_De_escuelas          
                            
class EjecutarSistema(ValidarDatos):
    def __init__(self):
        super().__init__()
    @property
    def _Registrarse(self):
        return Concursante()._Registrarse()
    @property
    def _GuardarDatos(self):
        return Concursante()._GuardarDatos()
                              
Aryan=EjecutarSistema()
    
def Validar(Arg_val:Optional[str])->None:
    fecha_concurso=Aryan._Registrarse
    concurso_y_Fecha:List[str]=[]
           
            
    while Arg_val == "str":
          if fecha_concurso[0] ==0:
           return concurso_y_Fecha[fecha_concurso[0]]
          elif fecha_concurso[1] ==1:
           return concurso_y_Fecha[fecha_concurso[0]]
          elif fecha_concurso[2] ==2:
           return concurso_y_Fecha[fecha_concurso[0]]
          elif fecha_concurso[3] ==3:
           return concurso_y_Fecha[fecha_concurso[0]]
          elif fecha_concurso[4] ==4:
           return concurso_y_Fecha[fecha_concurso[0]]
          elif fecha_concurso[5] ==5:
           return concurso_y_Fecha[fecha_concurso[0]]
          else :
           return "No se pudo validar la fecha del concurso"
    
  
    



       
