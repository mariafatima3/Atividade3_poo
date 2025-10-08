# 33) Crie uma classe Bateria com um atributo "privado" _carga (que representa a porcentagem de carga, de 0 a 100).
# Implemente um setter para a _carga que valide se o valor de entrada está entre 0 e 100.
# Adicione um segundo atributo "privado" _conectado_tomada (booleano, True ou False).
# Modifique o setter da _carga para incluir a seguinte lógica:
# Se a bateria não estiver conectada à tomada (_conectado_tomada é False), a carga não pode aumentar. Ela só pode diminuir.
# Se a bateria estiver conectada (_conectado_tomada é True), a carga pode aumentar ou diminuir.

class Bateria:
    def __init__(self):
        self._carga = 0
        self._conectado_tomada = False

    @property
    def carga(self):
       return self._carga 
    @carga.setter
    def carga(self, valor):
         if not (0 <= valor <= 100):
             raise ValueError("A carga deve estar entre 0 e 100.")
         if not self._conectado_tomada and valor > self._carga:
            raise ValueError("A carga não pode aumentar sem estar conectada à tomada.")
      
         self._carga = valor

    @property
    def conectado_tomada(self):
        return self._conectado_tomada
    @conectado_tomada.setter
    def conectado_tomada(self, valor):
        if not isinstance(valor, bool):
            raise TypeError("O valor deve ser True ou False.")
        self._conectado_tomada = valor

bateria = Bateria()
bateria.conectado_tomada = True
bateria.carga = 50 
print(f"A bateria está com {bateria.carga}% de carga.")

bateria.conectado_tomada = False
try:
    bateria.carga = 80 
except ValueError as e:
    print("Erro ao carregar:", e)
