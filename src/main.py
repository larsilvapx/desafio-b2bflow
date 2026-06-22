import logging
import sys


from supabase_client import SupabaseClient
from zapi_client import ZApiClient
from message_service import build_message

# Configuração de Logs unificada e direcionada para a saída padrão (sys.stdout)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def main():
    logging.info("Iniciando o processo de automação b2bflow...")

    # Inicialização dos clientes centralizada no fluxo principal
    supabase_client = SupabaseClient()
    zapi_client = ZApiClient()

    try:
        logging.info("Buscando contatos na base de dados do Supabase...")
        all_contacts = supabase_client.get_contacts()

        if not all_contacts:
            logging.warning("Nenhum contato encontrado no banco de dados.")
            return

        # Garante a regra do desafio: processa no máximo 3 contatos
        contacts = all_contacts[:3]
        logging.info(f"Total de {len(contacts)} contatos selecionados para envio.")

        for contact in contacts:
            name = contact.get("nome")
            phone = contact.get("telefone")

            # Validação defensiva de dados
            if not phone:
                logging.warning(f" Contato '{name}' ignorado por falta de número de telefone.")
                continue

            if not name:
                logging.warning(f" Contato com o telefone {phone} não possui nome cadastrado. Pulando...")
                continue

            # Constrói a mensagem customizada ("Olá, <nome> tudo bem com você?")
            message = build_message(name)

            try:
                logging.info(f"Disparando mensagem via Z-API para {name}...")
                response = zapi_client.send_message(phone, message)

                # Verifica se o retorno da Z-API indica sucesso
                if response and response.status_code in [200, 201]:
                    logging.info(f" Mensagem enviada com sucesso para {name} ({phone}).")
                else:
                    status_code = response.status_code if response else "Sem resposta"
                    error_text = response.text if response else "Timeout/Erro de Conexão"
                    logging.error(f" Falha no envio para {name}. Status: {status_code} - Erro: {error_text}")

            except Exception as error:
                logging.error(f" Erro de comunicação com a Z-API ao processar {name}: {error}")
                continue # Garante que o loop não quebre se uma requisição falhar

    except Exception as error:
        logging.critical(f" Erro geral e inesperado na execução do fluxo: {error}")

if __name__ == "__main__":
    main()