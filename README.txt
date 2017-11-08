SECRET MESSAGES PROJECT

This tool is allows users to encrypt and/or decrypt messages using three different cipher techniques. Users can
select which cipher technique they would like to use, and whether or not they would prefer to encrypt or decrypt a
message they provide via the selected cipher technique.

Getting Started

To begin the program, run the cipher_program.py file. Once the main menu is displayed, follow the prompts presented to
select encryption or decryption functionality, and which cipher technique you care to use.

Encrypting a Message

Once a message is encrypted, it will be stored in a global database (at this time, simply a list ;) ) of encrypted
messages, along with a PIN required to open the file for any user trying to decrypt it. To assign this PIN, enter a
four digit number once prompted prior to encrypting your message.

Character Blocking

All encrypted messages will be displayed within character blocks of five. When needed, padding is added to the end of
the encrypted message to ensure full blocks of five characters. This padding is as follows:
1) "1" for Polybius cipher
2) "S" for Bifid and Keyword ciphers
Users must now that this padding exists as a security feature, and that the padding must be removed by the user
prior to decrypting the message.

Decrypting a Message

There are two options for decrypting a message:
1) Decrypting a message already in the database (this requires a PIN to decrypt)
2) Decrypting a message not placed in the database by another user
In scenario #1, a user must provide the PIN associated with the message to decrypt it. If the PIN is incorrect, the
message will not be decrypted and the user will be sent back to the main menu (this is a security feature). Scenario #2
does not require a PIN and any message that is provided will be decrypted via the cipher technique selected.

Exiting the program

To exit the program, select the 'Quit' option within the main menu

Authors

This program was written by Cory Hooyman - Treehouse Student
