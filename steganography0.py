from PIL import Image

# ------------------------
# Simple XOR encryption/decryption for optional key
# ------------------------
def xor_encrypt_decrypt(text: str, key: str) -> str:
    if not key:
        return text  # No key, return as is
    key_bytes = key.encode("utf-8")
    text_bytes = text.encode("utf-8")
    result = bytearray()
    for i in range(len(text_bytes)):
        result.append(text_bytes[i] ^ key_bytes[i % len(key_bytes)])
    return result.decode("utf-8", errors="ignore")


# ------------------------
# Hide Message in Image using LSB
# ------------------------
def hide_message_lsb(image_path: str, message: str, output_path: str, key: str = ""):
    # Apply XOR if key provided
    if key:
        message = xor_encrypt_decrypt(message, key)

    # Add delimiter to detect end of message
    message += "%%END%%"
    binary_message = ''.join([format(ord(ch), "08b") for ch in message])

    # Open image
    img = Image.open(image_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size
    capacity = width * height * 3  # each channel can store 1 bit

    if len(binary_message) > capacity:
        raise ValueError("Message too long to hide in this image!")

    data_index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if data_index < len(binary_message):
                r = (r & ~1) | int(binary_message[data_index])
                data_index += 1
            if data_index < len(binary_message):
                g = (g & ~1) | int(binary_message[data_index])
                data_index += 1
            if data_index < len(binary_message):
                b = (b & ~1) | int(binary_message[data_index])
                data_index += 1
            pixels[x, y] = (r, g, b)
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    img.save(output_path)


# ------------------------
# Extract Message from Image
# ------------------------
def extract_message_lsb(image_path: str, key: str = "") -> str:
    img = Image.open(image_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size
    binary_data = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    # Split into bytes
    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) < 8:
            continue
        message += chr(int(byte, 2))
        if message.endswith("%%END%%"):
            message = message[:-7]  # remove delimiter
            break

    # Decrypt if key provided
    if key:
        message = xor_encrypt_decrypt(message, key)

    return message
