import random
import string

def generate_password(length):
    """Generate a random password with user specified length."""
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    # Define possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one of each type
    password = [
        random.choice(string.ascii_lowercase),  # Lowercase
        random.choice(string.ascii_uppercase),  # Uppercase
        random.choice(string.digits),          # Digit
        random.choice(string.punctuation)      # Special character
    ]

    # Filling the rest of the password length with random choices
    password += random.choices(characters, k=length - 4)

    # Shuffle the password list and join it into a string
    random.shuffle(password)
    return ''.join(password)

# Get user input for password length
try:
    length = int(input("Enter your desired password length: "))
    password = generate_password(length)
    if password:
        print("Generated password:", password)
except ValueError:
    print("Please enter a valid number, with a minimum value of 8 characters.")
