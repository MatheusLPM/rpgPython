from Classes.Atributo import Atributo

class Raca(Atributo):
    def __init__(self, atributoUnico, nome, debuff, descricao, forca = 0, vigor = 0, inteligencia = 0, sorte = 0, destreza = 0, mana = 0, stamina = 0):
        super().__init__(forca, vigor, inteligencia, sorte, destreza, mana, stamina)
        self._atributoUnico = atributoUnico
        self._nome = nome
        self._debuff = debuff
        self._descricao = descricao

    def __str__(self):
        atributos = super().__str__()
        return f"{atributos},{self._atributoUnico},{self._nome},{self._debuff},{self._descricao}"

    def getAtributoUnico(self):
        return self._atributoUnico

    def setAtributoUnico(self, valor: str):
        self._atributoUnico = valor

    def getNome(self):
        return self._nome

    def setNome(self, valor: str):
        self._nome = valor

    def getDebuff(self):
        return self._debuff

    def setDebuff(self, valor: str):
        self._debuff = valor

    def getDescricao(self):
        return self._descricao

    def setDescricao(self, valor: str):
        self._descricao = valor
