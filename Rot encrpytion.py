def rot(message, N):
    encryption = []
    N = N % 26
    for ch in message:
        if 'a' <= ch <= 'z':
            encryption.append(chr((ord(ch) - ord('a') + N) % 26 + ord('a'))) # LOWERcase characters
        elif 'A' <= ch <= "Z":
            encryption.append(chr((ord(ch) - ord('A') + N) % 26 + ord('A'))) # UPPERcase characters
        else:
            encryption.append(ch) # SPECIAL characters
            
    return ''.join(encryption)

N = int(input("Enter your encryption margin: "))
message = input("Enter your message: ")
encrypted_message = rot(message, N)
print(f"{encrypted_message}")
