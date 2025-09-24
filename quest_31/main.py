# 31) Crie uma classe chamada Playlist. Esta classe deve ter um atributo "privado" _musicas que deve ser uma lista de strings.
# Implemente os seguintes métodos: Um getter para o atributo _musicas. 
# Um setter para o atributo _musicas que valida as seguintes condições: O valor de entrada deve ser do tipo list.
# A lista não pode estar vazia. Se estiver, imprima uma mensagem de erro. Cada item na lista deve ser do tipo str.

class Playlist:
  def __init__(self, musicas):
    self.__musicas = []
    self.musicas = musicas
  @property
  def musicas(self):
     return self.__musicas

  @musicas.setter
  def musicas(self, nova_lista):
   if not isinstance(nova_lista, list):
     print("Erro: O valor deve ser uma lista.")
     return
   if not nova_lista:
     print(f"Erro: A lista não pode estar vazia ")
     return
   if not all(isinstance(musica, str) for musica in nova_lista):
            print("Erro: Todos os itens da lista devem ser strings.")
            return
   self.__musicas = nova_lista

playlist = Playlist(["Eu Navegarei"])

print(f"Lista de musicas:", playlist.musicas)
playlist.musicas = []
playlist.musicas = "  "
playlist.musicas = [123]
        
       