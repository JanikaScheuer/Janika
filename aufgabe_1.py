def encode(message, key):
    
    # static variables
    msg_len = len(message)
    alfa = 'abcdefghijklmnopqrstuvwxyz'
    out_message = ''
    
    for letter in message:
      if letter.lower() not in alfa:
        print('invalid letter')
        break
      if letter == letter.lower():
        # search letter position in alphabet
        letter_pos = alfa.index(letter)
      
        # rules for translating shift to letter position
        if key > msg_len:
          shift = key % msg_len
        elif key < msg_len:
          shift = msg_len ** key
        elif key == msg_len:
          shift = key + msg_len
        else:
          shift = key
        new_letter_pos = letter_pos + shift

        # make position stay in alphabet
        if new_letter_pos > 25:
          new_letter_pos = new_letter_pos % 25
        # Get new letter and add to output message
        new_letter = alfa[new_letter_pos]
      else:
        new_letter = letter
      
      out_message = out_message + new_letter
    return out_message

message_list = [
  ['SSSSSlkjlkjlkjsdfdFFF', 8],
  ['asFFfasfasf', 2],
  ['ljikMMMsdlg', 623],
  ['luuuukjsdf', 8],
]

for msg in message_list:
  output_message = encode(msg[0], msg[1])
  print(output_message)