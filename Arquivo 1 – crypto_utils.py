# crypto_utils.py
import base64


def encode_message(key: str, message: str) -> str:
    """
    Codifica uma mensagem usando uma chave e o algoritmo de substituição simples com base64.

    Parâmetros:
        key (str): Chave de criptografia.
        message (str): Mensagem de entrada a ser codificada.

    Retorna:
        str: Mensagem codificada em base64.

    Levanta:
        ValueError: Se a chave ou mensagem estiver vazia.
    """
    if not key or not message:
        raise ValueError("A chave e a mensagem não podem estar vazias.")

    encoded_chars = []
    try:
        for i, char in enumerate(message):
            key_c = key[i % len(key)]
            encoded_chars.append(chr((ord(char) + ord(key_c)) % 256))
        encoded_message = "".join(encoded_chars)
        return base64.urlsafe_b64encode(encoded_message.encode()).decode()
    except Exception as e:
        raise RuntimeError(f"Erro ao codificar a mensagem: {e}")


def decode_message(key: str, encoded_message: str) -> str:
    """
    Decodifica uma mensagem criptografada com base64 e chave de substituição simples.

    Parâmetros:
        key (str): Chave de descriptografia.
        encoded_message (str): Mensagem codificada em base64.

    Retorna:
        str: Mensagem original decodificada.

    Levanta:
        ValueError: Se a chave ou mensagem estiver vazia.
    """
    if not key or not encoded_message:
        raise ValueError("A chave e a mensagem não podem estar vazias.")

    try:
        decoded_base64 = base64.urlsafe_b64decode(encoded_message).decode()
        decoded_chars = []
        for i, char in enumerate(decoded_base64):
            key_c = key[i % len(key)]
            decoded_chars.append(chr((256 + ord(char) - ord(key_c)) % 256))
        return "".join(decoded_chars)
    except Exception as e:
        raise RuntimeError(f"Erro ao decodificar a mensagem: {e}")
