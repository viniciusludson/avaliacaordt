#Grupo 06: Criptografia RSA
import random
def miller_rabin(n, k=40):#vai fazer 40 testes
    """Verifica se n é provavelmente primo se n  não for primo ele para."""
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False

    # Decompõe n-1 em 2^s * d
    s, d = 0, n - 1   #vai verificar se um número é provavelmente primo
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n) #vai fazer a potencia modular
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def mod_inverse(e, phi):
    #Calcula d tal que (e * d) % phi(n) seja congruente a 1.
    a, b, x0, x1 = e, phi, 1, 0
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
    return x0 % phi


def encriptar(message, e, n):
    # vamos dividir a mensagem em blocos para poder criptografa.
    # Tamanho do bloco em bytes tem que ser menor que n
    block_size = (n.bit_length() - 1) // 8 or 1
    data = message.encode()

    cipher_blocks = []
    for i in range(0, len(data), block_size):
        block = data[i:i + block_size]
        m = int.from_bytes(block, 'big')
        cipher_blocks.append(pow(m, e, n))
    return cipher_blocks


def decrypt(bloco_cifrado, d, n):
    #Descriptografa cada bloco e juntar cada string para trazer a mensagem novamente."""
    dados_decifrados = bytearray()
    for c in bloco_cifrado:
        m = pow(c, d, n)
        # Converte de volta para bytes
        byte_len = (m.bit_length() + 7) // 8
        dados_decifrados.extend(m.to_bytes(byte_len, 'big'))#o ..extend é unir os dados, em um unico vetor
    return dados_decifrados.decode()


# saidas
print("-"*30, "Criptografando com RSA ","-"*30)
p = int(input("Digite o primo p: "))
q = int(input("Digite o primo q: "))
n=p*q
print("O modulo de n é: ",n)
if miller_rabin(p) and miller_rabin(q): #verificar se os números são primos
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Expoente público
    d = mod_inverse(e, phi)
    print("O phi de n é:",phi)
    print("O expoente público (e) é:", e)
    print("O expoente privado (d) é:", d)
    msg = input("\nDigite a mensagem: ")

    criptografado = encriptar(msg, e, n)
    print(f"Criptografando mensagem em (blocos): {criptografado}")

    descriptografado = decrypt(criptografado, d, n)
    print(f"Descriptografando mensagem: {descriptografado}")
else:
    print("Erro: Os números digitados não passaram no teste de Miller-Rabin.")




