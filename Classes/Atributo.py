class Atributo:
    def __init__(self, forca = 0, vigor = 0, inteligencia = 0, sorte = 0, destreza = 0, mana = 0, stamina = 0):
        self._forca = forca
        self._vigor = vigor
        self._inteligencia = inteligencia
        self._sorte = sorte
        self._destreza = destreza
        self._mana = mana
        self._stamina = stamina

    def __str__(self):
        return f"{self._forca},{self._vigor},{self._inteligencia},{self._sorte},{self._destreza},{self._mana},{self._stamina}"

    def get_forca(self):
        return self._forca

    def get_vigor(self):
        return self._vigor

    def get_inteligencia(self):
        return self._inteligencia

    def get_sorte(self):
        return self._sorte

    def get_destreza(self):
        return self._destreza

    def get_mana(self):
        return self._mana

    def get_stamina(self):
        return self._stamina

    def set_forca(self, valor):
        self._forca = valor

    def set_vigor(self, valor):
        self._vigor = valor

    def set_inteligencia(self, valor):
        self._inteligencia = valor

    def set_sorte(self, valor):
        self._sorte = valor

    def set_destreza(self, valor):
        self._destreza = valor

    def set_mana(self, valor):
        self._mana = valor

    def set_stamina(self, valor):
        self._stamina = valor