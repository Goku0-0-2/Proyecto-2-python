class Persona:
    def __init__(self):
        self.nombre=input("Diganos su nombre para inscribirlo")
        self.apellido=input("Cual es su apellido")
        self.concurso=input("Diganos el numero de lista del concurso en que desea inscribirse")
        self.escuela=input("De que escuela es usted")
    def __Verificar(self):
            Escuelas_Disponibles=["Josue Pais Garcia","Rafael Orejon Forment","Frank Pais Garcia"]
            Concursos_Disponibles={
                1:"Español Literatura",
                2:"Fisica",
                3:"Geografia",
                4:"Quimica",
                5:"Matematica",
                6:"Historia"
            }
            
            while (self.escuela.lower() == Escuelas_Disponibles[0].lower()) | (self.escuela.lower() == Escuelas_Disponibles[1].lower()) | (self.escuela.lower() == Escuelas_Disponibles[2].lower()):
                print("Tenemos bacantes para escuela")
                if (self.concurso.lower() != Concursos_Disponibles[1].lower()) | (self.concurso.lower() != Concursos_Disponibles[2].lower()) | (self.concurso.lower() != Concursos_Disponibles[3].lower()) | (self.concurso.lower() != Concursos_Disponibles[4].lower())  | (self.concurso.lower() != Concursos_Disponibles[5].lower()) | (self.concurso.lower() != Concursos_Disponibles[6].lower()):
                    concurso_validar="Correcto"
                    return concurso_validar
                else:
                    concurso_validar="Incorrecto"
                    return concurso_validar
            while  (self.escuela != Escuelas_Disponibles[0]) | (self.escuela != Escuelas_Disponibles[1]) | (self.escuela != Escuelas_Disponibles[2]):
                 print("No tenemos vancantes para esa escuela ")
                 break
    def  _Validar(self,conco):
        concurso=self.__Verificar()
        
        while concurso == "Correcto":
            print(f"Te has inscrito en el concurso de {self.concurso}")
            while self.concurso == 1:
                return
        while concurso != "Correcto":
            print(f"Lo sentimos no ahi ningun concurso con ese numero")
    def GuardarDatos(self):
        print()
        
                    