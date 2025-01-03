import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    # Método para verificar se os lados formam um triângulo
    def __existe_triangulo(self):
        return (self.__lado1 < self.__lado2 + self.__lado3 and
                self.__lado2 < self.__lado1 + self.__lado3 and
                self.__lado3 < self.__lado1 + self.__lado2)

    # Método para calcular os cossenos dos ângulos
    def __calcular_cossenos(self):
        a, b, c = self.__lado1, self.__lado2, self.__lado3
        cos_a = ((b**2) + (c**2) - (a**2)) / (2 * b * c)
        cos_b = ((a**2) + (c**2) - (b**2)) / (2 * a * c)
        cos_c = ((b**2) + (a**2) - (c**2)) / (2 * b * a)
        return cos_a, cos_b, cos_c

    # Método público para calcular senos
    def __calcular_senos(self, cossenos):
        return [math.sqrt(1 - cos**2) for cos in cossenos]

    # Método para calcular a área e o perímetro
    def __calcular_area_e_perimetro(self):
        a, b, c = self.__lado1, self.__lado2, self.__lado3
        p = (a + b + c) / 2  # Semiperímetro
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area, 2 * p

    # Método para calcular raios dos círculos inscrito e circunscrito
    def __calcular_raios(self, area):
        p = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        r = area / p
        R = (self.__lado1 * self.__lado2 * self.__lado3) / (4 * area)
        return r, R

    # Método para determinar o tipo de triângulo
    def __determinar_tipo(self):
        a, b, c = sorted([self.__lado1, self.__lado2, self.__lado3])  # Ordena os lados
        if (b**2) > (a**2) + (c**2):
            return "Triângulo obtusângulo"
        elif (b**2) == (a**2) + (c**2):
            return "Triângulo retângulo"
        else:
            return "Triângulo acutângulo"

    # Método principal para processar o triângulo
    def processar_triangulo(self):
        if not self.__existe_triangulo():
            return "O triângulo não existe"
        
        cossenos = self.__calcular_cossenos()
        senos = self.__calcular_senos(cossenos)
        area, perimetro = self.__calcular_area_e_perimetro()
        r, R = self.__calcular_raios(area)
        tipo = self.__determinar_tipo()

        resultado = {
            "Cossenos": cossenos,
            "Senos": senos,
            "Área": area,
            "Perímetro": perimetro,
            "Raio inscrito": r,
            "Raio circunscrito": R,
            "Tipo": tipo
        }
        return resultado


# Classe para gerenciar a interação com o usuário
class InterfaceTriangulo:
    @staticmethod
    def executar():
        lado1 = float(input("Lado 1 do triângulo: "))
        lado2 = float(input("Lado 2 do triângulo: "))
        lado3 = float(input("Lado 3 do triângulo: "))

        triangulo = Triangulo(lado1, lado2, lado3)
        resultado = triangulo.processar_triangulo()

        if isinstance(resultado, str):
            print(resultado)
        else:
            print("Resultado:")
            print(f"Cossenos: {resultado['Cossenos']}")
            print(f"Senos: {resultado['Senos']}")
            print(f"Área: {resultado['Área']:.2f}")
            print(f"Perímetro: {resultado['Perímetro']:.2f}")
            print(f"Raio inscrito: {resultado['Raio inscrito']:.2f}")
            print(f"Raio circunscrito: {resultado['Raio circunscrito']:.2f}")
            print(f"Tipo: {resultado['Tipo']}")


# Executa o programa
if __name__ == "__main__":
    InterfaceTriangulo.executar()
