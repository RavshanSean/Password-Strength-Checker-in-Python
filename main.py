import re
import string


def check_password_strength(password: str) -> tuple[str, list[str], int]:
    """
    Returns:
        strength label, feedback list, score (0-5)
    """
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("12+ characters would make it stronger.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"\d", password) or any(ch in string.punctuation for ch in password):
        score += 1
    else:
        feedback.append("Add at least one number or symbol.")

    has_digit = bool(re.search(r"\d", password))
    has_symbol = any(ch in string.punctuation for ch in password)
    if has_digit and has_symbol and len(password) >= 12:
        feedback.append("Nice: your password has good variety.")

    weak_patterns = ["123", "password", "qwerty", "admin", "0000"]
    if any(pattern in password.lower() for pattern in weak_patterns):
        feedback.append("Avoid common patterns like '123' or 'password'.")
        score = max(score - 1, 0)

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback, score


def main() -> None:
    print("=== Password Strength Checker ===")
    password = input("Enter a password: ")

    strength, feedback, score = check_password_strength(password)

    print(f"\nStrength: {strength}")
    print(f"Score: {score}/5")

    if feedback:
        print("\nFeedback:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Your password looks great.")


if __name__ == "__main__":
    main()
