def caesar_cipher():
    def encrypt(text, key):
        result = ""
        for char in text:
            if char.isalpha():
                shift = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - shift + key) % 26 + shift)
            else:
                result += char
        return result

    def decrypt(text, key):
        return encrypt(text, -key)

    while True:
        choice = input("Encrypt (e) or Decrypt (d)? ").lower()
        if choice in ['e', 'd']:
            break
        else:
            print("Invalid choice")

    text = input("Enter the string: ")
    while True:
        try:
            key = int(input("Enter the key: "))
            break
        except ValueError:
            print("Invalid key")

    if choice == 'e':
        result = encrypt(text, key)
    else:
        result = decrypt(text, key)

    print(f"Result: {result}")
    print(f"Length of the result: {len(result)}")

caesar_cipher()
