import time
class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def ajustar(self):
        self.hora = 60 * self.minuto
        self.minuto = 60 * 1

    def avancar(self):
        self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.minuto += 1
        if self.minuto == 60:
            self.minuto = 0
            self.hora += 1
        if self.hora == 24:
            self.hora = 0
            
    
    def exibir(self):
        print(f'{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}')

hora = int(input('Digite a hora: '))
minuto = int(input('Digite o minuto: '))
segundo = int(input('Digite o segundo: '))
relogio1 = Relogio(hora, minuto, segundo)
try:
    while True:
        relogio1.exibir()
        time.sleep(1)
        relogio1.avancar()
except KeyboardInterrupt:
    print("\nRelógio parado pelo usuário.")

