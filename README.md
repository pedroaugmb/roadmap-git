# Sistema de Cadastro de Usuários

Projeto final em trio — sistema CLI de cadastro de usuários desenvolvido em Python com persistência em JSON.

## Funcionalidades

- Criar usuário (nome e e-mail)
- Listar todos os usuários cadastrados
- Buscar usuário por e-mail
- Dados persistidos localmente em `data.json`

## Estrutura do Projeto

```
roadmap-git/
├── main.py       # Interface CLI (menu e inputs)
├── service.py    # Regras de negócio
├── storage.py    # Leitura e escrita em JSON
└── data.json     # Gerado automaticamente ao cadastrar o 1º usuário
```

## Como Rodar

**Pré-requisito:** Python 3 instalado.

```bash
python main.py
```

## Tecnologias

- Python 3
- JSON (persistência de dados)

## Integrantes

| Nome | GitHub |
|------|--------|
| Jhonatan Pereira Mota | [@jhonatanmotadev](https://github.com/jhonatanmotadev) |
| Caio Henrique Mendes Soares | [@caiomendes2304](https://github.com/caiomendes2304) |
| Pedro Augusto Mendes Barbosa | [@pedroaugmb](https://github.com/pedroaugmb) |
