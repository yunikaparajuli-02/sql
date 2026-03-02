# Task 1: Encoding and Decoding Demo

import base64

# Step 1: Input message
message = "Hello, Yunika!"

# Step 2: ASCII conversion
ascii_codes = [ord(char) for char in message]
print("ASCII Codes:", ascii_codes)

# Step 3: Base64 encoding
base64_encoded = base64.b64encode(message.encode('utf-8'))
print("Base64 Encoded:", base64_encoded.decode('utf-8'))

# Step 4: Base64 decoding
decoded_message = base64.b64decode(base64_encoded).decode('utf-8')
print("Decoded Message:", decoded_message)