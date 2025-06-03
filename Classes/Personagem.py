from Classes.Classe import Classe
from Classes.Raca import Raca
from Classes.Inventario import Inventario

class Personagem:
    def __init__( self, nome, altura, sexo, nivel, idade, classe: Classe, raca: Raca, inventario: Inventario,):
        self._nome = nome
        self._altura = altura
        self._sexo = sexo
        self._nivel = nivel
        self._idade = idade
        self._classe = classe
        self._raca = raca
        self._inventario = inventario

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getAltura(self):
        return self._altura

    def setAltura(self, altura):
        self._altura = altura

    def getSexo(self):
        return self._sexo

    def setSexo(self, sexo):
        self._sexo = sexo

    def getNivel(self):
        return self._nivel

    def setNivel(self, nivel):
        self._nivel = nivel

    def getIdade(self):
        return self._idade

    def setIdade(self, idade):
        self._idade = idade

    def getClasse(self) -> Classe:
        return self._classe

    def setClasse(self, classe: Classe):
        self._classe = classe

    def getRaca(self) -> Raca:
        return self._raca

    def setRaca(self, raca: Raca):
        self._raca = raca

    def getInventario(self) -> Inventario:
        return self._inventario

    def setInventario(self, inventario: Inventario):
        self._inventario = inventario
        
    def mostrarStatus(self):
        print("\n--- Status do Personagem ---")
        print(f"Nome: {self.getNome()}")
        print(f"Nível: {self.getNivel()}")
        print(f"Altura: {self.getAltura()}")
        print(f"Sexo: {self.getSexo()}")
        print(f"Idade: {self.getIdade()}")
        print(f"Raça: {self.getRaca().getNome()}")
        print(f"Classe: {self.getClasse().getNome()}")
        print("\n--- Atributos da Raça ---")
        raca = self.getRaca()
        print(f"Força: {raca.get_forca()}")
        print(f"Vigor: {raca.get_vigor()}")
        print(f"Inteligência: {raca.get_inteligencia()}")
        print(f"Sorte: {raca.get_sorte()}")
        print(f"Destreza: {raca.get_destreza()}")
        print(f"Mana: {raca.get_mana()}")
        print(f"Stamina: {raca.get_stamina()}")
        print("\nInventário:")
        itens = self.getInventario().getItens()  # pega lista de itens
        if itens:
            for item in itens:
                print(f"- {item.getNome()}")
        else:
            print("Inventário vazio.")
