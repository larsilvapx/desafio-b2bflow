# Desafio Técnico - b2bflow Automação

Este repositório contém a solução para o desafio técnico da **b2bflow**. A aplicação consiste em um pipeline automatizado em Python que consome dados de contatos a partir de uma base do **Supabase**, processa as informações respeitando as regras de negócio e realiza o disparo de mensagens customizadas via WhatsApp utilizando a **Z-API**.

##  Tecnologias Utilizadas

- **Python 3.11**
- **Supabase** (Backend as a Service / Banco de Dados)
- **Z-API** (Integração com a API do WhatsApp)
- **Pytest** (Framework de Testes Automatizados)
- **Requests** (Manipulação de chamadas HTTP)
- **Python-dotenv** (Gerenciamento de variáveis de ambiente)

##  Estrutura do Projeto

```text
desafio-b2bflow/
│
├── src/
│   ├── __init__.py
│   ├── config.py           # Validação e carga de variáveis de ambiente
│   ├── main.py             # Orquestração e ponto de entrada da aplicação
│   ├── message_service.py  # Regra de negócio e construção da mensagem
│   ├── supabase_client.py  # Integração com a API/Banco do Supabase
│   └── zapi_client.py      # Integração com os endpoints da Z-API
│
├── tests/
│   ├── __init__.py
│   └── test_message.py     # Testes unitários e mocks de chamadas de API
│
├── .env.example            # Modelo para configuração das credenciais
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação principal

 Configuração do Ambiente e Instalação
Siga os passos abaixo para configurar e executar o projeto localmente:

1. Clonar o Repositório
Bash
git clone [https://github.com/larsilvapx/desafio-b2bflow.git](https://github.com/larsilvapx/desafio-b2bflow.git)
cd desafio-b2bflow
2. Criar e Ativar o Ambiente Virtual (venv)
No Windows:

DOS
python -m venv venv
venv\Scripts\activate
3. Instalar as Dependências
Com a venv ativa, instale os pacotes necessários:

DOS
pip install -r requirements.txt
4. Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto com base no arquivo .env.example e preencha com as suas credenciais:

Ini, TOML
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_anon_ou_service_role
ZAPI_INSTANCE_ID=seu_id_de_instancia_zapi
ZAPI_TOKEN=seu_token_zapi

 Executando a Aplicação
Para iniciar o fluxo de automação (que busca os contatos pendentes e realiza os disparos limitados a até 3 registros conforme os requisitos), execute:

DOS
python src/main.py

 Executando os Testes Automatizados
Os testes unitários foram desenvolvidos utilizando Mocks para simular as respostas das APIs externas (Z-API e Supabase), garantindo que os testes sejam rápidos, isolados e não gerem custos ou efeitos colaterais de rede.

Para rodar os testes garantindo o escopo correto dos pacotes, execute o comando abaixo na raiz do projeto:

No Prompt de Comando (CMD) do Windows:

DOS
set PYTHONPATH=.&& pytest tests/test_message.py
No PowerShell:

PowerShell
$env:PYTHONPATH="."; pytest tests/test_message.py


Desenvolvido por Luciano Arruda.