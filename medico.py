class Medico:
    def __init__(self, nome):
        self.nome = nome

    def atenderPaciente(self):
        return "Realizando atendimento."

class Cardiologista(Medico):
    def atenderPaciente(self):
        return "está realizando um eletrocardiograma."
    
class Oncologista(Medico):
    def atenderPaciente(self):
        return "diagnosticando a paciente com câncer de pele."
    
class Neurologista(Medico):
    def atenderPaciente(self):
        return "certo de que o paciente possui transtorno dissociativo."
    
    #----------------------------------------------

cardiologista = Cardiologista("Dra. Nise")
oncologista = Oncologista("Dr. José")
neurologista = Neurologista("Dr. Erick")

def listarAtendimentos(medicos):
    for medico in medicos:
        print(f"O(A) {medico.nome} está {medico.atenderPaciente()}")

if __name__ == "__main__":
    cardiologista = Cardiologista("Dra. Nise")
    oncologista = Oncologista("Dr. José")
    neurologista = Neurologista("Dr. Erick")

    lista_de_medicos = [cardiologista, oncologista, neurologista]
    listarAtendimentos(lista_de_medicos)