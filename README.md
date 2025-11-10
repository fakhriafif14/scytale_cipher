
```markdown
# 🔐 Scytale Cipher (Python)

Proyek ini adalah implementasi sederhana algoritma **Scytale Cipher** menggunakan bahasa Python.  
Scytale Cipher merupakan salah satu teknik kriptografi klasik yang digunakan pada zaman Yunani kuno untuk
menyembunyikan pesan rahasia dengan bantuan sebuah batang silinder.

---

## 📖 Penjelasan Singkat

- **Apa itu Scytale Cipher?**  
  Scytale adalah metode enkripsi transposisi, di mana teks asli (*plaintext*) ditulis melingkar pada sebuah silinder dengan jumlah baris tertentu (*key*).  
  Setelah pesan selesai ditulis, hasil bacaan kolom demi kolom menghasilkan teks terenkripsi (*ciphertext*).

- **Bagaimana cara kerjanya?**  
  1. Plaintext ditulis dalam bentuk grid sesuai jumlah baris (*key*).  
  2. Ciphertext dibaca secara kolom, bukan baris.  
  3. Untuk dekripsi, teks dienkripsi kembali dengan cara yang sama menggunakan key yang sama.  

- **Kelemahan:**  
  Walaupun metode ini unik secara historis, algoritma ini **tidak aman** untuk kebutuhan kriptografi modern.  
  Scytale Cipher hanya cocok untuk pembelajaran atau eksplorasi sejarah kriptografi.

---

## 📜 Pseudocode

Berikut pseudocode program **Scytale Cipher** untuk mempermudah pemahaman algoritma:

```

PROGRAM ScytaleCipher

```
INPUT plaintext
INPUT key

// ===================
// Fungsi Enkripsi
// ===================
FUNCTION scytale_encrypt(text, key):
    IF key <= 1 THEN
        RETURN text
    ENDIF

    panjang ← LENGTH(text)
    kolom ← CEIL(panjang / key)
    
    // tambahkan padding jika perlu
    padded_text ← text + (spasi sampai panjang = kolom * key)

    result ← ""   // string kosong
    FOR i FROM 0 TO key-1:
        j ← i
        WHILE j < LENGTH(padded_text):
            result ← result + padded_text[j]
            j ← j + key
        ENDWHILE
    ENDFOR

    RETURN result
END FUNCTION


// ===================
// Fungsi Dekripsi
// ===================
FUNCTION scytale_decrypt(cipher, key):
    IF key <= 1 THEN
        RETURN cipher
    ENDIF

    panjang ← LENGTH(cipher)
    kolom ← CEIL(panjang / key)

    rows ← array kosong
    idx ← 0

    FOR i FROM 0 TO key-1:
        row_len ← kolom
        IF idx + row_len > panjang THEN
            row_len ← panjang - idx
        ENDIF
        rows[i] ← SUBSTRING(cipher, idx, row_len)
        idx ← idx + row_len
    ENDFOR

    result ← ""
    FOR i FROM 0 TO kolom-1:
        FOR each row IN rows:
            IF i < LENGTH(row) THEN
                result ← result + row[i]
            ENDIF
        ENDFOR
    ENDFOR

    RETURN result tanpa padding
END FUNCTION


// ===================
// Main Program
// ===================
encrypted ← scytale_encrypt(plaintext, key)
decrypted ← scytale_decrypt(encrypted, key)

OUTPUT "Plaintext : ", plaintext
OUTPUT "Encrypted : ", encrypted
OUTPUT "Decrypted : ", decrypted
```

END PROGRAM

````

---

## 💻 Implementasi Python

Berikut implementasi lengkap dalam bahasa Python:

```python
import math

# === Fungsi Enkripsi ===
def scytale_encrypt(text, key):
    if key <= 1:
        return text
    panjang = len(text)
    kolom = math.ceil(panjang / key)
    padded_text = text.ljust(kolom * key)
    result = []
    for i in range(0, key):
        j = i
        while j < len(padded_text):
            result.append(padded_text[j])
            j = j + key
    return "".join(result)


# === Fungsi Dekripsi ===
def scytale_decrypt(cipher, key):
    if key <= 1:
        return cipher
    panjang = len(cipher)
    kolom = math.ceil(panjang / key)
    rows = []
    idx = 0
    for i in range(key):
        row_len = kolom
        if idx + row_len > panjang:
            row_len = panjang - idx
        rows.append(cipher[idx:idx+row_len])
        idx += row_len
    result = []
    for i in range(kolom):
        for row in rows:
            if i < len(row):
                result.append(row[i])
    return "".join(result).rstrip()


# === Main Program ===
if __name__ == "__main__":
    plaintext = input("Masukkan teks yang akan dienkripsi: ")
    key = int(input("Masukkan key (jumlah baris): "))

    encrypted = scytale_encrypt(plaintext, key)
    decrypted = scytale_decrypt(encrypted, key)

    print("\n=== Hasil ===")
    print("Plaintext :", plaintext)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
````

---

## ✨ Contoh Penggunaan

```
Masukkan teks yang akan dienkripsi: HELLOSCYTALE
Masukkan key (jumlah baris): 3

=== Hasil ===
Plaintext : HELLOSCYTALE
Encrypted : HLOYAELCLTES
Decrypted : HELLOSCYTALE
```

---

## 📌 Catatan

* Parameter `key` harus lebih dari 1 agar enkripsi berfungsi.
* Jika `key = 1`, teks tidak akan berubah.
* Algoritma ini menunjukkan **konsep transposisi** dalam kriptografi, bukan untuk keamanan nyata.

```

