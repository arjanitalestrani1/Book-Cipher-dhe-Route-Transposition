from route_transposition_cipher import (
    encrypt_column_route,
    encrypt_zigzag_route,
    decrypt_column_route,
    decrypt_zigzag_route
)

from book_cipher import (
    book_cipher_encrypt,
    book_cipher_decrypt
)

print("Choose option:")
print("1. Column Route Encrypt")
print("2. Column Route Decrypt")
print("3. ZigZag Route Encrypt")
print("4. ZigZag Route Decrypt")
print("5. Book Cipher Encrypt")
print("6. Book Cipher Decrypt")

choice = input("Enter choice: ")
text = input("Enter text: ")

if choice in ["1", "2", "3", "4"]:
    cols = int(input("Enter columns: "))

if choice in ["5", "6"]:
    book_text = input("Enter book text: ")

if choice == "1":
    print("Encrypted:", encrypt_column_route(text, cols))

elif choice == "2":
    print("Decrypted:", decrypt_column_route(text, cols))

elif choice == "3":
    print("Encrypted:", encrypt_zigzag_route(text, cols))

elif choice == "4":
    print("Decrypted:", decrypt_zigzag_route(text, cols))

elif choice == "5":
    print("Encrypted:", book_cipher_encrypt(text, book_text))

elif choice == "6":
    print("Decrypted:", book_cipher_decrypt(text, book_text))