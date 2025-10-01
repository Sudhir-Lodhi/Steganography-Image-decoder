from PIL import Image

def _str_to_bin(message, key=None):
    binary = ''.join(format(ord(c), '08b') for c in message)
    
    if key:
        key_bin = ''.join(format(ord(k), '08b') for k in key)
        key_len = len(key_bin)
        binary = ''.join(
            str(int(b) ^ int(key_bin[i % key_len]))
            for i, b in enumerate(binary)
        )
    
    binary += '1111111111111110'  # End-of-message marker
    return binary

def _bin_to_str(binary, key=None):
    if key:
        key_bin = ''.join(format(ord(k), '08b') for k in key)
        key_len = len(key_bin)
        binary = ''.join(
            str(int(b) ^ int(key_bin[i % key_len]))
            for i, b in enumerate(binary)
        )
    
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ''
    for byte in chars:
        if len(byte) < 8:
            continue
        message += chr(int(byte, 2))
    return message

def hide_message_lsb(image_path, message, output_path, key=None):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = list(img.getdata())

    binary_msg = _str_to_bin(message, key)
    msg_len = len(binary_msg)

    if msg_len > len(pixels) * 3:
        raise ValueError("Message too large for this image!")

    new_pixels = []
    msg_index = 0

    for pixel in pixels:
        r, g, b = pixel
        if msg_index < msg_len:
            r = (r & 0xFE) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < msg_len:
            g = (g & 0xFE) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < msg_len:
            b = (b & 0xFE) | int(binary_msg[msg_index])
            msg_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)

def extract_message_lsb(image_path, key=None):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = list(img.getdata())

    binary_msg = ''
    for pixel in pixels:
        r, g, b = pixel
        binary_msg += str(r & 1)
        binary_msg += str(g & 1)
        binary_msg += str(b & 1)

    end_marker = binary_msg.find('1111111111111110')
    if end_marker != -1:
        binary_msg = binary_msg[:end_marker]

    return _bin_to_str(binary_msg, key)
