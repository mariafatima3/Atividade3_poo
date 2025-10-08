# 32) Crie uma classe Retangulo com dois atributos "privados": _largura e _altura.
# Implemente setters para _largura e _altura que garantam que os valores sejam numéricos e maiores que zero.
# Em seguida, crie uma propriedade apenas de leitura chamada area usando @property. 
# Esta propriedade deve calcular e retornar a área do retângulo, mas não deve permitir que o usuário defina seu valor diretamente.

class Retangulo:
    def __init__(self, largura, altura):
       self.largura = largura
       self.altura = altura
    
    @property
    def largura(self):
        return self._largura
    @largura.setter
    def largura(self,valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self._largura = valor
        else:
            raise  ValueError("A largura deve ser maior que zero.")
            
    @property
    def altura(self):
        return self._altura 
    @altura.setter
    def altura(self, valor):
         if isinstance(valor, (int, float)) and valor > 0:
            self._altura = valor
         else:
             raise  ValueError("A altura deve ser maior que zero.")
         

    @property
    def area(self):
        return self.largura * self.altura 
    
retangulo = Retangulo(3,7)
print("Área do  retângulo:", retangulo.area)
    
try:
    retangulo.area = 18
except AttributeError as e:
    print("Erro ao tentar definir a área diretamente:", e)

