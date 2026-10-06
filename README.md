# PonyTownBot

**PonyTownBot** adalah pengembangan lanjutan dari proyek sebelumnya, yaitu **PTBot** dan **PTBot_V2**, yang dikembangkan oleh **RandSfk**.

Berbeda dari versi sebelumnya yang lebih ditujukan untuk pengguna yang memahami konfigurasi dan scripting, **PonyTownBot kini hadir dalam bentuk aplikasi Android (APK)**. Dengan demikian, pengguna dapat menjalankan dan mengatur bot dengan lebih mudah tanpa harus memahami pemrograman atau mengedit source code secara manual.

---

# Main Features

## AI Integration

PonyTownBot memiliki integrasi **AI** yang memungkinkan bot memberikan respons secara lebih natural dan dinamis ketika berinteraksi dengan pemain lain.

Pengguna juga dapat mengatur karakter AI melalui **AI Setting**, sehingga respons bot dapat disesuaikan dengan karakter yang diinginkan.

---

## Chat Type Support

Bot mendukung beberapa jenis chat yang tersedia di PonyTown:

* **Whisper**
* **Think**
* **Say**

Pengguna dapat menyesuaikan jenis komunikasi yang digunakan bot sesuai kebutuhan.

---

## Custom Owner & Bot Name

Nama pemilik dan nama bot dapat dikustomisasi melalui pengaturan.

Contoh:

```text
Owner: Randy
Bot Name: RandSfk Bot
```

Informasi tersebut juga dapat digunakan oleh sistem AI dan command bot.

---

## Anti-AFK

Fitur **Anti-AFK** membantu menjaga bot tetap aktif ketika tidak ada aktivitas dari pengguna.

Dengan fitur ini, bot dapat terus berjalan tanpa harus terus-menerus dikontrol secara manual.

---

## AI Setting

PonyTownBot menyediakan pengaturan AI untuk menentukan identitas, kepribadian, dan latar belakang karakter.

Pengguna dapat mengatur informasi seperti:

```text
Name
Gender
Sifat
Lore
Gaya bicara
```

Contoh:

```json
{
  "name": "Lil Uzi Vert",
  "gender": "Male",
  "sifat": "Chill, Asik, Rapper",
  "lore": "Rapper asal Amerika Serikat yang bermain PonyTown"
}
```

Dengan pengaturan tersebut, AI dapat memberikan respons yang lebih sesuai dengan karakter yang telah dibuat.

---

# Commands

PonyTownBot menggunakan sistem **custom commands** yang dapat dikembangkan menggunakan **RandEngine**.

Command dapat digunakan untuk membuat:

* Menu bot
* Auto response
* Random response
* Informasi bot
* Sistem interaksi
* Response berbasis kondisi
* Dan berbagai kebutuhan lainnya

Command tidak harus dibuat ulang dari awal setiap kali berpindah perangkat.

---

## Export & Import Commands

PonyTownBot mendukung **Export dan Import Commands**.

Fitur ini digunakan untuk menyimpan kumpulan command sehingga dapat dipindahkan atau digunakan kembali dengan mudah.

### Export Commands

Gunakan fitur **Export** untuk menyimpan command yang telah dibuat.

File hasil export dapat digunakan sebagai backup atau dipindahkan ke perangkat lain.

```text
Commands
   ↓
Export
   ↓
File
```

### Import Commands

File command yang sebelumnya telah diexport dapat dimasukkan kembali menggunakan fitur **Import**.

```text
File Commands
      ↓
Import
      ↓
Commands
```

Fitur ini berguna untuk:

* Backup command
* Memindahkan command ke perangkat lain
* Berbagi template command
* Menyimpan beberapa konfigurasi command
* Mengembalikan command setelah reset aplikasi

---

# OC / Original Character

PonyTownBot juga mendukung pengelolaan **OC (Original Character)** atau **skin/character PonyTown**.

Fitur ini memungkinkan pengguna menyimpan konfigurasi karakter sehingga karakter dapat digunakan kembali tanpa harus mengatur ulang secara manual.

Pengguna dapat menyimpan beberapa karakter berbeda sebagai preset.

```text
Character 1
Character 2
Character 3
Character 4
```

---

## Export & Import OC

Konfigurasi OC atau karakter juga dapat **diekspor dan diimpor**.

### Export OC

Gunakan **Export** untuk menyimpan data karakter.

```text
OC / Character
      ↓
Export
      ↓
File
```

File tersebut dapat dijadikan backup atau dipindahkan ke perangkat lain.

### Import OC

Karakter yang sebelumnya telah disimpan dapat dimasukkan kembali menggunakan **Import**.

```text
File Character
      ↓
Import
      ↓
OC / Character
```

Dengan demikian pengguna dapat menyimpan banyak karakter dan memindahkannya tanpa harus membuat ulang satu per satu.

---

# Music Player

PonyTownBot dilengkapi dengan **Music Player** untuk memutar musik langsung melalui aplikasi.

Music Player dapat digunakan untuk menyimpan dan memutar koleksi musik yang ingin digunakan saat menjalankan bot.

Contoh fungsi yang tersedia:

```text
Play
Pause
Next
Previous
Volume
Playlist
```

Music Player berjalan sebagai fitur terpisah dari sistem command sehingga pengguna dapat tetap menggunakan fungsi bot sambil memutar musik.

---

# RandEngine Support

PonyTownBot menggunakan **RandEngine**, yaitu mesin scripting dan command khusus yang dikembangkan oleh **RandSfk**.

RandEngine digunakan untuk membuat dan mengatur sistem command secara fleksibel, termasuk:

* Variable
* Conditional
* Random response
* Text formatting
* JSON
* HTTP request
* Dynamic response
* Command menu
* Custom bot response

Contoh sederhana:

```text
$var name = "Randy"

$if name == "Randy" {
    $print "Hello Randy!"
}
```

Dokumentasi lengkap RandEngine:

https://randsfk.vercel.app/documentation

---

# How To Use

## 1. Download APK Terbaru

Unduh **PonyTownBot APK** melalui channel resmi WhatsApp:

https://whatsapp.com/channel/0029VbAVW52AO7RFpvpeCR3l

Disarankan menggunakan versi APK terbaru untuk mendapatkan fitur dan perbaikan terbaru.

---

## 2. Install APK

Setelah APK selesai diunduh:

1. Buka file APK.
2. Izinkan instalasi dari sumber yang diperlukan apabila Android meminta izin.
3. Selesaikan proses instalasi.
4. Buka **PonyTownBot**.

---

# 3. Masukkan API Key

Pada pertama kali menjalankan aplikasi, PonyTownBot akan meminta **API Key**.

API Key diperlukan agar aplikasi dapat menggunakan layanan yang terhubung dengan akun pengguna.

## Cara mendapatkan API Key

### Step 1 — Buka Dashboard

Buka:

https://randsfk.vercel.app/dashboard

Apabila belum memiliki akun, lakukan registrasi terlebih dahulu.

---

### Step 2 — Registrasi / Login

Masukkan informasi akun sesuai form yang tersedia.

Apabila OTP melalui email tidak masuk ke inbox, periksa folder:

```text
Inbox
Spam
Junk
Promotions
```

---

### Step 3 — Masuk ke Dashboard

Setelah berhasil login, kamu akan diarahkan ke **Dashboard**.

Apabila login melalui aplikasi mengalami masalah, gunakan browser:

**Login:**

https://randsfk.vercel.app/login

**Dashboard:**

https://randsfk.vercel.app/dashboard

---

### Step 4 — Salin API Key

Di bagian atas Dashboard, cari:

```text
Your Apikey
```

Salin API Key tersebut.

**Jangan membagikan API Key kepada orang lain**, karena API Key merupakan kredensial yang terkait dengan akun pengguna.

---

### Step 5 — Masukkan API Key

Kembali ke aplikasi **PonyTownBot**.

Masukkan API Key ke field:

```text
APIKey
```

Kemudian tekan:

```text
Submit
```

Jika API Key valid, aplikasi dapat melanjutkan ke tahap penggunaan bot.

---

# Export & Import

PonyTownBot memiliki sistem penyimpanan konfigurasi yang dapat digunakan untuk melakukan backup dan pemindahan data.

Saat ini fitur export/import digunakan untuk:

```text
Commands
OC / Original Character / Character Skin
```

Contoh workflow:

```text
Perangkat Lama
      │
      ├── Export Commands
      └── Export OC
              ↓
           File Backup
              ↓
      Perangkat Baru
              │
              ├── Import Commands
              └── Import OC
```

Dengan sistem ini, pengguna tidak perlu membuat ulang seluruh command atau character secara manual.

---

# Troubleshooting

## Tidak menerima OTP

Periksa folder:

```text
Inbox
Spam
Junk
Promotions
```

Pastikan alamat email yang digunakan saat registrasi sudah benar.

---

## Tidak bisa login melalui aplikasi

Coba login melalui browser:

https://randsfk.vercel.app/login

Setelah berhasil login, buka:

https://randsfk.vercel.app/dashboard

Kemudian ambil API Key pada bagian **Your Apikey**.

---

## API Key tidak dapat digunakan

Pastikan:

* API Key disalin secara lengkap.
* Tidak terdapat spasi tambahan.
* API Key berasal dari akun yang benar.
* Aplikasi menggunakan versi terbaru.

---

## Import tidak bekerja

Pastikan file yang digunakan merupakan file export yang sesuai dengan fitur yang dipilih.

Contohnya:

```text
Export Commands → Import Commands
Export OC → Import OC
```

Jangan menggunakan file OC pada menu import Commands atau sebaliknya.

---

# Untuk Pengguna Awam

PonyTownBot dirancang agar pengguna biasa **tidak perlu memahami programming** untuk menggunakan fitur utama aplikasi.

Alur penggunaan dasarnya:

```text
Download APK
      ↓
Install
      ↓
Login / Registrasi
      ↓
Ambil API Key
      ↓
Masukkan API Key
      ↓
Submit
      ↓
Gunakan PonyTownBot
```

Fitur seperti **Commands, OC, dan Music Player** dapat digunakan melalui antarmuka aplikasi tanpa harus mengedit source code.

---

# Untuk Pengguna Tingkat Lanjut

Pengguna yang ingin melakukan kustomisasi lebih jauh dapat menggunakan **RandEngine** untuk membuat sistem command dan response sendiri.

Contoh:

```text
Command Custom
Menu Custom
Random Response
Variable
Conditional
JSON
HTTP Request
Dynamic Response
```

Dokumentasi RandEngine:

https://randsfk.vercel.app/documentation

---

# Tujuan PonyTownBot

PonyTownBot dibuat untuk memberikan pengalaman bermain PonyTown yang lebih **fleksibel, interaktif, dan mudah dikustomisasi**.

Dengan hadirnya versi Android, pengguna tidak perlu lagi berurusan langsung dengan source code untuk menggunakan fitur utama bot.

PonyTownBot menyediakan:

```text
AI
Commands
Export / Import Commands
OC / Character
Export / Import OC
Music Player
Anti-AFK
Custom Owner & Bot Name
Chat Type Support
RandEngine
```

Pengguna biasa dapat langsung menggunakan aplikasi melalui GUI, sementara pengguna tingkat lanjut tetap memiliki kebebasan untuk melakukan kustomisasi melalui **RandEngine**.
