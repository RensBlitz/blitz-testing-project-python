class StringUtils:
    def capitalize_words(self, text):
        """Capitalize the first letter of each word in the text."""
        return ' '.join(word.capitalize() for word in text.split())

    def reverse_string(self, text):
        """Return the reversed version of the input string."""
        return text[::-1]

    def count_vowels(self, text):
        """Count the number of vowels in the text."""
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)

    def count_consonants(self, text):
        """Count the number of consonants in the text."""
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char.isalpha() and char not in vowels)

    def is_palindrome(self, text):
        """Check if the text is a palindrome (ignoring case and spaces)."""
        cleaned = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned == cleaned[::-1]

    def remove_whitespace(self, text):
        """Remove all whitespace from the text."""
        return ''.join(text.split())

    def word_count(self, text):
        """Count the number of words in the text."""
        return len(text.split())

    def replace_substring(self, text, old, new):
        """Replace all occurrences of old substring with new substring."""
        return text.replace(old, new)

    def starts_with_prefix(self, text, prefix):
        """Check if text starts with the given prefix."""
        return text.startswith(prefix)

    def ends_with_suffix(self, text, suffix):
        """Check if text ends with the given suffix."""
        return text.endswith(suffix)