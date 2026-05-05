# roadmap-git
# 📘 Sistema de Cadastro de Usuários (CLI)

## 📝 Descrição

Este projeto consiste em um sistema simples de cadastro de usuários via terminal (CLI), desenvolvido em Python.

O objetivo principal não foi apenas a implementação do sistema, mas sim a prática de boas práticas de versionamento com Git, incluindo:

* Criação de branches
* Commits organizados (Conventional Commits)
* Abertura de Pull Requests
* Code Review entre os membros
* Resolução de conflitos

O sistema permite cadastrar, listar e buscar usuários, utilizando persistência em arquivo JSON.

---

## ⚙️ Tecnologias e Ferramentas Utilizadas

* Python
* JSON (armazenamento de dados)
* Git
* GitHub

---

## 💻 Como Rodar o Projeto

bash
# Clone o repositório
git clone https://github.com/pedroaugmb/roadmap-git.git

# Acesse a pasta
cd roadmap-git

# Execute o projeto
python main.py


---

## 🚀 Funcionalidades

* ✅ Criar usuário (nome e e-mail)
* 📋 Listar usuários cadastrados
* 🔍 Buscar usuário por e-mail
* 💾 Persistência de dados em arquivo JSON

---

## 🧱 Estrutura do Projeto

text
main.py        # Interface CLI
service.py     # Regras de negócio
storage.py     # Leitura e escrita em JSON
user.py        # Modelo de usuário (estrutura de dados)
data.json      # Base de dados


---

## 👥 Colaboradores

| Nome          | GitHub                                                         |
| ------------- | -------------------------------------------------------------- |
| Pedro Augusto | [https://github.com/pedroaugmb](https://github.com/pedroaugmb) |
| Jhonatan      | [https://github.com/JhonatanMotaDev](https://github.com/JhonatanMotaDev)                                                      |
| Caio          | [https://github.com/caiomendes2304)](https://github.com/caiomendes2304)                                                      |

---

## 🔁 Fluxo de Desenvolvimento (Git)

Durante o desenvolvimento foram utilizadas boas práticas de versionamento:

* Cada integrante trabalhou em sua própria branch
* Foram criados Pull Requests para integração do código
* Os membros realizaram revisões (code review) entre si
* Houve resolução de conflitos durante o merge das branches

Esse processo permitiu simular um ambiente real de desenvolvimento em equipe.

---

## ⚠️ Desafios Encontrados

Durante o desenvolvimento, ocorreram conflitos de merge devido a alterações simultâneas nas mesmas partes do código, incluindo modificações diretas na branch principal (main).

A equipe resolveu os conflitos realizando:

* Atualização das branches com a main
* Merge local das alterações
* Correção manual dos conflitos

Esse processo contribuiu para o aprendizado prático do funcionamento do Git em cenários reais.
---

## 📄 Licença

Este projeto está licenciado sob a MIT License.