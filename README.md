# Site de cálculo nutricional e agendamento

## Contribuir com o codigo

Requisistos:

- Python 3.12 instalado
- Biblioteca venv
- Docker (opcional)

### Criando uma venv python

Entre na pasta do projeto no VSCode ou em sua IDE favorita e crie um ambiente virtual (venv) Python no terminal:

```bash
python -m venv .venv
```

Para entrar nela use esse comando:

```bash
.\.venv\Scripts\activate
```

Se estiver usando um linux use esse comando:

```bash
source ./.venv/bin/activate
```

Se aparecer um (.venv) no começo da linha, isso significa que você está no ambiente virtual do Python.

> ***NOTA:***
> Sempre ative o ambiente virtual (.venv) antes de trabalhar no projeto.

### Instalando dependencias

Com o venv ativado, instale as dependências usando o comando:

```bash
pip install -r requirements.txt
```

### Rodando o projeto

Após seguir os passos anteriores, para rodar o projeto, use o comando:

```bash
python manage.py runserver
```

Acesse a URL que aparecerá no terminal e pronto, o projeto estará rodando.