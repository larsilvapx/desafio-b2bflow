# Desafio Técnico - b2bflow Automação

Pipeline automatizado em Python que consome contatos do Supabase e realiza disparos de mensagens customizadas via WhatsApp utilizando a Z-API.

## 1. Setup de Tabelas (Supabase)

Para o funcionamento correto da aplicação, certifique-se de que a sua tabela no Supabase possui a seguinte estrutura base:

- **Tabela:** `contatos` (ou o nome configurado em seu cliente)
- **Campos obrigatórios:**
  - `nome` (text): Nome do contato.
  - `telefone` (text): Número do WhatsApp com código de área (ex: `5581999999999`).

## 2. Variáveis de Ambiente (.env)

Crie um arquivo chamado `.env` na raiz do projeto e preencha com as suas credenciais:

```ini
SUPABASE_URL=[https://seu-projeto.supabase.co](https://seu-projeto.supabase.co)
SUPABASE_KEY=sua-chave-api-supabase
ZAPI_INSTANCE_ID=seu-id-da-instancia-zapi
ZAPI_TOKEN=seu-token-da-zapi
3. Como Rodar
Executar a Automação
Para ativar o ambiente virtual, instalar as dependências e iniciar o fluxo de disparos (limitado a até 3 contatos), execute no terminal:

DOS
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
Executar os Testes Unitários
Para rodar a suíte de testes com mocks isolados de API, execute:

DOS
set PYTHONPATH=.&& pytest tests/test_message.py