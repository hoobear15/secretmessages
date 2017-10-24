def blocker(encrypted_message):

    encrypted_message = list(encrypted_message)
    blocked_message = ""

    while encrypted_message:
        for i in range(5):
            if len(encrypted_message) < 1:
                return blocked_message
            blocked_message += encrypted_message.pop(0)
        blocked_message += " "

    return blocked_message





