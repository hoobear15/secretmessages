from polybius_cipher import Polybius
from bifid_cipher import Bifid
from character_blocker import blocker
from keyword_cipher import Keyword


CIPHERBANK = []  # global variable for all ciphers


def main():
    """will print a menu of options and allow a user to select decrypt or encrypt methods, as well as which cipher
     they would like to use to perform each method; will loop until the program exits"""
    while True:

        print("Welcome to the cipher processor!\n\n")

        command = main_menu()  # print main menu of decrypt or encrypt and return command

        if command == "quit":
            exit()
        elif command == "encrypt" or "decrypt":
            selection, message = cipher_list()  # list ciphers to perform, then return cipher
        else:
            print("You did not enter a valid number, please try again\n")
            input("(press ENTER to continue)\n")

        displaytext, alert = produce_cipher(command, selection, message)

        input(alert+"\n")
        print(displaytext + "\n")
        input("Press ENTER to continue" + "\n")


def main_menu():
    """prints encrypt, decrypt and quit options for the user to select"""

    while True:
        print("\n1.  Encrypt\n2.  Decrypt\n3.  Quit\n")

        while True:
            try:
                selection = int(input("What would you like to do? >>> "))
                break
            except ValueError:
                print("Invalid entry - please select only the options available")

        if selection == 1:
            return "encrypt"
        elif selection == 2:
            return "decrypt"
        elif selection == 3:
            return "quit"
        else:
            print("Your selection was not valid, please enter a valid selection")


def cipher_list():
    """prints Polybius, Bifid and Keyword cipher options, as well as quit option for the user to select"""

    while True:
            try:
                print("\n1.  Polybius\n2.  Bifid\n3.  Keyword\n4.  Quit\n")

                while True:
                    try:
                        selection = int(input("Select the method you would like to use >>> "))
                        if 0 < selection <= 4:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Please enter a valid cipher selection")

                while True:
                    message = str(input("What is the message? >>> "))
                    move = False
                    for e in message:
                        if e in list("!@#$%^&*()_+-\|}]{[:;?/.><,~"):
                            move = True
                        else:
                            pass
                    if move:
                        print("Special characters cannot be processed by the cipher program, "
                              "please enter a new message")
                        continue
                    else:
                        break

                if selection == 1:
                    return "Polybius", message
                elif selection == 2:
                    return "Bifid", message
                elif selection == 3:
                    return "Keyword", message
                elif selection == 4:
                    return "quit"
                else:
                    print("Your cipher selection was not valid, please enter a valid selection (line 87)")

            except TypeError:
                print("Your selection was not valid, please enter a valid selection (line 90)")


def produce_cipher(command, selection, message):
    """takes user message, encryption or decryption preference, and cipher
    option to create a new cipher object and store it in the global cipher database if it does not currently exist"""

    if command == "encrypt":

        if selection == "Polybius":
            newcipher = Polybius(message, "encrypt")
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

        return blocker(newcipher.encrypted, newcipher), alert

    elif command == "decrypt":

        if selection == "Polybius":
            newcipher = Polybius(message, "decrypt")
        elif selection == "Bifid":
            newcipher = Bifid(message, "decrypt")
        elif selection == "Keyword":
            newcipher = Keyword(message, "decrypt")
        else:
            raise ValueError("The cipher type selection was not valid (line 126)")

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





