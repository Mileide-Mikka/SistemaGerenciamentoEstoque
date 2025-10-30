"""
Sistema de Gerenciamento de Estoque
Projeto da Faculdade Anhanguera- curso ADS
"""

# Classes para armazenar dados
class Produto:
    def __init__(self, id, nome, categoria, quantidade, preco, localizacao):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

    def mostrar_info(self):
        return f"ID: {self.id} | Nome: {self.nome} | Categoria: {self.categoria} | Quantidade: {self.quantidade} | Preco: R$ {self.preco} | Local: {self.localizacao}"

class Movimentacao:
    def __init__(self, produto_id, tipo, quantidade, data):
        self.produto_id = produto_id
        self.tipo = tipo
        self.quantidade = quantidade
        self.data = data

    def mostrar_info(self):
        return f"Produto: {self.produto_id} | Tipo: {self.tipo} | Quantidade: {self.quantidade} | Data: {self.data}"

# Listas para guardar os dados
lista_produtos = []
lista_movimentacoes = []

# Funcao para cadastrar produto
def cadastrar_produto():
    print("\n--- Cadastrar Novo Produto ---")

    id_produto = input("Digite o ID do produto: ")
    nome_produto = input("Digite o nome do produto: ")
    categoria_produto = input("Digite a categoria: ")
    quantidade_produto = int(input("Digite a quantidade: "))
    preco_produto = float(input("Digite o preco: R$ "))
    localizacao_produto = input("Digite a localizacao: ")

    # Criar novo produto
    novo_produto = Produto(id_produto, nome_produto, categoria_produto, quantidade_produto, preco_produto, localizacao_produto)
    lista_produtos.append(novo_produto)

    # Registrar a entrada no estoque
    nova_movimentacao = Movimentacao(id_produto, "entrada", quantidade_produto, "2024-07-24")
    lista_movimentacoes.append(nova_movimentacao)

    print("Produto cadastrado com sucesso!")

# Funcao para buscar produto
def buscar_produto():
    print("\n--- Buscar Produto ---")

    id_busca = input("Digite o ID do produto: ")

    for produto in lista_produtos:
        if produto.id == id_busca:
            print("Produto encontrado:")
            print(produto.mostrar_info())
            return produto

    print("Produto nao encontrado")
    return None

# Funcao para ver localizacao
def ver_localizacao():
    print("\n--- Ver Localizacao ---")

    id_busca = input("Digite o ID do produto: ")

    for produto in lista_produtos:
        if produto.id == id_busca:
            print(f"Localizacao: {produto.localizacao}")
            return produto.localizacao

    print("Produto nao encontrado")
    return None

# Funcao para atualizar estoque
def atualizar_estoque():
    print("\n--- Atualizar Estoque ---")

    id_produto = input("Digite o ID do produto: ")
    tipo_movimento = input("Digite o tipo (entrada/saida): ")
    quantidade_movimento = int(input("Digite a quantidade: "))

    for produto in lista_produtos:
        if produto.id == id_produto:
            if tipo_movimento == "entrada":
                produto.quantidade += quantidade_movimento
                print(f"Entrada registrada. Nova quantidade: {produto.quantidade}")
            elif tipo_movimento == "saida":
                if produto.quantidade >= quantidade_movimento:
                    produto.quantidade -= quantidade_movimento
                    print(f"Saida registrada. Nova quantidade: {produto.quantidade}")
                else:
                    print("Erro: Quantidade insuficiente")
                    return
            else:
                print("Erro: Tipo invalido")
                return

            # Registrar movimentacao
            mov = Movimentacao(id_produto, tipo_movimento, quantidade_movimento, "2024-07-24")
            lista_movimentacoes.append(mov)
            return

    print("Produto nao encontrado")

# Funcao para relatorio de estoque baixo
def relatorio_estoque_baixo():
    print("\n--- Relatorio Estoque Baixo ---")

    limite = 10
    produtos_com_pouco_estoque = []

    for produto in lista_produtos:
        if produto.quantidade < limite:
            produtos_com_pouco_estoque.append(produto)

    if produtos_com_pouco_estoque:
        print(f"Produtos com menos de {limite} unidades:")
        for prod in produtos_com_pouco_estoque:
            print(f"- {prod.nome}: {prod.quantidade} unidades")
    else:
        print("Nenhum produto com estoque baixo")

    return produtos_com_pouco_estoque

# Funcao para ver historico
def ver_historico():
    print("\n--- Historico de Movimentacoes ---")

    if lista_movimentacoes:
        for mov in lista_movimentacoes:
            print(mov.mostrar_info())
    else:
        print("Nenhuma movimentacao registrada")

# Funcao para listar todos produtos
def listar_todos_produtos():
    print("\n--- Todos os Produtos ---")

    if lista_produtos:
        for produto in lista_produtos:
            print(produto.mostrar_info())
    else:
        print("Nenhum produto cadastrado")

# Funcao para mostrar tabela verdade
def mostrar_tabela_verdade():
    print("\n--- Tabela Verdade do Sistema ---")

    print("Variaveis:")
    print("P = Cadastro de Produtos")
    print("E = Atualizacao de Estoque")
    print("L = Localizacao")
    print("R = Relatorios")

    print("\nTabela:")
    print("P | E | L | R | Sistema Completo")
    print("--------------------------------")

    # Todas as combinacoes possiveis
    combinacoes = [
        ['F', 'F', 'F', 'F', 'F'],
        ['F', 'F', 'F', 'T', 'F'],
        ['F', 'F', 'T', 'F', 'F'],
        ['F', 'F', 'T', 'T', 'F'],
        ['F', 'T', 'F', 'F', 'F'],
        ['F', 'T', 'F', 'T', 'F'],
        ['F', 'T', 'T', 'F', 'F'],
        ['F', 'T', 'T', 'T', 'F'],
        ['T', 'F', 'F', 'F', 'F'],
        ['T', 'F', 'F', 'T', 'F'],
        ['T', 'F', 'T', 'F', 'F'],
        ['T', 'F', 'T', 'T', 'F'],
        ['T', 'T', 'F', 'F', 'F'],
        ['T', 'T', 'F', 'T', 'F'],
        ['T', 'T', 'T', 'F', 'F'],
        ['T', 'T', 'T', 'T', 'T']
    ]

    for linha in combinacoes:
        print(f"{linha[0]} | {linha[1]} | {linha[2]} | {linha[3]} | {linha[4]}")

# Menu principal
def menu():
    while True:
        print("\n=================================")
        print("    SISTEMA DE ESTOQUE")
        print("=================================")
        print("1. Cadastrar Produto")
        print("2. Buscar Produto")
        print("3. Ver Localizacao")
        print("4. Atualizar Estoque")
        print("5. Relatorio Estoque Baixo")
        print("6. Ver Historico")
        print("7. Listar Todos Produtos")
        print("8. Tabela Verdade")
        print("0. Sair")
        print("=================================")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            buscar_produto()
        elif opcao == "3":
            ver_localizacao()
        elif opcao == "4":
            atualizar_estoque()
        elif opcao == "5":
            relatorio_estoque_baixo()
        elif opcao == "6":
            ver_historico()
        elif opcao == "7":
            listar_todos_produtos()
        elif opcao == "8":
            mostrar_tabela_verdade()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida")

# Inicio do programa
if __name__ == "__main__":
    # Adicionar alguns produtos para teste
    produto1 = Produto("001", "Notebook Dell", "Eletronicos", 15, 2500.00, "Prateleira A1")
    produto2 = Produto("002", "Mouse", "Perifericos", 8, 150.00, "Prateleira B2")
    produto3 = Produto("003", "Teclado", "Perifericos", 5, 300.00, "Prateleira B3")

    lista_produtos.append(produto1)
    lista_produtos.append(produto2)
    lista_produtos.append(produto3)

    print("Sistema iniciado com 3 produtos de exemplo")
    menu()