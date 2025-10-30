def cifrar_simple(texto, clave):
    bits_resultado = []
    for i in range(len(texto)):
        xor_result = ord(texto[i]) ^ ord(clave[i % len(clave)])
        for j in range(7, -1, -1):
            bit = (xor_result >> j) & 1
            bits_resultado.append(bit)
    return bits_resultado
def descifrar_simple(bits_cifrados, clave):
    texto = ""
    for i in range(0, len(bits_cifrados), 8):
        if i + 8 <= len(bits_cifrados):
            num = 0
            for j in range(8):
                num = (num << 1) | bits_cifrados[i + j]
            texto += chr(num ^ ord(clave[(i//8) % len(clave)]))
    return texto
mensaje = "Hola"
clave = "abc"
print("Mensaje:", mensaje)
print("Clave:", clave)
cifrado = cifrar_simple(mensaje, clave)
print("Cifrado:", cifrado)
descifrado = descifrar_simple(cifrado, clave)
print("Descifrado:", descifrado)
