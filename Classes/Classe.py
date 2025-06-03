class Classe:
    def __init__(self, nome, armaUnica, descricao):
        self._nome = nome
        self._armaUnica = armaUnica
        self._descricao = descricao
        
    def __str__(self):
        return f"Nome: {self._nome}, Arma Única: {self._armaUnica}, Descrição: {self._descricao}"

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getArmaUnica(self):
        return self._armaUnica

    def setArmaUnica(self, armaUnica):
        self._armaUnica = armaUnica

    def getDescricao(self):
        return self._descricao

    def setDescricao(self, descricao):
        self._descricao = descricao
