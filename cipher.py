class Cipher:

    def __init__(self,text,status):
        self.message = str(text).upper().replace(" ","")
        if status == "encrypt":
            self.pad = str(input("A one time PIN will secure this message, what four digit pin would you like to use? >>> "))
        self.encrypted = ""
        self.decrypted = ""

    def pad_check(self):
        return (str(input("This message requires a PIN to decrypt, please enter it: >>> ")) == self.pad)




