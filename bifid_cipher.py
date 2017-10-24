from cipher import Cipher

class Bifid(Cipher):
    """From a new cipher parent class, creates a bifid specific cipher class"""
    def __init__(self,text,status):
        self.alphabet = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")
        self.pair = [(x, y) for x in range(1, 6) for y in range(1, 6)]
        self.grid = {letter: coord for letter, coord in zip(self.alphabet, self.pair)}
        super().__init__(text,status)

    def decrypt(self):
        """take an encrypted message and decrypts it, storing the value in self.decrypted attribute"""
        message = list(self.message.upper())

        decryptcoords = []
        numberline = []

        for e in message:
            numberline.append(self.grid[e][0])
            numberline.append(self.grid[e][1])

        for i in range(int(len(numberline)/2)):
           decryptcoords.append((numberline[i], numberline[i+int((len(numberline)/2))]))

        message = ""

        for e in decryptcoords:
            for key, value in self.grid.items():
                if value == e:
                    message += key

        self.decrypted = message


    def encrypt(self):
        """take a message and encrypts it using the bifid method, storing the value in self.encrypted attribute"""
        message = list(self.message.upper())

        encryptcoords = []
        numberline = []

        # assign coordinate to each letter in the message
        for e in message:
            if e == " ":
                pass
            else:
                encryptcoords.append(self.grid[str(e).upper()])

        # get series of two numbers for each letter and translate them into two lines of numbers
        for i in range(len(encryptcoords)):
            numberline.append(encryptcoords[i][0])

        for i in range(len(encryptcoords)):
            numberline.append(encryptcoords[i][1])

        # combine sequence of two letters, swap with each letter in regular message
        swap = []
        for e in range(1,len(numberline),2):
            for key, value in self.grid.items():
                if value == (numberline[e-1],numberline[e]):
                    swap.append(key)

        message = "".join(swap)

        self.encrypted = message

