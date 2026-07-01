import hashlib
import random

def calcular_checksum(seq_num: int, dados: bytes) -> str:
    """Gera um checksum simples baseado no MD5 para detectar corrupção."""
    md5 = hashlib.md5()
    md5.update(str(seq_num).encode() + dados)
    return md5.hexdigest()

def criar_pacote(seq_num: int, dados: bytes) -> bytes:
    """Formata o pacote: seq_num | checksum | dados"""
    chk = calcular_checksum(seq_num, dados)
    return f"{seq_num}|{chk}|".encode() + dados

def desempacotar(pacote: bytes):
    """Separa os componentes do pacote recebido."""
    partes = pacote.split(b'|', 2) # Corrigido o caractere de split do PDF
    seq_num = int(partes[0].decode())
    chk_recebido = partes[1].decode()
    dados = partes[2]
    return seq_num, chk_recebido, dados

def rede_com_erros(pacote: bytes, taxa_erro=0.3) -> bytes:
    """Simula a perda ou corrupção de pacotes na rede."""
    rand = random.random()
    if rand < taxa_erro / 2:
        # Simula PERDA de pacote
        print("[REDE] X Pacote foi perdido no canal!")
        return None
    elif rand < taxa_erro:
        # Simula CORRUPÇÃO de dados (altera o último byte)
        print("[REDE] ! Pacote foi corrompido na transmissão!")
        if len(pacote) > 0:
            pacote = pacote[:-1] + b'\x00'
        return pacote
    return pacote