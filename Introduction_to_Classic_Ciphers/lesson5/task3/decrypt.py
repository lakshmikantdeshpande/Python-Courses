from pre_treat_message import pre_treat_message

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(message):

    message = pre_treat_message(message)

    decrypted_message = ''

    # assemble the plaintext message by decrypting the message one letter at a time
    for c in message:
        if c not in ALPHABET:
            decrypted_message += c
            continue

        # find the corresponding decrypted letter and append it to decrypted_message
        index_of_alphabet = ALPHABET.find(c)
        replacement_alphabet = ALPHABET[len(ALPHABET) - 1 - index_of_alphabet]
        decrypted_message += replacement_alphabet

    return decrypted_message


# do not modify this file beyond this point
MESSAGE_ONE = 'RG RH HGROO HMLDRMT'
MESSAGE_TWO = 'HSLFOW DV TL HOVWWRMT'
MESSAGE_THREE = 'R XZMMLG URMW NB YLLGH'

print decrypt(MESSAGE_ONE)
print decrypt(MESSAGE_TWO)
print decrypt(MESSAGE_THREE)
