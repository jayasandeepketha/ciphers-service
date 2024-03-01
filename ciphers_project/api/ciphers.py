def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if c.isalpha():
            ascii_offset = ord('a') if c.islower() else ord('A')
            c_encoded = (ord(c) - ascii_offset + shift) % 26 + ascii_offset
        else:
            c_encoded = ord(c) + shift
        c_encoded = chr(c_encoded)
        cipher_text += c_encoded
    return cipher_text
