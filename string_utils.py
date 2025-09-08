def capitalize_words(text):
    """Capitalize the first letter of each word in the text."""
    return ' '.join(word.capitalize() for word in text.split())


def reverse_string(text):
    """Return the reversed version of the input string."""
    return text[::-1]


def count_vowels(text):
    """Count the number of vowels in the text."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)


def count_consonants(text):
    """Count the number of consonants in the text."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char.isalpha() and char not in vowels)


def is_palindrome(text):
    """Check if the text is a palindrome (ignoring case and spaces)."""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def remove_whitespace(text):
    """Remove all whitespace from the text."""
    return ''.join(text.split())


def word_count(text):
    """Count the number of words in the text."""
    return len(text.split())


def replace_substring(text, old, new):
    """Replace all occurrences of old substring with new substring."""
    return text.replace(old, new)


def starts_with_prefix(text, prefix):
    """Check if text starts with the given prefix."""
    return text.startswith(prefix)


def ends_with_suffix(text, suffix):
    """Check if text ends with the given suffix."""
    return text.endswith(suffix)