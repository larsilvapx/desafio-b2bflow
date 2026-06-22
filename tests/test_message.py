from src.message_service import (
    build_message
)


def test_build_message():

    expected = (
        "Olá, João tudo bem com você?"
    )

    result = build_message("João")

    assert result == expected