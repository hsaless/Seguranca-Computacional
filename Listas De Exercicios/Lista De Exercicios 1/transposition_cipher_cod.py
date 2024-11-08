def transposition_cipher(text):
    key = "JIAZHENG"
    tam = len(key)
    text = text.replace(" ", "").upper()
    
    if len(text) % tam != 0:
        text += "X" * (tam - (len(text) % tam))
    
    
    num_rows = len(text) // tam
    matriz = [[None] * tam for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(tam):
            matriz[i][j] = text[i * tam + j]

    ordered_key = [2, 5, 7, 4, 1, 0, 6, 3]
    cipher_text = ""

    for col in ordered_key:
        for row in matriz:
            cipher_text += row[col]
    
    print(matriz)
    return cipher_text


message = input('Digite a mensagem a ser cifrada com a chave "Jiazheng": ')

print(transposition_cipher(message))