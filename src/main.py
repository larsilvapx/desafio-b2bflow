import logging

from supabase_client import SupabaseClient
from zapi_client import ZApiClient
from message_service import build_message


client = SupabaseClient()
contacts = client.get_contacts()
print(contacts)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    logging.info("Iniciando processo.")

    supabase_client = SupabaseClient()
    zapi_client = ZApiClient()

    try:

        contacts = supabase_client.get_contacts()

        if not contacts:
            logging.warning(
                "Nenhum contato encontrado."
            )
            return

        for contact in contacts:

            name = contact.get("nome")
            phone = contact.get("telefone")

            if not phone:

                logging.warning(
                    f"Contato {name} sem telefone."
                )

                continue

            message = build_message(name)

            try:

                response = (
                    zapi_client.send_message(
                        phone,
                        message
                    )
                )

                if response.status_code in [200, 201]:

                    logging.info(
                        f"Mensagem enviada para "
                        f"{name}"
                    )

                else:

                    logging.error(
                        f"Erro ao enviar para "
                        f"{name}: {response.text}"
                    )

            except Exception as error:

                logging.error(
                    f"Falha ao enviar para "
                    f"{name}: {error}"
                )

    except Exception as error:

        logging.error(
            f"Erro geral: {error}"
        )


if __name__ == "__main__":
    main()