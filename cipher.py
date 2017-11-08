class Cipher:
    """creates a new Cipher object; stores original user message as encrypted or decrypted message and
     creates a one time PAD to be used if user requests a decrypted message"""

    def __init__(self, text, status):
        self.message = str(text).upper().replace(" ", "")
        if status == "encrypt":
            while True:
                self.pad = int(input("A one time, four digit PIN will secure this message, "
                                     "what four digit pin would you like to use? >>> "))
                if isinstance(self.pad, int) and len(str(self.pad)) == 4:
                    break
                else:
                    print("Please ensure the PIN you entered uses only numbers and is exactly four digits")
        self.encrypted = ""
        self.decrypted = ""
        self.padding = 0

    def pad_check(self):
        """requests a user to enter a PAD number and returns boolean based on matching (or not) the objects PAD"""
        while True:
            try:
                return int(input("This message requires a PIN to decrypt, please enter it: >>> ")) == self.pad
            except ValueError:
                print("Please ensure the PIN is a number")

    def encrypt(self, message):
        """stub in place should user try to use encrypt method of a basic cipher class"""
        self.message = message
        raise NotImplementedError()

    def decrypt(self, message):
        """stub in place should user try to use decrypt method of a basic cipher class"""
        self.message = message
        raise NotImplementedError()







