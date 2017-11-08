def blocker(encrypted_message, cipher):
    """will take an encrypted message and turn it into a message in blocks of five characters each"""

    encrypted_message = list(encrypted_message)
    chunk = 5 - (len(encrypted_message) % 5)
    blocked_message = ""

    while encrypted_message:
        for i in range(5):
            if len(encrypted_message) < 1:
                break
            blocked_message += encrypted_message.pop(0)
        if len(encrypted_message) > 0:
            blocked_message += " "

    if ("1" or "2" or "3" or "4" or "5") in blocked_message:
        fill = "1"
    else:
        fill = "S"

    if len(blocked_message) > 4:
        while chunk > 0:
            blocked_message += fill
            chunk -= 1
    else:
        while chunk > 0:
            blocked_message += fill
            chunk -= 1

    return blocked_message

