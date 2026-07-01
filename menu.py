
import sys
import os
import time
import subprocess


def exibir_menu():
    print("=" * 55)
    print("        SIMULADOR DE CENÁRIOS - APENAS RDT 3.0        ")
    print("=" * 55)
    print("Escolha qual falha do canal você deseja testar no RDT 3.0:")
    print("-" * 55)
    print("1) Cenário Ideal (Sem erros - Transmissão limpa)")
    print("2) Corrupção de Dados (Cliente -> Servidor)")
    print("3) Perda Total de Pacote (Gera Timeout no Cliente)")
    print("4) Falha no ACK de Retorno (ACK perdido ou corrompido)")
    print("5) Modo Caos (Erros simultâneos em todas as etapas)")
    print("0) Sair")
    print("-" * 55)


def configurar_cenario(opcao):
    # Dicionário de parâmetros de erro dinâmicos
    # (taxa_cli_ida, taxa_serv_recebe, taxa_serv_ack_volta, timeout)
    cenarios = {
        '1': (0.0, 0.0, 0.0, 2.0),  # Ideal
        '2': (0.5, 0.0, 0.0, 2.0),  # Corrupção na ida (RDT 3.0 trata com timeout/duplicados)
        '3': (0.6, 0.0, 0.0, 1.5),  # Perda na ida (Gera timeout)
        '4': (0.0, 0.0, 0.6, 1.5),  # Erro no ACK (Gera retransmissão e duplicata no servidor)
        '5': (0.4, 0.2, 0.3, 2.0)  # Caos (Combinação de todos)
    }

    if opcao in cenarios:
        return cenarios[opcao]
    print("Opção inválida.")
    return None


def rodar_simulacao(config):
    taxa_cli, taxa_serv_rx, taxa_serv_ack, timeout = config

    # Código do Servidor RDT 3.0 adaptado do seu arquivo original
    codigo_servidor = f"""
import socket
from rdt_utils import desempacotar, calcular_checksum, criar_pacote, rede_com_erros

ENDERECO = ('127.0.0.1', 12000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ENDERECO)

estado_esperado_seq = 0
print("[SERV] Servidor RDT 3.0 aguardando pacotes...")

mensagens_recebidas = 0
while mensagens_recebidas < 4:
    try:
        pacote_bruto, endereco_cliente = sock.recvfrom(1024)

        # Aplica taxa de erro customizada no recebimento do servidor
        pacote_bruto = rede_com_erros(pacote_bruto, taxa_erro={taxa_serv_rx})
        if not pacote_bruto:
            continue

        seq_num, chk_recebido, dados = desempacotar(pacote_bruto)
        chk_calculado = calcular_checksum(seq_num, dados)

        if chk_recebido != chk_calculado:
            print(f"[REDE/SERV] Dados corrompidos detectados! Enviando ACK do estado oposto.")
            ack_inverso = 1 if estado_esperado_seq == 0 else 0
            pacote_ack = criar_pacote(ack_inverso, b"ACK")
            sock.sendto(pacote_ack, endereco_cliente)
            continue

        if seq_num == estado_esperado_seq:
            print(f"[SERV] Pacote {{seq_num}} recebido com sucesso: '{{dados.decode()}}'")
            pacote_ack = criar_pacote(seq_num, b"ACK")

            # Aplica taxa de erro customizada no envio do ACK de volta
            pacote_ack_simulado = rede_com_erros(pacote_ack, taxa_erro={taxa_serv_ack})
            if pacote_ack_simulado:
                sock.sendto(pacote_ack_simulado, endereco_cliente)

            estado_esperado_seq = 1 - estado_esperado_seq
            mensagens_recebidas += 1
        else:
            print(f"[SERV] Pacote duplicado detectado (esperava {{estado_esperado_seq}}, veio {{seq_num}}). Reenviando ACK.")
            pacote_ack = criar_pacote(seq_num, b"ACK")
            sock.sendto(pacote_ack, endereco_cliente)

    except Exception:
        break
"""

    # Código do Cliente RDT 3.0 adaptado do seu arquivo original
    codigo_cliente = f"""
import socket
from rdt_utils import criar_pacote, desempacotar, calcular_checksum, rede_com_erros

ENDERECO_SERVIDOR = ('127.0.0.1', 12000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout({timeout})

mensagens = ["Mensagem A", "Mensagem B", "Mensagem C", "Mensagem D"]
seq_atual = 0

for msg in mensagens:
    dados = msg.encode()
    pacote = criar_pacote(seq_atual, dados)
    sucesso = False

    while not sucesso:
        print(f"\\n[CLI] Enviando '{{msg}}' com Seq {{seq_atual}}...")

        # Aplica taxa de erro customizada no envio do cliente
        pacote_enviado = rede_com_erros(pacote, taxa_erro={taxa_cli})
        if pacote_enviado:
            sock.sendto(pacote_enviado, ENDERECO_SERVIDOR)
        else:
            print("[CLI] (Simulação: O pacote foi perdido no canal antes de sair)")

        try:
            ack_bruto, _ = sock.recvfrom(1024)
            ack_seq, ack_chk, ack_dados = desempacotar(ack_bruto)
            chk_calculado = calcular_checksum(ack_seq, ack_dados)

            if ack_chk != chk_calculado:
                print("[CLI] ! ACK recebido está corrompido! Ignorando e esperando Timeout...")
                continue

            if ack_seq != seq_atual:
                print(f"[CLI] -> Recebeu ACK {{ack_seq}}, mas esperava ACK {{seq_atual}}. Ignorando...")
                continue

            print(f"[CLI] OK! ACK {{ack_seq}} recebido com sucesso.")
            sucesso = True

        except socket.timeout:
            print(f"[CLI] !!! TIMEOUT !!! Nenhuma resposta válida para Seq {{seq_atual}}. Reenviando...")

    seq_atual = 1 - seq_atual

print("\\n[CLI] Envio finalizado para este cenário!")
"""

    # Criação dos ambientes temporários para execução em paralelo
    with open("temp_servidor.py", "w", encoding="utf-8") as f:
        f.write(codigo_servidor)
    with open("temp_cliente.py", "w", encoding="utf-8") as f:
        f.write(codigo_cliente)

    proc_servidor = subprocess.Popen([sys.executable, "temp_servidor.py"])
    time.sleep(0.5)  # Janela para o Servidor abrir o socket UDP

    subprocess.run([sys.executable, "temp_cliente.py"])

    # Finalização segura dos subprocessos
    proc_servidor.terminate()
    time.sleep(0.3)

    if os.path.exists("temp_servidor.py"): os.remove("temp_servidor.py")
    if os.path.exists("temp_cliente.py"): os.remove("temp_cliente.py")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha o cenário de teste: ").strip()

        if opcao == '0':
            print("Encerrando simulador RDT 3.0.")
            break

        config = configurar_cenario(opcao)
        if config:
            rodar_simulacao(config)
            input("\nPressione [ENTER] para continuar...")
        else:
            time.sleep(1)


if __name__ == "__main__":
    main()
