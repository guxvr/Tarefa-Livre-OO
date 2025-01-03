class Medico:
    def __init__(self, nome, crm, hospital):
        self.__nome = nome       
        self.__crm = crm         
        self.__hospital = hospital  

    
    @property
    def nome(self):
        return self.__nome

  
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string não vazia.")
    
    @property
    def crm(self):
        return self.__crm

    @crm.setter
    def crm(self, novo_crm):
        if isinstance(novo_crm, int) and novo_crm > 0:
            self.__crm = novo_crm
        else:
            raise ValueError("O CRM deve ser um número inteiro positivo.")

    @property
    def hospital(self):
        return self.__hospital

    @hospital.setter
    def hospital(self, novo_hospital):
        if isinstance(novo_hospital, str) and len(novo_hospital) > 0:
            self.__hospital = novo_hospital
        else:
            raise ValueError("O nome do hospital deve ser uma string não vazia.")

    def atender_paciente(self):
        return "Realizando atendimento genérico."


class Cardiologista(Medico):
    def atender_paciente(self):
        return "Realizando exames cardíacos e avaliando o coração."


class Pediatra(Medico):
    def atender_paciente(self):
        return "Cuidando da saúde das crianças."


class Dermatologista(Medico):
    def atender_paciente(self):
        return "Tratando de problemas de pele."


def listar_atendimentos(medicos):
    for medico in medicos:
        print(f"O Dr(a). {medico.nome} ({medico.crm}) do hospital {medico.hospital} está: {medico.atender_paciente()}")


if __name__ == "__main__":
    cardiologista = Cardiologista("Dra. Alice", 12345, "Hospital Central")
    pediatra = Pediatra("Dr. João", 67890, "Hospital Infantil")
    dermatologista = Dermatologista("Dr. Marcos", 11223, "Hospital Dermatológico")

    lista_de_medicos = [cardiologista, pediatra, dermatologista]
    listar_atendimentos(lista_de_medicos)
