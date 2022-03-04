def encode(user_message, user_key):
    final_message = ''

    for i in range(len(user_message)):
        message_input = ord(user_message[i]) + user_key
        final_message += chr(message_input)

    return final_message


def encode_better(user_message, user_key, file_name):
    final_message = ''

    for i in range(len(user_message)):
        message_input = ord(user_message[i]) - 65
        convert_key = ord(user_key[i % len(user_key)]) - 65
        new_code = message_input + convert_key
        shift_message = new_code % 58
        result_char = chr(shift_message + 65)
        final_message += result_char

    return final_message
