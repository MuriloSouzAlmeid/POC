# POC - Desafio DevCertacon

O projeto POC é uma prova de conceito que integra automação web com Selenium e uma API construída em FastAPI, com persistência de dados em Microsoft SQL Server usando o SQLModel e exportação de dados para um arquivo de planilhas Excel usando Openpyxl.

A API simula o processo de login de um usuário através do site `https://practicetestautomation.com/practice-test-login/` e realiza a extração de dados da tabela NCM presente em `https://www.contabilizei.com.br/contabilidade-online/ncm/` por meio de um WebDriver Selenium. Os dados coletados são gerenciados por uma API RESTful que oferece rotas documentadas via Swagger (OpenAPI) para:

* Realizar login simulado via Selenium com autenticação via JWT Bearer token; 

* Buscar dados NCM do site;

* Persistir os dados em banco de dados;

* Realizar operações de CRUD (criação, leitura e remoção) dos dados NCM;

* Exportar os dados do banco para uma planilha Excel utilizando openpyxl.
## Setup do Proeto

### Requisitos

* Python 3.10+

* Microsoft SQL Server ativo e configurado

* Chrome + ChromeDriver compatível instalado

* **(Opcional)** Ambiente virtual Python (recomendado)

### Instalação

Siga as seguintes etapas para a intalação e configuração do projeto:


**1. Clone o repositório:**

```bash
git clone https://github.com/MuriloSouzAlmeid/POC.git
```

**2. Crie e ative um ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente (exemplo com .env):**

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`POC_SECRET_KEY_TOKEN`

`POC_SELENIUM_HEADLESS` ("S" ou "N")

`POC_ALGORITHM_JWT_TOKEN`

`POC_EXPIRATION_TOKEN_TIME` (em minutos)

`POC_STRINGCONNECTION_DATABASE`

**5. Execute a aplicação:**

```bash
uvicorn app.main:app --reload

# ou também com

cd/app
fastapi dev main.py
```

    
## Usando a OpenAPI (Swagger.UI)

Um breve tutorial com exemplos de uso das rotas da API criada por meio do Swagger do FastAPI:

### Acessando a Documentação

### Realizando o Login na Aplicação

### Autenticação via JWT Bearer token

### Iniciando Automoção de Extração de NCM

### Listando NCMs Persistidos no Banco

### Selecionando NCM Desejado pelo ID

### Deletando NCM Selecionado pelo ID

### Exportanto Dados Persistidos no Banco para uma Planilha Excel