<div align="center">

# ?? Spotify Create Account

**Auto-create multiple Spotify accounts from a list. Batch. Headless-friendly. No manual input.**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?labelColor=black&style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-undetected--chromedriver-green?labelColor=black&style=flat-square&logo=selenium&logoColor=white)](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
[![License](https://img.shields.io/badge/license-MIT-white?labelColor=black&style=flat-square)](./LICENSE)

</div>

---

## What it does

```
You:    buat accounts.txt berisi email|username
Script: [CHECK]    validasi email belum terdaftar
        [FILL]     isi form signup otomatis
        [SUBMIT]   password, nama, tanggal lahir, gender
        [SAVE]     simpan akun berhasil ke result.txt
You:    cek result.txt
```

Satu script, banyak akun. Cukup siapkan listnya.

---

## Requirements

- Python 3.8+
- Google Chrome (versi terbaru)
- `chromedriver.exe` (disertakan dalam repo, sesuaikan versi dengan Chrome kamu)

---

## Installation

```bash
# Clone repo
git clone https://github.com/prawira-rexsa/spotify-create-acc.git
cd spotify-create-acc

# Install dependencies
pip install undetected-chromedriver selenium termcolor
```

---

## Usage

### 1. Siapkan `accounts.txt`

Format setiap baris:

```
email@example.com|Username
email2@example.com|Username2
```

### 2. Jalankan script

```bash
python main.py
```

### 3. Cek hasil

Akun yang berhasil dibuat tersimpan di `result.txt`.

---

## File Structure

```
spotify-create-acc/
+-- main.py          # Script utama
+-- accounts.txt     # Daftar email|username (buat sendiri)
+-- chromedriver.exe # ChromeDriver binary
+-- result.txt       # Output akun berhasil (auto-generated)
```

---

## How It Works

| Step | Aksi |
| :--- | :--- |
| **1. Read** | Baca `accounts.txt` line by line |
| **2. Check** | Deteksi jika email sudah terdaftar, skip otomatis |
| **3. Fill** | Isi form: email ? password ? nama ? DOB ? gender |
| **4. Submit** | Klik tombol daftar & verifikasi URL sukses |
| **5. Save** | Tulis email ke `result.txt` jika berhasil |

---

## Notes

- Script menggunakan **undetected-chromedriver** untuk menghindari deteksi bot
- Setiap akun dibuat di tab Chrome terpisah (incognito mode)
- Email yang sudah terdaftar akan di-skip dan lanjut ke email berikutnya
- Pastikan versi `chromedriver.exe` sesuai dengan versi Google Chrome yang terinstall

---

## Disclaimer

> Repo ini dibuat untuk keperluan edukasi dan riset.
> Penggunaan tool ini untuk melanggar Terms of Service Spotify sepenuhnya menjadi tanggung jawab pengguna.

---

<div align="center">
Made by <a href="https://github.com/prawira-rexsa">prawira-rexsa</a>
</div>
