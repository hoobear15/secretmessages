from cipher import Cipher

class Keyword(Cipher):

    def __init__(self,text,status):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        super().__init__(text,status)

    def decrypt(self):
        """take an encrypted message and decrypts it, storing the value in self.decrypted attribute"""
        # get message of instance and keyword used to encrypt
        message = list(self.message)
        kryptoalpha = self.krypto_alpha(list(str(input("What is the keyword used to decrypt this message? >>> ").upper())))

        # decrypt message by swapping index values from alphabet and krypto alphabet
        for i in range(len(message)):
            if message[i] == " ":
                pass
            else:
                message[i] = self.alphabet[kryptoalpha.index(message[i])]

        message = "".join(message)

        self.decrypted = message


    def encrypt(self):
        """take a message and encrypts it using the bifid method, storing the value in self.encrypted attribute"""
        # encrypt the message from text
        message = list((self.message).upper())  # define the message, where we will store the decrypted message once complete
        kryptoalpha = self.krypto_alpha(list(str(input("You need a keyword to encrypt your message; "
                                                       "What keyword would you like to use? >>> ").upper()))) # obtain krypto alphabet

        # encrypt message by swapping index values from alphabet and krypto alphabet
        for i in range(len(message)):
            if message[i] == " ":
                pass
            else:
                message[i] = kryptoalpha[self.alphabet.index(message[i])]

        message = "".join(message)

        self.encrypted = message



    def krypto_alpha(self, keyword):

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

