import re


class Validator:
    def is_email_valid(self, email):
        """Validate if the given email address is in correct format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def is_phone_valid(self, phone):
        """Validate if the given phone number is in correct format."""
        pattern = r'^\+?1?-?\.?\s?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
        return bool(re.match(pattern, phone))

    def is_url_valid(self, url):
        """Validate if the given URL is in correct format."""
        pattern = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
        return bool(re.match(pattern, url))

    def is_password_strong(self, password):
        """Check if password meets strong password criteria."""
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True

    def is_credit_card_valid(self, card_number):
        """Validate credit card number using Luhn algorithm."""
        card_number = card_number.replace(' ', '').replace('-', '')
        if not card_number.isdigit():
            return False
        
        total = 0
        reverse_digits = card_number[::-1]
        
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n = n // 10 + n % 10
            total += n
        
        return total % 10 == 0

    def is_age_valid(self, age):
        """Check if age is within valid range (0-150)."""
        try:
            age_int = int(age)
            return 0 <= age_int <= 150
        except (ValueError, TypeError):
            return False

    def is_username_valid(self, username):
        """Validate username format (3-20 chars, alphanumeric and underscore only)."""
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return bool(re.match(pattern, username))

    def is_zip_code_valid(self, zip_code):
        """Validate US zip code format."""
        pattern = r'^\d{5}(-\d{4})?$'
        return bool(re.match(pattern, zip_code))