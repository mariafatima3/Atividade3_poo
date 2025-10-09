# 34) Crie uma classe CarrinhoDeCompras com um atributo "privado" _itens (uma lista) e um atributo _total (inicializado em 0).
# Implemente um setter para o atributo _itens que: Substitua a lista atual de itens pela nova lista fornecida.
# Após a substituição, chame um método interno (por exemplo, _recalcular_total()) que recalcule o valor total dos itens e atualize o atributo _total. 
# Considere que cada item é um dicionário com chaves como 'nome' e 'preco'.

class CarrinhoDeCompras:
    def __init__(self):
        self._itens = []
        self._total = 0
    @property
    def itens(self):
        return self._itens
    @itens.setter
    def itens(self, nova_lista_itens):
        self._itens = nova_lista_itens
        self._recalcular_total()

    @property
    def total(self):
     return self._total
 
    def _recalcular_total(self):
        self._total = sum(item.get('preco', 0) for item in self._itens)

    def adicionar_item(self, item):
       self._itens.append(item)
       self._recalcular_total()

    def remover_item(self, nome):
        for item in self._itens:
            if item.get('nome') == nome:
                self._itens.remove(item)
                self._recalcular_total()
                return
        print(f"Item '{nome}' não encontrado no carrinho.")


carrinhoDeCompras = CarrinhoDeCompras()
carrinhoDeCompras.adicionar_item({'nome': 'Notebook', 'preco': 3500.00})
print(f"Itens no carrinho: {carrinhoDeCompras.itens}")
print(f"Total: R${carrinhoDeCompras.total:.2f}")

nova_lista_itens = [{'nome': 'Mouse', 'preco': 180.00}, {'nome': 'Mochila', 'preco':190.00}]
carrinhoDeCompras.itens = nova_lista_itens
print(f"Itens da nova lista: {carrinhoDeCompras.itens}")
print(f"Total da nova lista: {carrinhoDeCompras.total:.2f}")

carrinhoDeCompras.remover_item('Mochila')
print(f"Itens no carrinho após remover Mochila: {carrinhoDeCompras.itens}")
print(f"Total do carrinho após remover Mochila: {carrinhoDeCompras.total:.2f}")
