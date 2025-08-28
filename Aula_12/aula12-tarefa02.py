class Carro:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = ""
        self.seguro = False
        self._ligado = False
        self.placa = ""
        self.reboque = False
    
    def ligar(self):
        if self._ligado:
            print(f"\n\t [ERRO] Já está ligado \n")
        else:
                self._ligado = True
                print(f"\t\t [OK] O carro está ligado!")

    def desligar(self):
        if self._ligado:
            self._ligado = False
            print("[OK] O carro foi desligado!")
        else:
                print(f"\n\t [ERRO] Já está desligado \n")



    def exibir_info(self):
        if self._ligado:
            status = "ligado"
        else:
            status = "desligado"

        if self.seguro:
            seguro = "seguro contratado"
        else:
            seguro = "seguro cancelado"

        if self.placa :
            emplacado = "Carro emplacado"
        else: 
            emplacado = "Carro não emplacado"
        
        if self.reboque :
            reboque = "Reboque contratado"
        else: 
            reboque = "Reboque não contratado"
            
            print(f"{self.marca} - {self.modelo} - {self.seguro} - {self.reboque} está {status}")

    def seguro_contratar(self):
        if self.seguro:
            print(f"\n\t [ERRO] O seguro já foi contratado.")
        else:
            self.seguro = True
            print(f"\n\t O seguro foi contratado!")

    def seguro_cancelar(self):
        if self.seguro:
            self.seguro = False
            print(f"\n\t [OK] O seguro foi cancelado!")
        else:
                print(f"\n\t [ERRO] O seguro ja foi cancelado.")

    def info_cor(self):
        if self.cor:
            print(f"\n\t A cor do carro é [Grafite]")

    def placa_emplacar(self):
        if self.placa:
            print(f"\n\t Seu carro foi emplacado, sua placa é [ASGWE23467K]")

    def placa_cancelar(self):
        if self.placa:
            print(f"\n\t O seu carro não está emplacado!")

    def reboque_contratar(self):
        if self.reboque:
            print(f"\n\t Seu reboque foi contratado!")

    def reboque_cancelar(self):
        if self.reboque:
            print(f"\n\t Seu reboque foi cancelado!")
