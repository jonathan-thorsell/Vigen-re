alfabetet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

text = input("Enter text to encrypt: ").upper()
key = input("Enter key: ").upper()

def encrypt(text, key):
    #vigeneres chiffere
    encrypted_text = ""
    key_index = 1
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

encrypted = encrypt(text, key)
print("Encrypted text:", encrypted)