# Book-Cipher-dhe-Route-Transposition

## Project Description

This project implements two classical encryption techniques:

- Book Cipher  
- Route Transposition Cipher  
  - Column Route  
  - ZigZag Route  

The program provides a simple command-line interface that allows the user to encrypt and decrypt messages using these algorithms.

---

## Project Structure
```
Book-Cipher-dhe-Route-Transposition/
│
├── ciphers/
│ ├── book_cipher.py
│ └── route_transposition_cipher.py
│
├── main.py
├── README.md
└── .gitignore
```

---

## How to Run the Program

### Requirements
- Python 3.x installed  

### Steps

1. Clone the repository:
```bash
git clone https://github.com/arjanitalestrani1/Book-Cipher-dhe-Route-Transposition.git
```

2. Navigate to the project folder:
```bash
cd Book-Cipher-dhe-Route-Transposition
```

3. Run the program:
```bash
python main.py
```


4. Follow the menu instructions in the terminal.

---

## Algorithms Description

### 1. Book Cipher

The Book Cipher is a substitution-based encryption method that uses a shared reference text (book text) as the key.

Instead of encrypting individual characters, this method works at the **word level**, replacing words with their positions in the reference text.

#### Encryption

- The reference text is first processed by:
  - converting all text to lowercase
  - removing unnecessary characters
  - splitting it into individual words

- A data structure (dictionary) is created where:
  - each word is a key
  - the value is a list of positions where that word appears in the text

- The input message:
  - is split into words
  - each word is replaced with its corresponding position in the reference text

- The result is a sequence of numbers representing the encrypted message

#### Decryption

- The ciphertext consists of numeric indices
- Using the same reference text:
  - each number is mapped back to the word at that position
- The words are combined to reconstruct the original message

#### Key Idea

The security of this method relies on both the sender and receiver using the exact same reference text.

---

### 2. Route Transposition Cipher

The Route Transposition Cipher is a transposition-based method, meaning it does not change the characters themselves, but rearranges their positions.

The text is written into a grid and then read following a specific route.

---

### a) Column Route Cipher

#### Encryption

- The input text:
  - has spaces removed
  - is converted to uppercase

- The number of columns is defined by the user

- A grid is created:
  - filled row by row with the characters of the text
  - remaining empty cells are filled with `X`

- The ciphertext is produced by:
  - reading the grid column by column (top to bottom)

#### Decryption

- A grid with the same dimensions is created

- The ciphertext is placed:
  - column by column into the grid

- The original text is recovered by:
  - reading the grid row by row

- Padding characters (`X`) are removed at the end

---

### b) ZigZag Route Cipher

#### Encryption

- The text is written into a grid row by row

- The rows are read in alternating directions:
  - even rows: left → right
  - odd rows: right → left

- This creates a zigzag pattern that changes the order of characters

#### Decryption

- A grid is created with the same dimensions

- The ciphertext is inserted into the grid following the same zigzag pattern

- Once filled:
  - the original message is reconstructed by reading row by row

- Padding characters (`X`) are removed at the end

---

### Summary

- Book Cipher → replaces words with positions (substitution)
- Route Cipher → rearranges characters (transposition)

---

## How to Use the Program

After running the program, a menu will appear in the terminal:
```
1. Book Cipher  
2. Route Cipher  
3. Exit  
```

- Enter the number corresponding to your choice and press Enter.

### Book Cipher

- Choose:
  - 1 for encryption
  - 2 for decryption
- Enter the text you want to process
- Enter the reference book text

### Route Cipher

- Choose the type:
  - 1 for Column Route
  - 2 for ZigZag Route

- Then choose:
  - 1 for encryption
  - 2 for decryption

- Enter the text and number of columns when prompted

## Error Handling

The program validates:
- Empty input  
- Invalid numbers  
- Incorrect encrypted text during decryption  

If decryption fails, a safe message is returned instead of crashing the program.

## Example Executions

### Book Cipher Example

**Input:**
```
Text: hello world
Book Text: hello this is a simple hello world example
```



**Output (example):**
```
Encrypted: 1 6
Decrypted: hello world
```



---

### Column Route Cipher Example

**Input:**
```
Text: HELLO
Columns: 3
```



**Grid:**

```
H E L
L O X
```



**Output:**

```
Encrypted: HLEOLX
Decrypted: HELLO
```



---

### ZigZag Route Cipher Example

**Input:**

```
Text: HELLO
Columns: 3
```



**Grid:**

```
H E L
L O X
```



**Reading ZigZag:**

```
Row 1 → H E L
Row 2 ← X O L
```


**Output:**

```
Encrypted: HELXOL
Decrypted: HELLO
```



---

## .gitignore

The project includes a `.gitignore` file to exclude unnecessary files such as:

```
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.vscode/
.idea/
```


This prevents temporary and system files from being uploaded to the repository.

---

## Notes

- All encryption removes spaces and converts text to uppercase  
- Padding is done using the character `X` when necessary  
- The same parameters (columns or book text) must be used for correct decryption  