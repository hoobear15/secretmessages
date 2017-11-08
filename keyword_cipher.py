from cipher import Cipher


class Keyword(Cipher):
    """From a new cipher parent class, creates a keyword specific cipher class"""

    def __init__(self, text, status):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        super().__init__(text, status)

    def decrypt(self):
        """take an encrypted message and decrypts it, storing the value in self.decrypted attribute"""
        # get message of instance and keyword used to encrypt
        message = list(self.message)

        while True:
            kryptoalpha = input("What is the keyword used to decrypt "
                                "this message? >>> ").upper()
            if isinstance(kryptoalpha, str):
                kryptoalpha = self.krypto_alpha(list(str(kryptoalpha)))
                break
            else:
                print("Please ensure you are using only letters in your keyword; Try again")

        # decrypt message by swapping index values from alphabet and krypto alphabet
        for i in range(len(message)):
            if message[i] == " ":
                pass
            else:
                message[i] = self.alphabet[kryptoalpha.index(message[i])]

        message = "".join(message)

        self.decrypted = message

    def encrypt(self):
        """take a message and encrypts it using the keyword method (obtaining the keyword to encrypt with from the user)
         storing the value in self.encrypted attribute"""
        # encrypt the message from text
        message = list(self.message.upper())  # define the message, where we will store the
        # decrypted message once complete

        while True:
            kryptoalpha = input("You need a keyword to encrypt your message; "
                                "What keyword would you like to use? >>> ").upper()
            if isinstance(kryptoalpha, str):
                kryptoalpha = self.krypto_alpha(list(str(kryptoalpha)))
                break
            else:
                print("Please ensure you are using only letters in your keyword; Try again")

        # encrypt message by swapping index values from alphabet and krypto alphabet
        for i in range(len(message)):
            if message[i] == " ":
                pass
            else:
                message[i] = kryptoalpha[self.alphabet.index(message[i])]

        message = "".join(message)

        self.encrypted = message

    def krypto_alpha(self, keyword):
        """"creates the alphabet that will be used to encrypt messages, developed using a keyword given by the user"""

        kryptoalpha = []

        for c in keyword:
            if c in kryptoalpha:
                pass
            else:
                kryptoalpha.append(c)

        for c in self.alphabet:
            if c in kryptoalpha:
                pass
            else:
                kryptoalpha.append(c)

        return kryptoalpha

