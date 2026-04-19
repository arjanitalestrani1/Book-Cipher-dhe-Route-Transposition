from ciphers.route_transposition_cipher import (
    encrypt_column_route,
    encrypt_zigzag_route,
    decrypt_column_route,
    decrypt_zigzag_route
)

from ciphers.book_cipher import (
    book_cipher_encrypt,
    book_cipher_decrypt
)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_text(prompt):
    while True:
        text = input(prompt)
        if text.strip() == "":
            print("Input cannot be empty!")
        else:
            return text


def safe_decrypt(func, text, *args):
    try:
        return func(text, *args)
    except Exception:
        return "Invalid input! Please enter valid encrypted text."



while True:
    print("\n==============================")
    print("        MAIN MENU")
    print("==============================")
    print("1. Book Cipher")
    print("2. Route Cipher")
    print("3. Exit")

    choice = input("Enter option: ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        continue

    if choice == "3":
        print("Goodbye!")
        break

    # ================= BOOK =================
    elif choice == "1":

        print("\n==============================")
        print("        BOOK CIPHER")
        print("==============================")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back")

        action = input("Enter option: ")

        if action not in ["1", "2", "3"]:
            print("Invalid choice!")
            continue

        if action == "3":
            continue

        text = get_text("Enter text: ")
        book_text = get_text("Enter book text: ")

        if action == "1":
            print("\nResult:", book_cipher_encrypt(text, book_text))

        elif action == "2":
            print("\nResult:", safe_decrypt(book_cipher_decrypt, text, book_text))


    # ================= ROUTE =================
    elif choice == "2":

        print("\n==============================")
        print("        ROUTE CIPHER")
        print("==============================")
        print("1. Column")
        print("2. ZigZag")
        print("3. Back")

        route = input("Enter option: ")

        if route not in ["1", "2", "3"]:
            print("Invalid choice!")
            continue

        if route == "3":
            continue

       
        if route == "1":
            title = "Column Route Cipher"
        else:
            title = "ZigZag Route Cipher"

        print("\n==============================")
        print(f"   {title}")
        print("==============================")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Back")

        action = input("Enter option: ")

        if action not in ["1", "2", "3"]:
           print("Invalid choice!")
           continue

        if action == "3":
           continue

        text = get_text("Enter text: ")
        cols = get_int("Enter columns: ")

        if route == "1" and action == "1":
            print("\nResult:", encrypt_column_route(text, cols))

        elif route == "1" and action == "2":
            print("\nResult:", safe_decrypt(decrypt_column_route, text, cols))

        elif route == "2" and action == "1":
            print("\nResult:", encrypt_zigzag_route(text, cols))

        elif route == "2" and action == "2":
            print("\nResult:", safe_decrypt(decrypt_zigzag_route, text, cols))