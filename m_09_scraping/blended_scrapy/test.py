hex_string = "77 77 77 2E 63 75 62 69 73 74 2E 65 75 2F 67 30"
hex_bytes = bytes.fromhex(hex_string.replace(" ", ""))
print(hex_bytes.decode("utf-8"))
