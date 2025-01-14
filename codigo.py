import sqlite3
import pandas as pd

from dataclasses import dataclass
from typing import Optional,Dict,List,Union

@dataclass   
class Datos:   
            Escuelas_Disponibles:List[str]=["Josue Pais Garcia","Rafael Orejon Forment","Frank Pais Garcia"]
            Concursos_Disponibles:Dict[str|int]={
                1:"Español Literatura".lower(),
                2:"Fisica".lower(),
                3:"Geografia".lower(),
                4:"Quimica".lower(),
                5:"Matematica".lower(),
                6:"Historia".lower()
          }
    
@dataclass           
class Persona(Datos):     
      nombre:str=input("Diganos su nombre para inscribirlo: ")
      apellido:str=input("Cual es su apellido: ")
      concurso:int|str=input("Diganos el numero de lista del concurso en que desea inscribirse: ")
      escuela:str=input("De que escuela es usted: ")
      @classmethod
      def  _Registrarse(self,concur:Optional[int])->None:    
       if self.escuela.lower() == Datos().Escuelas_Disponibles[0].lower() | self.escuela.lower() == Datos().Escuelas_Disponibles[1].lower()| self.escuela.lower() == Datos().Escuelas_Disponibles[2].lower():
           
        while self.concurso.lower() != Datos().Concursos_Disponibles[1] | self.concurso.lower() != Datos().Concursos_Disponibles[2] | self.concurso.lower() != Datos().Concursos_Disponibles[3] | self.concurso.lower() != Datos().Concursos_Disponibles[4]| self.concurso.lower() != Datos().Concursos_Disponibles[2] | self.concurso.lower() != Datos().Concursos_Disponibles[2]:
            print("No ahi ningun concurso con ese numero de lista")
            break
        while self.concurso.lower() == Datos().Concursos_Disponibles[1] | self.concurso.lower() == Datos().Concursos_Disponibles[2] | self.concurso.lower() == Datos().Concursos_Disponibles[3] | self.concurso.lower() == Datos().Concursos_Disponibles[4]| self.concurso.lower() == Datos().Concursos_Disponibles[2] | self.concurso.lower() == Datos().Concursos_Disponibles[2]:
            print("No te hemos inscrito en la lista")
            break
       else:
           print("No tenemos vacantes para esa escuela")
      @property     
      def GuardarDatos()->None:
          conectar=sqlite3.connect("base_de_datos.db")
          
          GurdarDatos='''

                 '''
               
           
        
        
        

Aryan=Persona()                 
Aryan._Registrarse()       