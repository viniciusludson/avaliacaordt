import socket
from rdt_utils import criar_pacote, desempacotar, calcular_checksum, rede_com_erros

ENDERECO_SERVIDOR = ('127.0.0.1', 12000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2.0)  # Define o tempo limite para o Timeout (RDT 3.0)

mensagens = ["Olá servidor !", "Estabelecendo conexão! ", "Mensagem enviada! ", "Mensagens detectadas! "]
seq_atual = 0

for msg in mensagens:
    dados = msg.encode()
    pacote = criar_pacote(seq_atual, dados)
    sucesso = False

    while not sucesso:
        print(f"\n[CLI] Enviando '{msg}' com Seq {seq_atual}...")

        # Simula erro no envio do pacote do cliente para o servidor
        pacote_enviado = rede_com_erros(pacote, taxa_erro=0.4)
        if pacote_enviado:
            sock.sendto(pacote_enviado, ENDERECO_SERVIDOR)
        else:
            print("[CLI] (Simulação: O pacote nem saiu da placa de rede local)")

        try:
            # Espera pelo ACK do servidor
            ack_bruto, _ = sock.recvfrom(1024)
            ack_seq, ack_chk, ack_dados = desempacotar(ack_bruto)
            chk_calculado = calcular_checksum(ack_seq, ack_dados)

            # Tratamento de erro 1: ACK corrompido
            if ack_chk != chk_calculado:
                print("[CLI] ! ACK recebido está corrompido! Ignorando e tentando reenvio...")
                continue

            # Tratamento de erro 2: ACK com sequência errada
            if ack_seq != seq_atual:
                print(f"[CLI] -> Recebeu ACK {ack_seq}, mas esperava ACK {seq_atual}. Ignorando...")
                continue

            # Se passou nas checagens, sucesso!
            print(f"[CLI] OK! ACK {ack_seq} recebido com sucesso.")
            sucesso = True

        except socket.timeout:
            # Tratamento de erro 3: Timeout
            print(f"[CLI] !!! TIMEOUT !!! Nenhuma resposta do servidor para Seq {seq_atual}. Reenviando...")

    # Alterna o número de sequência para a próxima mensagem
    seq_atual = 1 - seq_atual

print("\n[CLI]  Mensagens enviadas com sucesso via RDT 3.0!")