import random

def generate_otp_key(length, seed):
    """
    Generate a pseudo-random OTP key based on a seed (e.g., user's name).
    """
    random.seed(seed)  # Use the seed to initialize the PRNG
    return [random.randint(0, 95) for _ in range(length)]  # Ensure key values are within range for printable characters

def encrypt(message, seed):
    """
    Encrypt a message using a one-time pad derived from the seed.
    The encrypted message will consist of printable characters.
    """
    key = generate_otp_key(len(message), seed)
    encrypted = ''.join(chr(((ord(char) - 32 + k) % 95) + 32) for char, k in zip(message, key))
    return encrypted, key

def decrypt(encrypted_message, seed):
    """
    Decrypt a message using the seed.
    """
    key = generate_otp_key(len(encrypted_message), seed)
    decrypted = ''.join(chr(((ord(char) - 32 - k) % 95) + 32) for char, k in zip(encrypted_message, key))
    return decrypted

# Example usage
seed = "Md_Mehedi_Hasan"  # Input seed for reproducibility
message = "Mehedi"         # Message to encrypt

# Encrypt the message
encrypted_message, key = encrypt(message, seed)
print("Encrypted Output:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, seed)
print("Decrypted Output:", decrypted_message)