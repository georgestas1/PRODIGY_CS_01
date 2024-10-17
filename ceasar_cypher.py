def encrypt(text, shift):
    try:
        # Initialize an empty string to store the result
        result = ""
        # Loop through each character in the input text
        for i in range(len(text)):
            # Get the current character
            char = text[i]
            # Check if the character is an uppercase letter
            if char.isupper():
                # Encrypt the character and append to the result
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # Check if the character is a lowercase letter
            elif char.islower():
                # Encrypt the character and append to the result
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                # If it's neither, just append the character as is
                result += char
        # Return the encrypted result
        return result
    except Exception as e:
        # Print error message if an exception occurs
        print(f"Error during encryption: {e}")
        return None

def decrypt(text, shift):
    try:
        # Decrypt by calling the encrypt function with a negative shift
        return encrypt(text, -shift)
    except Exception as e:
        # Print error message if an exception occurs
        print(f"Error during decryption: {e}")
        return None

def get_valid_choice():
    while True:
        # Ask the user if they want to encrypt or decrypt
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        # Check if the choice is valid
        if choice in ['e', 'd']:
            return choice
        else:
            # Print error message for invalid choice
            print("Invalid choice. Please select 'e' to encrypt or 'd' to decrypt.")

def get_valid_shift():
    while True:
        try:
            # Ask for the shift value and attempt to convert it to an integer
            shift = int(input("Enter shift value (integer): "))
            return shift
        except ValueError:
            # Print error message for invalid input
            print("Invalid input. Please enter a valid integer for the shift value.")

def main():
    try:
        # Keep asking for valid choice until the user provides one
        choice = get_valid_choice()

        # Get the message from the user
        text = input("Enter your message: ")

        # Keep asking for a valid shift value until the user provides one
        shift = get_valid_shift()

        # Encrypt or decrypt based on the user's choice
        if choice == 'e':
            # Encrypt the message
            encrypted_message = encrypt(text, shift)
            if encrypted_message:
                # Print the encrypted message
                print("Encrypted message:", encrypted_message)
        else:
            # Decrypt the message
            decrypted_message = decrypt(text, shift)
            if decrypted_message:
                # Print the decrypted message
                print("Decrypted message:", decrypted_message)

    except Exception as e:
        # Print error message if an unexpected error occurs
        print(f"An unexpected error occurred: {e}")

# Call the main function if this script is executed
if __name__ == "__main__":
    main()