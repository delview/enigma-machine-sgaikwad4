# Make lists
final_message = []

# Create a dictionary
cipher_atbash = {"a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o", "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", "y":"b", "z":"a",}
# Ask user if they want to encrypt or decrypt a message
def choice():
    while True:
        choice = input("Do you want to [e]ncrypt or [d]ecrypt a message").strip().title()
        if choice == "E":
            atbash()
            break
        elif choice== "D":
            pass
            break
        else:
            print("Please enter a valid answer")

# Encrypting function
def atbash():
    # Accept a string that will either encrypt or decrypt
    message = input("Enter a message you want to encrypt: ").strip().lower()
    for letter in message:
        if letter in cipher_atbash:
            final_message.append(cipher_atbash[letter])
        else:
            print("Oh no")
    print("".join(map(str, final_message)))
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




