from cipher import Cipher


class Polybius(Cipher):
    """From a new cipher parent class, creates a Polybius specific cipher class"""
    def __init__(self, text, status):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        self.square = list("12345")
        self.pair = [(x, y) for x in self.square for y in self.square]
        self.grid = {letter: coord for letter, coord in zip(self.alphabet, self.pair)}
        super().__init__(text, status)

    def decrypt(self):
        """take an encrypted message and decrypts it, storing the value in self.decrypted attribute"""
        # build decrypted message container
        letters = ""

        # loop through even string of numbers, creating list for coordinates
        for e in range(0, len(self.message)-1, 2):
            setter = (str(self.message[e]), str(self.message[e+1]))
            for key, value in self.grid.items():
                # append coordinate keys to container
                if value == setter:
                    letters += key

        # assign the decrypted message attribute
        self.decrypted = letters

    def encrypt(self):
        """take a message and encrypts it using the polybius method, storing the value in self.encrypted attribute"""
        # build encrypted container
        nums = ""
        self.message = self.message.upper()

        # iterate over message string and add coordinates to container
        for e in self.message:
            if e == " ":
                pass
            else:
                nums += self.grid[e][0]
                nums += self.grid[e][1]

        # assign encrypted message attribute
        self.encrypted = nums



