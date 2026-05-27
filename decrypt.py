alfabetet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"]

text = input("Text att avkryptera: ").upper()
key = input("Nyckel: ").upper()

def decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0
    for char in encrypted_text:
        if char in alfabetet:
            char_index = alfabetet.index(char)
            key_char = key[key_index % len(key)]
            key_index += 1
            key_char_index = alfabetet.index(key_char)
            
            # P_i = (C_i - K_i) mod 29
            decrypted_char_index = (char_index - key_char_index) % len(alfabetet)
            decrypted_text += alfabetet[decrypted_char_index]
        else:
            decrypted_text += char
    return decrypted_text

decrypted = decrypt(text, key)
print("Avkrypterad text:", decrypted)