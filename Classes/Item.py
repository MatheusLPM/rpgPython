class Item():
    def __init__(self, nome, peso, preco, descricao, raridade, tipo):
        self._nome = nome
        self._peso = peso
        self._preco = preco
        self._descricao = descricao
        self._raridade = raridade
        self._tipo = tipo
        
    def __str__(self):
        return (f"Nome: {self._nome}, Peso: {self._peso}, Preço: {self._preco}, Descrição: {self._descricao}, Raridade: {self._raridade}, Tipo: {self._tipo}")

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getPeso(self):
        return self._peso

    def setPeso(self, peso):
        self._peso = peso

    def getPreco(self):
        return self._preco

    def setPreco(self, preco):
        self._preco = preco

    def getDescricao(self):
        return self._descricao

    def setDescricao(self, descricao):
        self._descricao = descricao

    def getRaridade(self):
        return self._raridade

    def setRaridade(self, raridade):
        self._raridade = raridade

    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo):
        self._tipo = tipo
