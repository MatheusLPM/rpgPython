from Classes.Item import Item
from Classes.Arma import Arma
from Classes.Classe import Classe
from Classes.Raca import Raca
from Classes.Personagem import Personagem

# Factory Method para criação dos métodos para que subclasses (ou classes específicas) decidam qual classe instanciar.

class RpgObjectFactory:
    @staticmethod
    def criar_item(nome, peso, preco, descricao, raridade, tipo):
        return Item(nome, peso, preco, descricao, raridade, tipo)
    
    @staticmethod
    def criar_arma(item, dano, durabilidade, nivel):
        return Arma(item, dano, durabilidade, nivel)
    
    @staticmethod
    def criar_classe(nome, arma_unica, descricao):
        return Classe(nome, arma_unica, descricao)
    
    @staticmethod
    def criar_raca(atributo_unico, nome, debuff, descricao, forca, vigor, inteligencia, sorte, destreza, mana, stamina):
        return Raca(atributo_unico, nome, debuff, descricao,
                    forca, vigor, inteligencia, sorte, destreza, mana, stamina)
    
    @staticmethod
    def criar_personagem(nome, altura, sexo, nivel, idade, classe, raca, inventario):
        return Personagem(nome, altura, sexo, nivel, idade, classe, raca, inventario)
