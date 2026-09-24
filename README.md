# DecodeLabs-internships

# Basic Encryption & Decryption (Project 2)

 **DecodeLabs Industrial Training Kit**|**Batch 2026 Track:** Cyber Security | **Goal:** Data Confidentiality in transit

**Formula:**
- Encrypt: `Eₙ(x) = (x + n) % 26` → `chr((ord(c)-base + shift) % 26 + base)`
- Decrypt: `Dₙ(x) = (x - n) % 26`
- Preserves case, leaves spaces / digits / punctuation unchanged.

**Run:**
```bash
python3 Project_2_Basic_Encryption_Decryption.py
```

Menu:
```
1. Encrypt (Caesar)  2. Decrypt (Caesar)  3. Encrypt+Decrypt demo
4. Brute-force demo  5. Vigenère (bonus)  6. Exit
```

---

## Feature 1 — Caesar Encrypt (user text + custom shift key)

**Test:** Choose `1` → Plaintext: `Hello World` → Shift: `3`
**Expected:**
```
[INPUT]  Plaintext : Hello World
[KEY]    Shift     : 3
[OUTPUT] Ciphertext: Khoor Zruog
```

![Feature 1 - Encrypt](screenshots/feature1-encrypt.png)
> Save your terminal screenshot as `screenshots/feature1-encrypt.png` to show it here.

## Feature 2 — Caesar Decrypt (reverse shift)

**Test:** Choose `2` → Ciphertext: `Khoor Zruog` → Shift: `3`
**Expected:**
```
[INPUT]  Ciphertext: Khoor Zruog
[KEY]    Shift     : 3
[OUTPUT] Plaintext : Hello World
```

![Feature 2 - Decrypt](screenshots/feature2-decrypt.png)

## Feature 3 — Encrypt + Decrypt Demo (roundtrip validation)

**Test:** Choose `3` → Text: `DecodeLabs 2026!` → Shift: `7`
**Expected:**
```
Original  : DecodeLabs 2026!
Encrypted (shift=7): KljvklShiz 2026!
Decrypted : DecodeLabs 2026!
Validated: OK - roundtrip success
```

![Feature 3 - Roundtrip](screenshots/feature3-roundtrip.png)

## Feature 4 — Brute-Force Demo (vulnerability proof)

**Test:** Choose `4` → Ciphertext: `Khoor`
**Expected (excerpt):**
```
shift  1: Jgnnq
shift  2: Ifmmp
shift  3: Hello
...
25 keys tried = lockbox, not a vault (tiny key space + frequency analysis)
```

![Feature 4 - Brute Force](screenshots/feature4-bruteforce.png)

## Feature 5 — Vigenère Cipher (bonus, per Conclusion slide)

**Test:** Choose `5` → Text: `ATTACKATDAWN` → Keyword: `LEMON`
**Expected:**
```
Original  : ATTACKATDAWN
Encrypted (Vigenère key=LEMON): LXFOPVEFRNHR
Decrypted : ATTACKATDAWN
Validated: OK
```

![Feature 5 - Vigenere](screenshots/feature5-vigenere.png)

---

## Quick auto-test (no typing)
```bash
python3 -c "import Project_2_Basic_Encryption_Decryption as c; print(c.caesar_encrypt('Hello World',3)); print(c.caesar_decrypt('Khoor Zruog',3)); print(c.vigenere_encrypt('ATTACKATDAWN','LEMON'))"
# Khoor Zruog
# Hello World
# LXFOPVEFRNHR
```

## For LinkedIn
1. Run each feature above, take 5 screenshots with Snipping Tool / Screenshot app.
2. Save them with exact names in `screenshots/` folder so this README displays them.
3. Post with caption: `Project 2 Done @ DecodeLabs – Caesar + Vigenère in Python #CyberSecurity #Python #DecodeLabs Batch 2026` + attach Feature 3 screenshot as cover.

**Files:**
- `Project_2_Basic_Encryption_Decryption.py` — main submission (Project 2 labelled)
- `screenshots/feature1-encrypt.png` … `feature5-vigenere.png` — your 5 proofs
