# Caesar Cipher Program

This program implements a simple Caesar cipher for encrypting and decrypting text based on a user-defined shift value. The user can choose to either encrypt or decrypt a message, and the shift is applied accordingly.

## Features
- **Encrypt Text:** Converts input text into an encrypted form using a Caesar cipher with a shift value.
- **Decrypt Text:** Converts an encrypted message back to its original form by reversing the shift.
- **Error Handling:** Handles invalid inputs and exceptions gracefully, providing user feedback.

## How It Works
The program shifts each letter of the input text by a number of positions defined by the shift value:
- Uppercase letters are shifted within the range of ASCII values for uppercase letters.
- Lowercase letters are shifted within the range of ASCII values for lowercase letters.
- Non-alphabetic characters are not modified.

### Example

If the input is `HELLO` and the shift is `3`, the encrypted message will be `KHOOR`.

### Encryption
```
def encrypt(text, shift):
    # Encrypts the text using the Caesar cipher algorithm
```

### Decryption
```
def decrypt(text, shift):
    # Decrypts the text by reversing the shift
```

## Functions

### `encrypt(text, shift)`
Encrypts a given `text` using the Caesar cipher technique with a specified `shift` value.

- **Parameters:**
  - `text` (str): The text to be encrypted.
  - `shift` (int): The number of positions to shift each character.
  
- **Returns:**
  - (str): The encrypted text.

### `decrypt(text, shift)`
Decrypts a given `text` by reversing the Caesar cipher technique with a specified `shift` value.

- **Parameters:**
  - `text` (str): The text to be decrypted.
  - `shift` (int): The number of positions to reverse the shift.

- **Returns:**
  - (str): The decrypted text.

### `get_valid_choice()`
Asks the user to choose whether they want to encrypt or decrypt a message. Repeats the question until the user provides a valid choice (`e` or `d`).

- **Returns:**
  - (str): `'e'` for encrypt or `'d'` for decrypt.

### `get_valid_shift()`
Asks the user for a valid integer to be used as the shift value. Repeats the question until the user provides a valid integer.

- **Returns:**
  - (int): The valid shift value.

### `main()`
The main function that handles user input and calls the appropriate functions to either encrypt or decrypt a message based on the user's choice.

## How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/georgestas1/PRODIGY_CS_01.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd PRODIGY_CS_01
   ```

3. **Run the Program:**
   ```bash
   python caesar_cipher.py
   ```

4. **Follow the prompts:**
   - Enter the message you want to encrypt or decrypt.
   - Enter the shift value (an integer).
   - The program will display the encrypted or decrypted message.

## Example Usage

### Encrypting a message
```
Do you want to (e)ncrypt or (d)ecrypt? e
Enter your message: hello
Enter shift value (integer): 3
Encrypted message: khoor
```

### Decrypting a message
```
Do you want to (e)ncrypt or (d)ecrypt? d
Enter your message: khoor
Enter shift value (integer): 3
Decrypted message: hello
```

## Error Handling
- If the user enters an invalid shift value (not an integer), the program will ask again until a valid integer is provided.
- If an unexpected error occurs, the program will print an error message.

## License
This project is licensed under the MIT License.
