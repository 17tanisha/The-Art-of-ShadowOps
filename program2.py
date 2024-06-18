def caesar_cipher():
    def shift_char(char, key):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + key) % 26 + base)
        else:
            return char

    def caesar(text, key, mode):
        if mode == 'd':
            key = -key
        return ''.join(shift_char(char, key) for char in text)

    file_name = input("Enter the file name: ").strip()
    try:
        with open(file_name, 'r') as file:
            original_text = file.read()
    except FileNotFoundError:
        print("File not found.")
        return

    key = input("Enter the key: ").strip()
    while not key.isdigit():
        print("Invalid key, please enter a numerical value.")
        key = input("Enter the key: ").strip()
    
    key = int(key)

    mode = input("Encrypt (e) or Decrypt (d)? ").strip().lower()
    while mode not in ['e', 'd']:
        print("Invalid choice.")
        mode = input("Encrypt (e) or Decrypt (d)? ").strip().lower()

    result = caesar(original_text, key, mode)

    with open("output.txt", 'w') as output_file:
        output_file.write(result)

    print("Output written to output.txt.")

caesar_cipher()
