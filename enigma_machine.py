# Make lists
message = []
final_message = []

# Create a dictionary
cipher = {"a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o", "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", "y":"b", "z":"a",}
# Ask user if they want to encrypt or decrypt a message
def choice():
    while True:
        choice = input("Do you want to [e]ncrypt or [d]ecrypt a message").strip().title()
        if choice == "E":
            encrypt()
            break
        elif choice== "D":
            decrypt()
            break
        else:
            print("Please enter a valid answer")

# Encrypting function
def encrypt():
    # Accept a string that will either encrypt or decrypt
    message = input("Enter a message you want to encrypt: ").strip().lower()
    for letter in message:
        if letter in cipher:
            final_message.append(cipher[letter])
        else:
            print("Oh no")
    print(final_message)
    restart()
# Decrypting function
def decrypt():
    # Accept a string that will either encrypt or decrypt
    print("jovn")
    restart()

# Ask user if they want to use the program again
def restart():
    while True:
        restart = input("Do you want to do another encryption or decryption? [Y]es or [N]o").strip().title()
        if restart == "Y":
            choice()
            break
        elif restart == "N":
            print("Goodbye") 
            break
        else:
            print("Please enter a valid answer")
# Tell user what cipher the program is using
print("Hello, and welcome to the Enigma machine. This machine only works with the atbash cipher")
choice()

# Print the final encrypted or decrypted string to the user




