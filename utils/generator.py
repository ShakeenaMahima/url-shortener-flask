import random
import string
from models.url import URL

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_unique_code():
    while True:
        code = generate_short_code()
        if not URL.query.filter_by(short_code=code).first():
            return code
