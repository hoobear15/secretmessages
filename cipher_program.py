from polybius_cipher import polybius
from bifid_cipher import Bifid
from character_blocker import blocker
from keyword_cipher import Keyword

CIPHERBANK = [] # global variable for all ciphers

def main():

    print("Welcome to the cipher processor!\n\n")

    while True:

        command = main_menu() # print main menu of decrypt or encrypt and return command

        if command == "quit":
            exit()
        elif command == "encrypt" or "decrypt":
            selection, message = cipher_list() # list ciphers to perform, then return cipher
        else:
            print("You did not enter a valid number, please try again\n")
            input("(press enter to continue)\n")
            continue

        displaytext, alert = produce_cipher(command, selection, message)

        input(alert+"\n")
        print(displaytext + "\n")
        input("Press ENTER to continue" + "\n")

def main_menu():

    print("\n1.  Encrypt\n2.  Decrypt\n3.  Quit\n")

    selection = int(input("What would you like to do? >>> "))

    if selection == 1:
        return "encrypt"
    elif selection == 2:
        return "decrypt"
    elif selection == 3:
        return "quit"
    else:
        return "not_right"

def cipher_list():

    print("\n1.  Polybius\n2.  Bifid\n3.  Keyword\n4.  Quit\n")

    selection = int(input("Select the method you would like to use >>> "))

    message = str(input("What is the message? >>> "))

    if selection == 1:
        return "Polybius", message
    elif selection == 2:
        return "Bifid", message
    elif selection == 3:
        return "Keyword", message
    elif selection == 4:
        return "quit"
    else:
        return "not_right"

def produce_cipher(command, selection, message):

    if command == "encrypt":

        if selection == "Polybius":
            newcipher = polybius(message, "encrypt")
        elif selection == "Bifid":
            newcipher = Bifid(message, "encrypt")
        elif selection == "Keyword":
            newcipher = Keyword(message, "encrypt")
        else:
            raise ValueError("The cipher type selection was not valid")

        newcipher.encrypt()

        CIPHERBANK.append(newcipher)

        alert = "Your message has been placed into our cipher " \
                "database; Press ENTER to view the encryption"

        return blocker(newcipher.encrypted), alert

    elif command == "decrypt":

        if selection == "Polybius":
            newcipher = polybius(message, "decrypt")
        elif selection == "Bifid":
            newcipher = Bifid(message, "decrypt")
        elif selection == "Keyword":
            newcipher = Keyword(message, "decrypt")
        else:
            raise ValueError("The cipher type selection was not valid")

        newcipher.decrypt()

        result = True

        for e in CIPHERBANK:
            if e.message.upper() == newcipher.decrypted:
                result = e.pad_check()
                break

        if result:

            alert = "Your message has been decrypted; Press ENTER to view it"
            return newcipher.decrypted, alert

        else:

            alert = "You do not have the correct PIN - "
            return "Your message was not decrypted", alert

main()





