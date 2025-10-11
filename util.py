import random
import string


def random_email():
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(4, 6)))
    digits = ''.join(random.choice(string.digits) for _ in range(random.randint(3, 5)))
    domains = ['icloud.com', 'gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com']
    return f"{letters}{digits}@{random.choice(domains)}"


def generate_username():
    characters = string.ascii_lowercase + string.digits
    length = random.randint(7, 10)
    username = ''.join(random.choice(characters) for _ in range(length))
    return username


def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
