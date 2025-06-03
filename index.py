import sys
import os

from Classes.Item import Item
from Classes.Arma import Arma
from Classes.Classe import Classe
from Classes.Raca import Raca
from Classes.Personagem import Personagem
from Classes.Inventario import Inventario

from Classes.factory import RpgObjectFactory  # Importando a factory

personagens = []
itens = []
armas = []
classes = []
racas = []

def limparTela():
    os.system("cls" if os.name == "nt" else "clear") 

def menuPrincipal():
    print('===== MENU PRINCIPAL =====')
    print("[0] - Sair")
    print("[1] - Criar Personagem")
    if personagens:
        print("[2] - Gerenciar Personagem")
    print("[3] - Gerenciar Jogo")
    print('==========================')
    opc = input("Escolha uma opção: ")

    validOptions = ['0', '1', '3']
    if personagens:
        validOptions.append('2')

    if opc not in validOptions:
        print("Opção inválida ou indisponível no momento.")
        return -1

    return int(opc)

def submenuGerenciarPersonagem():
    print('--- Gerenciar Personagem ---')
    print("[0] - Voltar")
    print("[1] - Mostrar status do personagem")
    if itens or armas:
        print("[2] - Adicionar item ao inventário")
        validOptions = ['0', '1', '2']
    else:
        print("[2] - Adicionar item ao inventário (Indisponível - nenhum item ou arma criado)")
        validOptions = ['0', '1']

    opc = input("Escolha uma opção: ")
    if opc not in validOptions:
        print("Opção inválida ou indisponível no momento.")
        return -1
    return int(opc)

def submenuGerenciarJogo():
    print('--- Gerenciar Jogo ---')
    print("[0] - Voltar")
    print("[1] - Listar")
    print("[2] - Criar")
    print('---------------------')
    opc = input("Escolha uma opção: ")
    return int(opc) if opc.isdigit() else -1

def submenuListarObjetos():
    print('--- Listar Objetos ---')
    print("[0] - Voltar")
    print("[1] - Listar Raças")
    print("[2] - Listar Classes")
    print("[3] - Listar Itens")
    print("[4] - Listar Armas")
    print('---------------------')
    opc = input("Escolha uma opção: ")
    return int(opc) if opc.isdigit() else -1

def submenuCriarObjetos():
    print('--- Criar Objetos ---')
    print("[0] - Voltar")
    print("[1] - Criar Raça")
    print("[2] - Criar Classe")
    print("[3] - Criar Item")
    print("[4] - Criar Arma")
    print('---------------------')
    opc = input("Escolha uma opção: ")
    return int(opc) if opc.isdigit() else -1

def listarRacas():
    if not racas:
        print("Nenhuma raça criada.")
    else:
        print("Raças:")
        for idx, raca in enumerate(racas):
            print(f"[{idx}] {raca.getNome()}")

def listarClasses():
    if not classes:
        print("Nenhuma classe criada.")
    else:
        print("Classes:")
        for idx, classe in enumerate(classes):
            print(f"[{idx}] {classe.getNome()}")

def listarItens():
    if not itens:
        print("Nenhum item criado.")
    else:
        print("Itens:")
        for idx, item in enumerate(itens):
            print(f"[{idx}] {item.getNome()}")

def listarArmas():
    if not armas:
        print("Nenhuma arma criada.")
    else:
        print("Armas:")
        for idx, arma in enumerate(armas):
            print(f"[{idx}] {arma.getNome()}")

def criarItem():
    print("=== Criar Item ===")
    nome = input("Nome do item: ")
    peso = float(input("Peso: "))
    preco = float(input("Preço: "))
    descricao = input("Descrição: ")
    raridade = input("Raridade: ")
    tipo = input("Tipo: ")
    item = RpgObjectFactory.criar_item(nome, peso, preco, descricao, raridade, tipo)
    itens.append(item)
    print(f"Item '{nome}' criado e adicionado à lista de itens.")

def criarArma():
    if not itens:
        print("Nenhum item criado ainda. Crie um item antes de criar uma arma.")
        return

    print("Itens disponíveis:")
    for idx, item in enumerate(itens):
        print(f"[{idx}] {item.getNome()}")

    idxItem = int(input("Escolha o índice do item para associar à arma: "))
    itemSelecionado = itens.pop(idxItem)

    dano = float(input("Dano: "))
    durabilidade = int(input("Durabilidade: "))
    nivel = int(input("Nível: "))

    arma = RpgObjectFactory.criar_arma(itemSelecionado, dano, durabilidade, nivel)
    armas.append(arma)
    print(f"Arma '{arma.getNome()}' criada e associada ao item '{itemSelecionado.getNome()}'.")

def criarClasse():
    print("=== Criar Classe ===")
    nome = input("Nome da classe: ")
    armaUnica = input("Arma única da classe: ")
    descricao = input("Descrição da classe: ")
    classe = RpgObjectFactory.criar_classe(nome, armaUnica, descricao)
    classes.append(classe)
    print(f"Classe '{nome}' criada e adicionada à lista de classes.")

def criarRaca():
    print("=== Criar Raça ===")
    atributoUnico = input("Atributo único da raça: ")
    nome = input("Nome da raça: ")
    debuff = input("Debuff da raça: ")
    descricao = input("Descrição da raça: ")
    
    try:
        print("=== Adicionar Atributos ===")
        forca = int(input("Força: "))
        vigor = int(input("Vigor: "))
        inteligencia = int(input("Inteligência: "))
        sorte = int(input("Sorte: "))
        destreza = int(input("Destreza: "))
        mana = int(input("Mana: "))
        stamina = int(input("Stamina: "))
    except ValueError:
        print("Entrada inválida. Usando valor padrão 0 para atributos.")
        forca = vigor = inteligencia = sorte = destreza = mana = stamina = 0

    raca = RpgObjectFactory.criar_raca(atributoUnico, nome, debuff, descricao,
                                       forca, vigor, inteligencia, sorte, destreza, mana, stamina)
    racas.append(raca)
    print(f"Raça '{nome}' criada e adicionada à lista de raças.")

def criarPersonagem():
    print("=== Criar Personagem ===")
    if not racas:
        print("Não há raças criadas. Crie uma raça primeiro no Gerenciar Jogo.")
        return
    if not classes:
        print("Não há classes criadas. Crie uma classe primeiro no Gerenciar Jogo.")
        return
    nome = input("Nome do personagem: ")
    altura = float(input("Altura (m): "))
    sexo = input("Sexo: ")
    nivel = int(input("Nível: "))
    idade = int(input("Idade: "))
    print("\nRaças disponíveis:")
    for idx, raca in enumerate(racas):
        print(f"[{idx}] {raca.getNome()}")
    idxRaca = int(input("Escolha o índice da raça: "))
    racaSel = racas[idxRaca]
    print("\nClasses disponíveis:")
    for idx, classe in enumerate(classes):
        print(f"[{idx}] {classe.getNome()}")
    idxClasse = int(input("Escolha o índice da classe: "))
    classeSel = classes[idxClasse]

    inventario = Inventario(capacidade = 10)

    personagem = RpgObjectFactory.criar_personagem(nome, altura, sexo, nivel, idade, classeSel, racaSel, inventario)
    personagens.append(personagem)
    print(f"Personagem '{nome}' criado com sucesso.")

def mostrarStatusPersonagem():
    if not personagens:
        print("Nenhum personagem criado.")
        return
    print("Personagens disponíveis:")
    for idx, p in enumerate(personagens):
        print(f"[{idx}] {p.getNome()} (Nível {p.getNivel()})")
    idxP = int(input("Escolha o índice do personagem: "))
    p = personagens[idxP]
    p.mostrarStatus()

def adicionarItemPersonagem():
    if not personagens:
        print("Nenhum personagem criado.")
        return
    if not itens and not armas:
        print("Nenhum item ou arma criado para adicionar.")
        return
    print("Personagens disponíveis:")
    for idx, p in enumerate(personagens):
        print(f"[{idx}] {p.getNome()}")
    idxP = int(input("Escolha o índice do personagem: "))
    personagem = personagens[idxP]

    print("Itens disponíveis:")
    for idx, item in enumerate(itens):
        print(f"[I{idx}] {item.getNome()}")
    print("Armas disponíveis:")
    for idx, arma in enumerate(armas):
        print(f"[A{idx}] {arma.getNome()}")

    escolha = input("Escolha o código do item/arma para adicionar (ex: I0, A1): ").strip()
    if escolha.startswith('I'):
        idxItem = int(escolha[1:])
        itemSel = itens[idxItem]
    elif escolha.startswith('A'):
        idxArma = int(escolha[1:])
        itemSel = armas[idxArma]
    else:
        print("Escolha inválida.")
        return

    inventario = personagem.getInventario()
    if inventario.inserirItem(itemSel):
        print(f"Item '{itemSel.getNome()}' adicionado ao inventário do personagem '{personagem.getNome()}'.")
    else:
        print("Inventário cheio!")

def gerenciarPersonagem():
    while True:
        opc = submenuGerenciarPersonagem()
        if opc == -1:
            input("Pressione Enter para continuar...")
            limparTela()
            continue

        limparTela()
        match opc:
            case 0:
                break
            case 1:
                mostrarStatusPersonagem()
            case 2:
                adicionarItemPersonagem()
            case _:
                print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        limparTela()

def gerenciarJogo():
    while True:
        opc = submenuGerenciarJogo()
        if opc == -1:
            input("Pressione Enter para continuar...")
            limparTela()
            continue

        limparTela()
        match opc:
            case 0:
                break
            case 1:
                while True:
                    opcListar = submenuListarObjetos()
                    limparTela()
                    match opcListar:
                        case 0:
                            break
                        case 1:
                            listarRacas()
                        case 2:
                            listarClasses()
                        case 3:
                            listarItens()
                        case 4:
                            listarArmas()
                        case _:
                            print("Opção inválida.")
                    input("\nPressione Enter para continuar...")
                    limparTela()
            case 2:
                while True:
                    opcCriar = submenuCriarObjetos()
                    limparTela()
                    match opcCriar:
                        case 0:
                            break
                        case 1:
                            criarRaca()
                        case 2:
                            criarClasse()
                        case 3:
                            criarItem()
                        case 4:
                            criarArma()
                        case _:
                            print("Opção inválida.")
                    input("\nPressione Enter para continuar...")
                    limparTela()
            case _:
                print("Opção inválida.")
                input("\nPressione Enter para continuar...")
                limparTela()

def main():
    while True:
        opc = menuPrincipal()
        if opc == -1:
            input("Pressione Enter para continuar...")
            limparTela()
            continue

        limparTela()
        match opc:
            case 0:
                print("Saindo...")
                sys.exit()
            case 1:
                criarPersonagem()
            case 2:
                gerenciarPersonagem()
            case 3:
                gerenciarJogo()
            case _:
                print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        limparTela()

if __name__ == "__main__":
    main()
