import random

# --- 1. FERRAMENTA: TESTE DE MILLER-RABIN ---
def eh_primo(n, k=40):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    # Decompõe n-1 para 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# --- 2. FERRAMENTA: MATEMÁTICA DO RSA ---
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


def inverso_modular(e, phi):
    # Acha o 'd' que "desfaz" a conta do 'e'
    a, b = e, phi
    x0, x1 = 1, 0
    while b:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
    return x0 % phi


# --- 3. EXECUÇÃO PRINCIPAL ---

# Entrada dos números primos
print("--- Gerador de Chaves RSA ---")
p = int(input("Digite um número primo (p): "))
q = int(input("Digite outro número primo (q): "))

if not (eh_primo(p) and eh_primo(q)):
    print("ERRO: Um dos números digitados não é primo pelo teste de Miller-Rabin!")
else:
    # Cálculo das chaves
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"O phi de n é:",{phi})
    # Escolha do 'e' (deve ser primo entre si com phi)
    e = 65537
    if mdc(e, phi) != 1:
        e = 3  # Alternativa simples se o padrão falhar

    d = inverso_modular(e, phi)

    print(f"\nChave Pública: (e={e}, n={n})")
    print(f"Chave Privada: (d={d}, n={n})")

    # Entrada da mensagem
    msg_texto =("Criptografia rsa para a segurança" )

    # Converte texto para NÚMERO (Baseado em bytes)
    msg_num = int.from_bytes(msg_texto.encode('utf-8'), 'big')

    if msg_num >= n:
        print("ERRO: Mensagem muito longa para esses primos. Use números maiores!")
    else:
        # CRIPTOGRAFAR
        cifrada = pow(msg_num, e, n)
        print(f"\nMensagem Cifrada (número): {cifrada}")

        # DESCRIPTOGRAFAR
        decifrada_num = pow(cifrada, d, n)

        # Converte NÚMERO de volta para texto
        tamanho_bytes = (decifrada_num.bit_length() + 7) // 8
        msg_final = decifrada_num.to_bytes(tamanho_bytes, 'big').decode('utf-8')

        print(f"Mensagem Decifrada (texto): {msg_final}")