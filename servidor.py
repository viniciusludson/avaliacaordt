
import socket
from rdt_utils import desempacotar, calcular_checksum, criar_pacote, rede_com_erros

ENDERECO = ('127.0.0.1', 12000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ENDERECO)

print("Servidor RDT 3.0 aguardando conexões...")
estado_esperado_seq = 0

while True:
    try:
        pacote_bruto, endereco_cliente = sock.recvfrom(1024)
        # Aplica o simulador de erros da rede no recebimento
        pacote_bruto = rede_com_erros(pacote_bruto, taxa_erro=0.2)

        if not pacote_bruto:
            continue  # Pacote perdido, espera o timeout do cliente

        seq_num, chk_recebido, dados = desempacotar(pacote_bruto)
        chk_calculado = calcular_checksum(seq_num, dados)

        # Verificação 1: O pacote está corrompido?
        if chk_recebido != chk_calculado:
            print(f"[REDE/SERV] Dados corrompidos detectados! Enviando ACK do estado oposto.")
            ack_inverso = 1 if estado_esperado_seq == 0 else 0
            pacote_ack = criar_pacote(ack_inverso, b"ACK")
            sock.sendto(pacote_ack, endereco_cliente)
            continue


        # Verificação 2: É o número de sequência esperado?
        if seq_num == estado_esperado_seq:
            print(f"[SERV] Pacote {seq_num} recebido com sucesso: '{dados.decode()}'")
            pacote_ack = criar_pacote(seq_num, b"ACK")

            # Simula que o ACK também pode se perder ou corromper na volta
            pacote_ack_simulado = rede_com_erros(pacote_ack, taxa_erro=0.2)
            if pacote_ack_simulado:
                sock.sendto(pacote_ack_simulado, endereco_cliente)

            # Alterna o estado esperado (0 -> 1 ou 1 -> 0)
            estado_esperado_seq = 1 - estado_esperado_seq
        else:
            print(
                f"[SERV] Pacote duplicado detectado (esperava {estado_esperado_seq}, veio {seq_num}). Reenviando ACK.")
            pacote_ack = criar_pacote(seq_num, b"ACK")
            sock.sendto(pacote_ack, endereco_cliente)

    except Exception as e:
        print(f"Erro ao processar pacote: {e}")