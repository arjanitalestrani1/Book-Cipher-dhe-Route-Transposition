# =======================================
#   BOOK CIPHER ENCRYPTION 
# =======================================

def clean_text(text):
    return text.lower().replace("\n", " ").split()


def build_book_index(book_text):
    words = clean_text(book_text)
    index_map = {}

    for i, word in enumerate(words, start=1):
        if word not in index_map:
            index_map[word] = []
        index_map[word].append(i)

    return index_map


def book_cipher_encrypt(message, book_text):
    index_map = build_book_index(book_text)
    message_words = clean_text(message)

    encrypted = []

    for word in message_words:
        if word in index_map:
            encrypted.append(str(index_map[word][0]))
        else:
            encrypted.append("?")

    return " ".join(encrypted)


