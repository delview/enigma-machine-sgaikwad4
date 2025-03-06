

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
    
# Accept a string that will either encrypt or decrypt

# Encrypting function
def encrypt():
    print("hello")
# Decrypting function
def decrypt():
    print("jovn")

# Tell user what cipher the program is using
print("Hello, and welcome to the Enigma machine. This machine only works with the atbash cipher")
choice()

# Print the final encrypted or decrypted string to the user

# Ask user if they want to use the program again