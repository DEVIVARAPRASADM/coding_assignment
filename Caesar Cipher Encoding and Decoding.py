def caesar_cipher(message, shift, encode=True):
    if not encode:
        shift = -shift

    result = []
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)
    return ''.join(result)

original = "Hello, World!"
shift = 3
encoded = caesar_cipher(original, shift, encode=True)
decoded = caesar_cipher(encoded, shift, encode=False)

print("Original:", original)
print("Encoded :", encoded)
print("Decoded :", decoded)
