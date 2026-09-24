from modules.hash import hash_file, verify_integrity
from modules.encryption import aes_encryption_decryption, rsa_encryption_decryption
from modules.password import check_strength, hash_password, verify_password
from getpass import getpass

def menu():
    print("\nSelect operation: ")
    print("1. Hash file")
    print("2. Check file integrity")
    print("3. AES Encrypt/Decrypt")
    print("4. RSA Encrypt/Decrypt")
    print("5. Password Manager")
    print("0. Exit")

print("""
Initializing Cryptography Toolkit v1.0...

Here you can:
    - Analyze and hash files to detect tampering
    - Encrypt and decrypt messages with AES and RSA
    - Securely manage passwords and assess their strength

All systems online. Data protection protocols active!
""")

while True:
    menu()
    choice = input("Enter choice(0-5):")
    if choice == "0":
        break
    elif choice == "1":
        file_path = input("Enter file path: ")
        print(f"\nSHA Hash of File is: {hash_file(file_path)}")
    elif choice == "2":
        file_path1 = input("Enter file path 1: ")
        file_path2 = input("Enter file path 2: ")
        print(verify_integrity(file_path1, file_path2))
    elif choice == "3":
        message = input("Enter message: ")
        key, ciphertext, plaintext = aes_encryption_decryption(message)
        print(f"AES Key: {key}")
        print(f"AES Ciphertext: {ciphertext}")
        print(f"AES Plaintext: {plaintext}")
    elif choice == "4":
        message = input("Enter message: ")
        ciphertext, plaintext = rsa_encryption_decryption(message)
        print(f"RSA message, encrypted with a public key: {ciphertext}")
        print(f"RSA message, decrypted with a private key: {plaintext}")
    elif choice == "5":
        while True:
            password1 = getpass("Enter a password to check strength: ")
            print(check_strength(password1))
            if check_strength(password1).startswith("Weak"):
                print("Please choose a stronger password.")
            else:
                break
        hashed_password = hash_password(password1)
        print(f"Hashed password: {hashed_password}")
        attempt = getpass("Re-enter the password to verify: ")
        print(verify_password(attempt, hashed_password))
    else:
        print("Invalid choice.")

print("Exiting...Stay sharp and secure out there!")