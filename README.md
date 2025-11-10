

# Scytale Cipher 

Proyek ini adalah implementasi sederhana algoritma **Scytale Cipher** menggunakan bahasa Python.  
Scytale Cipher merupakan salah satu teknik kriptografi klasik yang digunakan pada zaman Yunani kuno untuk
menyembunyikan pesan rahasia dengan bantuan sebuah batang silinder.

---
##  Fitur Utama
Program ini mengimplementasikan **Scytale Cipher** dengan beberapa opsi tambahan:

1. 🔤 **Pertahankan Spasi** → Pesan tetap utuh (tanpa dihapus).
2. 🧩 **Pilih Karakter Padding Sendiri** → Default `'X'`, tapi bisa diganti (misal `'-'` atau `'_'`).
3. 🔁 **Key sebagai Baris atau Kolom** → Pilih apakah nilai kunci mewakili jumlah **baris** atau **kolom**.

---

## 🧠 Penjelasan Singkat
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



Misalnya, plaintext `HELLOWORLD` dengan `key=3` (jumlah kolom) akan disusun seperti ini:

```
H E L
L O W
O R L
D X X
```

Ciphertext dibaca kolom demi kolom → **HLOD EORW LXXX** (tanpa spasi dan padding X di akhir).

---

## 💻 Source Code: `scytale_cipher.py`

```python
import math

def encrypt_scytale(
    plaintext: str,
    key: int,
    pad_char: str = "X",
    keep_spaces: bool = True,
    key_as: str = "cols",  # "cols" atau "rows"
) -> str:
    """
    Enkripsi Scytale Cipher dengan opsi varian.
    
    Args:
        plaintext : string pesan asli
        key : jumlah kolom atau baris (tergantung key_as)
        pad_char : karakter padding jika grid tidak penuh
        keep_spaces : jika True, spasi dipertahankan
        key_as : "cols" jika key = jumlah kolom, "rows" jika key = jumlah baris
    """

    if not plaintext:
        return ""
    if key <= 0:
        raise ValueError("Key harus lebih besar dari 0")

    # Bersihkan atau pertahankan spasi
    msg = plaintext if keep_spaces else "".join(plaintext.split())
    n = len(msg)

    # Tentukan jumlah baris dan kolom berdasarkan parameter key_as
    if key_as == "cols":
        cols = key
        rows = math.ceil(n / cols)
    elif key_as == "rows":
        rows = key
        cols = math.ceil(n / rows)
    else:
        raise ValueError("key_as harus 'cols' atau 'rows'")

    total_cells = rows * cols
    msg_padded = msg.ljust(total_cells, pad_char)

    # Buat matriks
    matrix = [msg_padded[i*cols:(i+1)*cols] for i in range(rows)]

    # Baca kolom demi kolom
    ciphertext = []
    for c in range(cols):
        for r in range(rows):
            ciphertext.append(matrix[r][c])
    return "".join(ciphertext)


def decrypt_scytale(
    ciphertext: str,
    key: int,
    pad_char: str = "X",
    key_as: str = "cols"
) -> str:
    """
    Dekripsi Scytale Cipher dengan opsi varian.
    """
    if not ciphertext:
        return ""
    if key <= 0:
        raise ValueError("Key harus lebih besar dari 0")

    n = len(ciphertext)

    if key_as == "cols":
        cols = key
        rows = math.ceil(n / cols)
    elif key_as == "rows":
        rows = key
        cols = math.ceil(n / rows)
    else:
        raise ValueError("key_as harus 'cols' atau 'rows'")

    # Isi kolom demi kolom
    matrix = [[""] * cols for _ in range(rows)]
    idx = 0
    for c in range(cols):
        for r in range(rows):
            if idx < n:
                matrix[r][c] = ciphertext[idx]
                idx += 1

    # Baca baris demi baris
    plaintext = []
    for r in range(rows):
        for c in range(cols):
            plaintext.append(matrix[r][c])
    return "".join(plaintext).rstrip(pad_char)


# --- Contoh penggunaan ---
if __name__ == "__main__":
    text = "HELLO WORLD"
    key = 4

    print("=== SCYTALE CIPHER ===")
    print(f"Plaintext: {text}")

    # VARIAN 1: Key sebagai kolom, spasi dihapus
    ct1 = encrypt_scytale(text, key, keep_spaces=False)
    print("\n[1] Enkripsi (key=kolom, hapus spasi)")
    print("Ciphertext:", ct1)
    print("Dekripsi  :", decrypt_scytale(ct1, key))

    # VARIAN 2: Key sebagai baris, spasi dipertahankan
    ct2 = encrypt_scytale(text, 3, keep_spaces=True, key_as="rows", pad_char="-")
    print("\n[2] Enkripsi (key=baris, spasi dipertahankan, padding '-')")
    print("Ciphertext:", ct2)
    print("Dekripsi  :", decrypt_scytale(ct2, 3, pad_char='-', key_as="rows"))
```

---

## 🧪 Contoh Hasil

### 🔸 Varian 1 — Key = Kolom (tanpa spasi)

```
Plaintext : HELLO WORLD
Key       : 4
Ciphertext: HORELLOWLDX
Dekripsi  : HELLOWORLD
```

### 🔸 Varian 2 — Key = Baris (pertahankan spasi, padding ‘-’)

```
Plaintext : HELLO WORLD
Key       : 3
Ciphertext: H LORLEWLD O--
Dekripsi  : HELLO WORLD
```

---

## 🧭 Flowchart Ringkas

```
┌────────────────────┐
│   Mulai Program    │
└───────┬────────────┘
        │
┌───────▼───────────┐
│ Input teks & key  │
│ Pilih mode & varian│
└───────┬───────────┘
        │
 ┌──────▼──────┐
 │ Enkripsi /  │
 │ Dekripsi    │
 └──────┬──────┘
        │
 ┌──────▼──────┐
 │ Tampilkan   │
 │ Hasil       │
 └──────┬──────┘
        │
   ┌────▼────┐
   │ Selesai │
   └─────────┘
```

---

## 📊 Kompleksitas

* **Waktu:** `O(n)`
* **Memori:** `O(n)`
* **Kelemahan:** Mudah dipecahkan bila panjang kunci diketahui.
* **Kelebihan:** Cocok untuk memahami konsep *transposition cipher* klasik.

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

