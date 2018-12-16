class Carro:
    def __init__(self, velocidade_max):
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        # if((self.velocidade_atual + delta) > self.velocidade_max):
        #     self.velocidade_atual = self.velocidade_max
        # else:
        #     self.velocidade_atual += delta
        # return self.velocidade_atual
        maxima = self.velocidade_max
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova <= maxima else maxima 
        return self.velocidade_atual


    def frear(self, delta=5):
        # if(self.velocidade_atual - delta) < 0:
        #     self.velocidade_atual = 0
        # else:
        #     self.velocidade_atual -= delta
        # return self.velocidade_atual
        maxima = self.velocidade_max
        nova = self.velocidade_atual - delta
        self.velocidade_atual = nova if nova >= 0 else 0 
        return self.velocidade_atual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))


    for _ in range(40):
        print(c1.frear())



