# DecodeLabs-internships

# Basic Encryption & Decryption (Project 2)

 **DecodeLabs Industrial Training Kit**|**Batch 2026 Track:** Cyber Security | **Goal:** Implement a simple encryption and decryption technique.



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

**Test:** Choose `1` → Plaintext: `My name is khaleed` → Shift: `2`
**Expected:**
```
[INPUT]  Plaintext : My name is khaleed
[KEY]    Shift     : 2
[OUTPUT] Ciphertext: Oa  pcog ku mjcnggf
```

![Feature 1 - Encrypt](https://github.com/Walcott-iam/TASK-2-Oresanya-Khaleed-Walcott/blob/main/encryption.png)

## Feature 2 — Caesar Decrypt (reverse shift)

**Test:** Choose `` → Ciphertext: `Oa  pcog ku mjcnggf` → Shift: `2`
**Expected:**
```
[INPUT]  Ciphertext: Oa  pcog ku mjcnggf
[KEY]    Shift     : 2
[OUTPUT] Plaintext : My name is khaleed
```

![Feature 2 - Decrypt](https://github.com/Walcott-iam/TASK-2-Oresanya-Khaleed-Walcott/blob/main/decryption.png)

## Feature 3 — Encrypt + Decrypt Demo (roundtrip validation)

**Test:** Choose `3` → Text: `I love my parent` → Shift: `2`
**Expected:**
```
Original  : I love my parent
Encrypted (shift=2): K nqxg oa rctgpv
Decrypted : I love my parent
Validated: OK - roundtrip success
```

![Feature 3 - Roundtrip](https://github.com/Walcott-iam/TASK-2-Oresanya-Khaleed-Walcott/blob/main/encrypt-decrypt.png)

## Feature 4 — Brute-Force Demo (vulnerability proof)

**Test:** Choose `4` → Ciphertext: `I love my parent`
**Expected :**
```
shift  1: J mpwf nz qbsfou
** shift  2: I love my parent **
shift  3: H knud lx ozqdms
...
25 keys tried = lockbox, not a vault (tiny key space + frequency analysis)
```

![Feature 4 - Brute Force](https://github.com/Walcott-iam/TASK-2-Oresanya-Khaleed-Walcott/blob/main/brute%20force%20demo.png)

## Feature 5 — Vigenère Cipher (bonus, per Conclusion slide)

**Test:** Choose `5` → Text: `ATTACKATDAWN` → Keyword: `LEMON`
**Expected:**
```
Original  : ATTACKATDAWN
Encrypted (Vigenère key=LEMON): LXFOPVEFRNHR
Decrypted : ATTACKATDAWN
Validated: OK
```

![Feature 5 - Vigenere](https://github.com/Walcott-iam/TASK-2-Oresanya-Khaleed-Walcott/blob/main/Vignere.png)


# key skill demonstrated

**1. Encryption Concepts (Symmetric Crypto)**
Implemented `Eₙ(x)=(x+n)%26` and `Dₙ(x)=(x-n)%26` – same key locks and unlocks.

**2. Logic Building / IPO Model**
Input (plaintext + key) → Process (`ord()` → `-base` → `+key` → `%26` → `+base` → `chr()`) → Output (ciphertext).

**3. Data Protection Basics**
Case preserved, spaces/punctuation/digits untouched, roundtrip validated: `decrypt(encrypt(x))==x`. Bonus Vigenère with keyword (`ATTACKATDAWN`+`LEMON`=`LXFOPVEFRNHR`).

**4. Vulnerability Analysis**
Proved Caesar is lockbox not vault via brute-force (25 keys) + pattern preservation – foundation for understanding AES.
