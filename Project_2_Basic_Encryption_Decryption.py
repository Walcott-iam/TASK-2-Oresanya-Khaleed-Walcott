"""
Project 2: Basic Encryption & Decryption - DecodeLabs (Batch 2026)
Cybersecurity Track - Data Confidentiality via Caesar Cipher

IPO Model:
  INPUT   : Plaintext (raw data) + Shift Key (n)
  PROCESS : En(x) = (x + n) % 26 using ord() / chr()
  OUTPUT  : Ciphertext (secured)

  Decryption reverses it: Dn(x) = (x - n) % 26
"""

def _shift_char(char: str, shift: int) -> str:
    """Shift a single alphabetical character, preserve case. Non-letters unchanged."""
    if 'A' <= char <= 'Z':
        base = ord('A')  # 65
        # E_n(x) = (x + n) % 26
        return chr((ord(char) - base + shift) % 26 + base)
    if 'a' <= char <= 'z':
        base = ord('a')  # 97
        return chr((ord(char) - base + shift) % 26 + base)
    # Edge cases: spaces, punctuation, digits -> unchanged
    return char


def caesar_encrypt(plaintext: str, shift: int) -> str:
    """Encrypt plaintext with Caesar shift key."""
    if not isinstance(plaintext, str):
        raise TypeError("plaintext must be a string")
    shift = int(shift) % 26
    return "".join(_shift_char(c, shift) for c in plaintext)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt ciphertext with same shift key. Dn(x) = (x - n) % 26."""
    if not isinstance(ciphertext, str):
        raise TypeError("ciphertext must be a string")
    shift = int(shift) % 26
    return "".join(_shift_char(c, -shift) for c in ciphertext)


def brute_force(ciphertext: str) -> dict:
    """Try all 25 keys — demonstrates why Caesar is a lockbox, not a vault."""
    return {shift: caesar_decrypt(ciphertext, shift) for shift in range(1, 26)}


def vigenere_encrypt(plaintext: str, keyword: str) -> str:
    """Vigenère cipher (bonus): each letter shifted by keyword letter (A=0..Z=25)."""
    if not keyword or not keyword.isalpha():
        raise ValueError("keyword must be non-empty alphabetic string")
    keyword = keyword.upper()
    out, ki = [], 0
    for ch in plaintext:
        if 'A' <= ch <= 'Z':
            shift = ord(keyword[ki % len(keyword)]) - ord('A')
            out.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
            ki += 1
        elif 'a' <= ch <= 'z':
            shift = ord(keyword[ki % len(keyword)]) - ord('A')
            out.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
            ki += 1
        else:
            out.append(ch)
    return "".join(out)


def vigenere_decrypt(ciphertext: str, keyword: str) -> str:
    """Reverse Vigenère with same keyword."""
    if not keyword or not keyword.isalpha():
        raise ValueError("keyword must be non-empty alphabetic string")
    keyword = keyword.upper()
    out, ki = [], 0
    for ch in ciphertext:
        if 'A' <= ch <= 'Z':
            shift = ord(keyword[ki % len(keyword)]) - ord('A')
            out.append(chr((ord(ch) - ord('A') - shift) % 26 + ord('A')))
            ki += 1
        elif 'a' <= ch <= 'z':
            shift = ord(keyword[ki % len(keyword)]) - ord('A')
            out.append(chr((ord(ch) - ord('a') - shift) % 26 + ord('a')))
            ki += 1
        else:
            out.append(ch)
    return "".join(out)


def main():
    print("=" * 55)
    print(" Project 2: Basic Encryption & Decryption (Caesar Cipher)")
    print(" DecodeLabs | Data Confidentiality in Transit")
    print("=" * 55)

    while True:
        print("\n1. Encrypt (Caesar)  2. Decrypt (Caesar)  3. Encrypt+Decrypt demo")
        print("4. Brute-force demo  5. Vigenère (bonus)  6. Exit")
        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            text = input("Enter plaintext: ")
            try:
                shift = int(input("Enter shift key (e.g. 3): "))
            except ValueError:
                print("Shift must be an integer.")
                continue
            cipher = caesar_encrypt(text, shift)
            print(f"\n[INPUT]  Plaintext : {text}")
            print(f"[KEY]    Shift     : {shift % 26}")
            print(f"[OUTPUT] Ciphertext: {cipher}")

        elif choice == "2":
            text = input("Enter ciphertext: ")
            try:
                shift = int(input("Enter shift key: "))
            except ValueError:
                print("Shift must be an integer.")
                continue
            plain = caesar_decrypt(text, shift)
            print(f"\n[INPUT]  Ciphertext: {text}")
            print(f"[KEY]    Shift     : {shift % 26}")
            print(f"[OUTPUT] Plaintext : {plain}")

        elif choice == "3":
            text = input("Enter text to encrypt: ")
            try:
                shift = int(input("Enter shift key (e.g. 3): "))
            except ValueError:
                print("Shift must be an integer.")
                continue
            encrypted = caesar_encrypt(text, shift)
            decrypted = caesar_decrypt(encrypted, shift)
            print(f"\nOriginal  : {text}")
            print(f"Encrypted (shift={shift % 26}): {encrypted}")
            print(f"Decrypted : {decrypted}")
            print("Validated:", "OK - roundtrip success" if decrypted == text else "FAIL")

        elif choice == "4":
            text = input("Enter ciphertext to brute-force: ")
            results = brute_force(text)
            print("\nAll 25 possible keys:")
            for s, p in results.items():
                print(f"  shift {s:2d}: {p}")

        elif choice == "5":
            text = input("Enter text: ")
            key = input("Enter keyword (letters only, e.g. LABS): ").strip()
            try:
                enc = vigenere_encrypt(text, key)
                dec = vigenere_decrypt(enc, key)
            except ValueError as e:
                print(e)
                continue
            print(f"\nOriginal  : {text}")
            print(f"Encrypted (Vigenère key={key.upper()}): {enc}")
            print(f"Decrypted : {dec}")
            print("Validated:", "OK" if dec == text else "FAIL")

        elif choice == "6":
            print("Exiting. Remember: master the shift, master the shield.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
