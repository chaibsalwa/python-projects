"""
Secure Password Generator
Author: Salwa Chaib
"""

import random
import string

def generate_password(length=12, use_upper=True, use_numbers=True, use_symbols=True):
    """Generate a secure random password"""
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_strength(password):
    """Check password strength"""
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()" for c in password): score += 1
    
    levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return levels[min(score, 5)]

if __name__ == "__main__":
    print("🔐 Secure Password Generator\n")
    for length in [8, 12, 16]:
        pwd = generate_password(length)
        strength = check_strength(pwd)
        print(f"{length} chars: {pwd} -> {strength}")
