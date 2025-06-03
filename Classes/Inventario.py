
class Inventario:
    def __init__(self, capacidade, itens = None):
        self._capacidade = capacidade
        self._itens = itens if itens is not None else []
        
    def __str__(self):
        itens_str = ', '.join([str(item) for item in self._itens])
        return f"Capacidade: {self._capacidade}, Itens: [{itens_str}]"

    def getCapacidade(self):
        return self._capacidade

    def setCapacidade(self, capacidade):
        self._capacidade = capacidade

    def getItens(self):
        return self._itens

    def setItens(self, itens):
        self._itens = itens

    def inserirItem(self, item):
        if len(self._itens) < self._capacidade:
            self._itens.append(item)
            return True
        else:
            return False
        
    def listarItens(self):
        for item in self._itens:
            print(item)
