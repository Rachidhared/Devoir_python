import re

def clean_string(s: str) -> str:
    """Nettoie la chaîne en supprimant les caractères non alphanumériques et convertit en minuscules."""
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

def is_palindrome_while(input_string: str) -> bool:
    """Vérifie si une chaîne est un palindrome en utilisant une boucle while."""
    cleaned = clean_string(input_string)
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

def is_palindrome_for(input_string: str) -> bool:
    """Vérifie si une chaîne est un palindrome en utilisant une boucle for."""
    cleaned = clean_string(input_string)
    length = len(cleaned)
    
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - 1 - i]:
            return False
    
    return True

def test_palindromes():
    test_cases = [
        "A man, a plan, a canal, Panama",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "Hello, World!",
        "Able was I ere I saw Elba"
    ]
    
    for test in test_cases:
        print(f"Testing: {test}")
        print(f"Using while loop: {is_palindrome_while(test)}")
        print(f"Using for loop: {is_palindrome_for(test)}")
        print()

if __name__ == "__main__":
    test_palindromes()
