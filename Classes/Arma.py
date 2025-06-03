from Classes.Item import Item

class Arma(Item):
    def __init__(self, item: Item, dano, durabilidade, nivel):
        super().__init__( nome = item.getNome(), peso = item.getPeso(), preco = item.getPreco(), descricao = item.getDescricao(), raridade = item.getRaridade(), tipo = item.getTipo())
        self._dano = dano
        self._durabilidade = durabilidade
        self._nivel = nivel
        
    def __str__(self):
        atributos = super().__str__()
        return f"{atributos}, Dano: {self._dano}, Durabilidade: {self._durabilidade}, Nível: {self._nivel}"

    def getDano(self):
        return self._dano

    def setDano(self, dano):
        self._dano = dano

    def getDurabilidade(self):
        return self._durabilidade

    def setDurabilidade(self, durabilidade):
        self._durabilidade = durabilidade

    def getNivel(self):
        return self._nivel

    def setNivel(self, nivel):
        self._nivel = nivel
    
    def getTipo(self):
        return self._tipo
    
    def setTipo(self, tipo):
        self._tipo = tipo
