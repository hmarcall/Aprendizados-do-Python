class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def comprar(self):
          self.quantidade +=1
            
    def vender(self):
            if self.quantidade > 0:
                  self.quantidade -= 1
            else:
                  print ('Não foi possivel vender pois não há nada em estoque!')

    def valor_estoque(self):
        return self.preco * self.quantidade

    def mostrar_dados(self):
        print(f'Nome:{self.nome}\nPreço:{self.preco}\nQuantidade:{self.quantidade}\nValor em estoque:R${self.valor_estoque():.2f}')

produto1 = Produto('Coca-cola', 20, 1)
produto1.mostrar_dados()
produto1.comprar()
produto1.mostrar_dados()
produto1.vender()
produto1.mostrar_dados()