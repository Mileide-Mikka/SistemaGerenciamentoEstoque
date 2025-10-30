# Sistema de Gerenciamento de Estoque

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Concluído-green.svg)
![License](https://img.shields.io/badge/License-Acadêmica-lightgray.svg)

</div>

## 📋 Descrição do Projeto

Sistema de gerenciamento de estoque desenvolvido em Python como projeto acadêmico para a Faculdade Anhanguera no curso de Análise e Desenvolvimento de Sistemas (ADS).

## ✨ Funcionalidades

<details>
<summary><b>Clique para ver todas as funcionalidades</b></summary>

- **Cadastro de Produtos**: Registro completo de produtos com ID, nome, categoria, quantidade, preço e localização
- **Busca e Consulta**: Localização rápida de produtos por ID
- **Controle de Estoque**: Entradas e saídas com atualização automática
- **Relatórios**: 
  - Estoque baixo (abaixo de 10 unidades)
  - Histórico completo de movimentações
  - Listagem geral de produtos
- **Localização**: Controle de posicionamento dos produtos no estoque
- **Tabela Verdade**: Demonstração lógica do sistema funcionando

</details>

## 🚀 Começando

### Pré-requisitos

- Python 3.6 ou superior

### Instalação e Execução

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-estoque.git

# Acesse o diretório
cd sistema-estoque

# Execute o programa
python sistema_estoque.py
```

## 🏗️ Estrutura do Projeto

```
sistema-estoque/
│
├── sistema_estoque.py    # Arquivo principal do sistema
├── README.md             # Este arquivo
└── requirements.txt      # Dependências do projeto
```

### 📁 Classes Principais

```python
class Produto:
    def __init__(self, id, nome, categoria, quantidade, preco, localizacao):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao
```

### 🎯 Menu Principal

| Opção | Funcionalidade |
|-------|----------------|
| 1 | Cadastrar Produto |
| 2 | Buscar Produto |
| 3 | Ver Localização |
| 4 | Atualizar Estoque |
| 5 | Relatório Estoque Baixo |
| 6 | Ver Histórico |
| 7 | Listar Todos Produtos |
| 8 | Tabela Verdade |
| 0 | Sair |

## 💻 Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Paradigma**: Programação Orientada a Objetos
- **Estruturas de Dados**: Listas e Classes
- **Persistência**: Em memória (listas)

## 👨‍💻 Desenvolvido por

**Mileide Silva de Arruda** - Estudante de Análise e Desenvolvimento de Sistemas  
Faculdade Anhanguera

## 🔧 Características Técnicas

<details>
<summary><b>Detalhes técnicos</b></summary>

- Interface via terminal
- Dados armazenados em memória (volátil)
- Validações básicas de entrada
- Sistema modular e expansível
- Inclui 3 produtos de exemplo para testes

</details>

## 📈 Exemplos de Uso

O sistema inclui produtos de exemplo para demonstração:

| ID | Nome | Categoria | Quantidade | Preço | Localização |
|----|------|-----------|------------|-------|-------------|
| 001 | Notebook Dell | Eletrônicos | 15 | R$ 2500.00 | Prateleira A1 |
| 002 | Mouse | Periféricos | 8 | R$ 150.00 | Prateleira B2 |
| 003 | Teclado | Periféricos | 5 | R$ 300.00 | Prateleira B3 |

## 🔮 Melhorias Futuras

- [ ] Persistência em banco de dados
- [ ] Interface gráfica (Tkinter, PyQt)
- [ ] Relatórios em PDF/Excel
- [ ] Sistema de usuários e permissões
- [ ] Controle por lote e validade
- [ ] Integração com leitor de código de barras

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.

---

<div align="center">

**Projeto acadêmico** - Faculdade Anhanguera - Curso ADS

</div>
