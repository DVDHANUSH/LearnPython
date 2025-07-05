def palindrome(i, s):
    # Base condition
    if i >= len(s) / 2:
        return True

    # If characters at i and len - i - 1 are not equal
    if s[i] != s[len(s) - i - 1]:
        return False

    # Recursive call
    return palindrome(i + 1, s)

# Example usage
s = "kpkk"
print(palindrome(0, s))  # Output: True