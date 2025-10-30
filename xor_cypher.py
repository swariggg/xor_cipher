def cifrar_simple(texto):
    bits_resultado = []
    for letra in texto:
        ascii_val = ord(letra)
        for j in range(7, -1, -1):
            bit = (ascii_val >> j) & 1
            bits_resultado.append(bit)
    return bits_resultado
def descifrar_simple(bits_cifrados):
    texto = ""
    for i in range(0, len(bits_cifrados), 8):
        if i + 8 <= len(bits_cifrados):
            num = 0
            for j in range(8):
                num = (num << 1) | bits_cifrados[i + j]
            texto += chr(num)
    return texto
mensaje = "Hola"
print("Mensaje:", mensaje)
cifrado = cifrar_simple(mensaje)
print("Cifrado:", cifrado)
descifrado = descifrar_simple(cifrado)
print("Descifrado:", descifrado)
