class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprimirVeiculo(self):
        print(f"Marca do Veículo: {self.marca}")
        print(f"Modelo do Veículo: {self.modelo}")


class Garagem:
    def __init__(self):
        self.__catalogo = [] 

    def adicionarVeiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):  # Garantindo que seja um objeto do tipo Veiculo
            self.__catalogo.append(veiculo)
            print(f"Veículo {veiculo.marca} {veiculo.modelo} adicionado com sucesso!")
        else:
            print("Erro: Apenas objetos do tipo Veiculo podem ser adicionados.")

    def removerVeiculo(self, marca, modelo):
        for veiculo in self.__catalogo:
            if veiculo.marca == marca and veiculo.modelo == modelo:
                self.__catalogo.remove(veiculo)
                print(f"Veículo {marca} {modelo} removido com sucesso.")
                return
        print(f"Veículo {marca} {modelo} não encontrado na garagem.")

    def imprimirGaragem(self):
        if not self.__catalogo:
            print("A garagem está vazia.")
            return

        print("Veículos na garagem:")
        print("-----------")
        for veiculo in self.__catalogo:
            veiculo.imprimirVeiculo()
            print("-----------")


def menu():
    garagem = Garagem()

    while True:
        print("\n--- MENU GARAGEM ---")
        print("1. Adicionar Veículo")
        print("2. Remover Veículo")
        print("3. Listar Veículos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            veiculo = Veiculo(marca, modelo)
            garagem.adicionarVeiculo(veiculo)

        elif opcao == "2":
            marca = input("Digite a marca do veículo a ser removido: ")
            modelo = input("Digite o modelo do veículo a ser removido: ")
            garagem.removerVeiculo(marca, modelo)

        elif opcao == "3":
            garagem.imprimirGaragem()

        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()
