import json
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f"Nome: {self._nome}"

class Medico(Pessoa):
    def __init__(self, crm, nome):
        super().__init__(nome)
        self._crm = crm
        self._disponivel = True

    @property
    def crm(self):
        return self._crm

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, disponibilidade):
        self._disponivel = disponibilidade

    @abstractmethod
    def especialidade(self):
        pass

    def marcar_consulta(self):
        if self._disponivel:
            self._disponivel = False
            print(f"O médico {self._nome} ({self._crm}) foi marcado para consulta!")
        else:
            print(f"O médico {self._nome} ({self._crm}) não está disponível.")

    def cancelar_consulta(self):
        self._disponivel = True
        print(f"A consulta com o médico {self._nome} ({self._crm}) foi cancelada!")

    def to_dict(self):
        return {
            "crm": self._crm,
            "nome": self._nome,
            "especialidade": self.especialidade(),
            "disponivel": self._disponivel
        }

    @classmethod
    def from_dict(cls, dados):
        especialidade = dados["especialidade"]
        if especialidade == "Cardiologia":
            medico = Cardiologista(dados["crm"], dados["nome"])
        elif especialidade == "Dermatologia":
            medico = Dermatologista(dados["crm"], dados["nome"])
        elif especialidade == "Ortopedia":
            medico = Ortopedista(dados["crm"], dados["nome"])
        elif especialidade == "Pediatria":
            medico = Pediatra(dados["crm"], dados["nome"])
        elif especialidade == "Neurologia":
            medico = Neurologista(dados["crm"], dados["nome"])
        elif especialidade == "Ginecologia":
            medico = Ginecologista(dados["crm"], dados["nome"])
        medico.disponivel = dados["disponivel"]
        return medico

    def __str__(self):
        status = "Disponível" if self._disponivel else "Indisponível"
        return f"Nome: {self._nome}, CRM: {self._crm}, Especialidade: {self.especialidade()}, Status: {status}"

class Cardiologista(Medico):
    def especialidade(self):
        return "Cardiologia"

class Dermatologista(Medico):
    def especialidade(self):
        return "Dermatologia"

class Ortopedista(Medico):
    def especialidade(self):
        return "Ortopedia"

class Pediatra(Medico):
    def especialidade(self):
        return "Pediatria"

class Neurologista(Medico):
    def especialidade(self):
        return "Neurologia"

class Ginecologista(Medico):
    def especialidade(self):
        return "Ginecologia"

class SistemaHospital:
    def __init__(self):
        self._medicos = self.inicializar_medicos()

    def inicializar_medicos(self):
        return [
            Cardiologista("37293", "Dr. Chase"),
            Dermatologista("67890", "Dr. Taub"),
            Ortopedista("11223", "Dr. Wilson"),
            Pediatra("40981", "Dra. Cameron"),
            Neurologista("22801", "Dr. Foreman"),
            Ginecologista("11359", "Dr. House")
        ]

    def listar_medicos(self):
        for i, medico in enumerate(self._medicos):
            print(f"{i + 1}. {medico}")

    def marcar_consulta(self, indice_medico):
        try:
            medico = self._medicos[indice_medico - 1]
            medico.marcar_consulta()
            self.salvar_dados("dados_medicos.json")  
        except IndexError:
            print("Médico inválido.")

    def cancelar_consulta(self, indice_medico):
        try:
            medico = self._medicos[indice_medico - 1]
            medico.cancelar_consulta()
            self.salvar_dados("dados_medicos.json")  
        except IndexError:
            print("Médico inválido.")

    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump([medico.to_dict() for medico in self._medicos], arquivo, indent=4)
        print("Dados salvos com sucesso!")

    def carregar_dados(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
                self._medicos = [Medico.from_dict(medico) for medico in dados]
            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado.")

def main():
    sistema = SistemaHospital()
    nome_arquivo = "dados_medicos.json"  
    sistema.carregar_dados(nome_arquivo)  

    while True:
        print("\nSeja bem vindo ao hospital escola Princeton Plaisboro!")
        print("1) Listar médicos")
        print("2) Marcar consulta")
        print("3) Cancelar consulta")
        print("4) Salvar dados")
        print("5) Carregar dados")
        print("6) Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            sistema.listar_medicos()
            input("\nPressione Enter para voltar ao menu...")  

        elif escolha == '2':
            sistema.listar_medicos()
            try:
                indice_medico = int(input("\nEscolha o número do médico para marcar consulta: "))
                sistema.marcar_consulta(indice_medico)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif escolha == '3':
            sistema.listar_medicos()
            try:
                indice_medico = int(input("\nEscolha o número do médico para cancelar consulta: "))
                sistema.cancelar_consulta(indice_medico)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif escolha == '4':
            sistema.salvar_dados(nome_arquivo)

        elif escolha == '5':
            sistema.carregar_dados(nome_arquivo)

        elif escolha == '6':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
