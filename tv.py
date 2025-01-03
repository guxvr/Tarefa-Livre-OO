class Televisao:
    def __init__(self):
        self.canal = 1
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100
        self.canal_min = 1
        self.canal_max = 99
        self.ligada = False 
    
    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False
 
    def mudar_canal_para_cima(self):
        
        if not self.ligada:
            return
        if self.canal < self.canal_max:
            self.canal += 1

    def mudar_canal_para_baixo(self):

        if not self.ligada:
            return
        if self.canal > self.canal_min:
            self.canal -= 1

    def aumentar_volume(self):

        if not self.ligada:
            return
        if self.volume < self.volume_max:
            self.volume += 20

    def reduzir_volume(self):

        if not self.ligada:
            return
        if self.volume > self.volume_min:
            self.volume -= 10
#--------------------------------------------------------------------------

    def __str__(self) -> str:
        return f'Televisao - esta ligada: {self.ligada} - Canal: {self.canal} - Volume: ({self.volume})'
    
    def get_canal(self):
        return self.canal

    def set_canal(self, canal):
        self.canal = canal

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_ligada(self):
        return self.ligada

    def set_ligada(self, ligada):
        self.ligada = ligada
    

tv_teste = Televisao()

print("A TV está ligada? ", tv_teste.ligada)

tv_teste.ligar()
print(" A TV está ligada agora? ", tv_teste.ligada)


print("Canal atual:", tv_teste.canal)
tv_teste.mudar_canal_para_cima()
print("Canal atual:", tv_teste.canal)
tv_teste.mudar_canal_para_baixo()
print("Canal atual:", tv_teste.canal)

print("Volume atual:", tv_teste.volume)
tv_teste.aumentar_volume()
print("Volume atual:", tv_teste.volume)
tv_teste.reduzir_volume()
print("Volume atual:", tv_teste.volume)
