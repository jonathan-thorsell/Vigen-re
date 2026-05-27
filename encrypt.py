alfabetet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"]

text = input("Text att krypteras: ").upper()
key = input("Nyckel: ").upper()

def vigenere(text, key):
    encrypted_text = ""
    key_index = 0
    for char in text:
        if char in alfabetet:
            text_index = alfabetet.index(char)
            key_char = key[key_index % len(key)]
            key_index += 1
            key_char_index = alfabetet.index(key_char)
            encrypted_char_index = (text_index + key_char_index) % len(alfabetet)
            encrypted_text += alfabetet[encrypted_char_index]
        else:
            encrypted_text += char
    return encrypted_text

encrypted = vigenere(text, key)
print("Krypterad text:", encrypted)