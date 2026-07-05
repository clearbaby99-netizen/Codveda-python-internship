import os

def caesar_cipher(text, shift, decrypt=False):
    # If decrypting, we reverse the shift direction
    if decrypt:
        shift = -shift
        
    result = ""
    for char in text:
        # Encrypt/Decrypt printable characters securely
        # Using modular arithmetic (modulo 256) ensures all standard characters are safely handled
        result += chr((ord(char) + shift) % 256)
    return result

def process_file():
    print("--- Basic File Encryption/Decryption ---")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Select an option (1 or 2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice.")
        return
        
    file_path = input("Enter the text file name or path (e.g., balance_sheet.txt): ")
    
    if not os.path.exists(file_path):
        print("Error: The file does not exist!")
        return
        
    try:
        # Ask for a shift key (must be a whole number)
        key = int(input("Enter an encryption key (a number, e.g., 5): "))
    except ValueError:
        print("Invalid key. Please enter a valid integer.")
        return

    try:
        # Read the original file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if choice == '1':
            # Encrypting
            processed_content = caesar_cipher(content, key, decrypt=False)
            output_file = "encrypted_" + file_path
            message = "File encrypted successfully!"
        else:
            # Decrypting
            processed_content = caesar_cipher(content, key, decrypt=True)
            output_file = "decrypted_" + file_path
            message = "File decrypted successfully!"
            
        # Write the outcome to a new file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(processed_content)
            
        print(f"{message} Saved as: '{output_file}'")
        
    except Exception as e:
        print(f"An error occurred while handling the file: {e}")

# Run the encryption tool
process_file()
