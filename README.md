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

# RandEngine Documentation

**Runtime:** RandEngine
**Bahasa:** RandEngine
**Model eksekusi:** line-based interpreter
**Block syntax:** `{ ... }`
**Variable:** `this.vars`
**Output:** `output`, `values`
**HTTP:** `$rget`, `$rpost`
**JSON:** `$rjson.*`

---

# 1. Gambaran Umum

RandEngine adalah bahasa scripting sederhana yang dijalankan oleh class `RandEngine`.

RandEngine bukan JavaScript. Script diproses oleh interpreter internal yang menangani:

* variable
* expression
* conditional
* function
* JSON
* HTTP
* command runtime
* interpolation
* object chaining

Syntax umum menggunakan `$`.

Contoh:

```rand
$var name = "Randy"

Halo $name.
Username: $username
Owner: $owner

$if $username == $owner {
    Kamu adalah owner.
} $else {
    Kamu adalah user.
}
```

RandEngine tidak membutuhkan `$print` untuk output biasa. Setiap baris teks yang bukan statement khusus akan diproses sebagai output.

---

# 2. Menjalankan RandEngine

Runtime dapat dibuat seperti berikut:

```javascript
const engine = new RandEngine({
  variables: {},
  commands: [],
  username: 'Randy',
  owner: 'RandSfk',
  msg: 'hello'
})

const result = await engine.run(code, {
  username: 'Randy',
  owner: 'RandSfk',
  msg: 'hello'
})
```

Result:

```javascript
{
  output: "...",
  values: [...],
  variables: {...},
  stopped: false
}
```

## `output`

`output` adalah seluruh hasil output yang sudah digabung menggunakan newline.

Contoh:

```javascript
result.output
```

```text
Hello Randy
Owner: RandSfk
```

## `values`

`values` berisi output sebagai array.

```javascript
[
  "Hello Randy",
  "Owner: RandSfk"
]
```

## `variables`

Berisi seluruh variable setelah script selesai.

```javascript
{
  name: "Randy",
  age: 21
}
```

## `stopped`

Bernilai `true` ketika execution dihentikan oleh `$stop` atau `$rawText`.

---

# 3. Struktur Script

RandEngine menggunakan model line-based.

Setiap baris diproses secara berurutan.

Contoh:

```rand
$var name = "Randy"

Halo $name.

$var age = 21

$if age >= 18 {
    Dewasa.
}
```

Baris kosong diabaikan.

Komentar menggunakan:

```rand
// komentar
```

Komentar dan baris kosong tidak dijalankan.

---

# 4. Output Tanpa `$print`

`$print` tidak digunakan oleh RandEngine versi ini.

Teks biasa langsung menjadi output.

```rand
Halo dunia.
```

Output:

```text
Halo dunia.
```

Variable juga bisa langsung digunakan:

```rand
$var name = "Randy"

Halo $name.
```

Output:

```text
Halo Randy.
```

Function juga dapat digunakan di dalam teks:

```rand
Nama: $uppercase($name)
```

---

# 5. `$rawText`

`$rawText` menghasilkan output kemudian langsung menghentikan execution.

```rand
$rawText Halo

Baris ini tidak dijalankan.
```

Output:

```text
Halo
```

`$rawText` dapat menerima string:

```rand
$rawText "Hello"
```

atau expression yang dapat dievaluasi:

```rand
$rawText $uppercase("hello")
```

---

# 6. Variable

## `$var`

Membuat variable.

```rand
$var name = "Randy"
$var age = 21
$var online = true
```

Nama variable harus berupa identifier:

```text
name
age
user1
_data
```

Contoh valid:

```rand
$var name = "Randy"
$var user1 = "Randy"
$var _data = 123
```

Contoh tidak valid:

```rand
$var 123name = "Randy"
$var user-name = "Randy"
```

---

# 7. `$set`

`$set` memiliki dua bentuk.

## Statement

```rand
$set name = "Randy"
$set age = 21
```

## Function-style

```rand
$set(name = "Randy")
$set(age = 21)
```

Contoh:

```rand
$var score = 10

$set score = 20

Score: $score
```

---

# 8. `$get`

`$get` mengambil value berdasarkan nama variable.

```rand
$var name = "Randy"

$get("name")
```

Hasil:

```text
Randy
```

Nama variable juga dapat diberikan tanpa tanda quote:

```rand
$get(name)
```

Contoh:

```rand
$var username = "Randy"

User: $get(username)
```

`$get` juga dapat digunakan di dalam expression:

```rand
$var age = 21

$if $get(age) >= 18 {
    Dewasa.
}
```

---

# 9. Akses Variable Langsung

Selain `$get`, variable dapat digunakan langsung dengan prefix `$` atau `#`.

Contoh:

```rand
$var name = "Randy"

Hello $name.
Hello #name.
```

Keduanya mengakses variable yang sama.

Untuk variable:

```rand
$var score = 100
```

dapat digunakan:

```rand
Score: $score
```

atau:

```rand
Score: #score
```

Syntax ini juga berlaku di expression:

```rand
$if $score >= 80 {
    Lulus.
}
```

atau:

```rand
$if #score >= 80 {
    Lulus.
}
```

---

# 10. Runtime Context

RandEngine mempunyai beberapa symbol bawaan.

## `$username`

Nama user yang sedang menjalankan script.

```rand
Halo $username.
```

Nilainya berasal dari:

```javascript
context.username
```

---

## `$owner`

Nama owner.

```rand
Owner: $owner
```

Nilainya berasal dari:

```javascript
context.owner
```

---

## `$msg`

Pesan atau input yang diberikan ke runtime.

```rand
Pesan: $msg
```

---

## `$date`

Tanggal saat script dijalankan.

Format:

```text
YYYY/MM/DD
```

Contoh:

```rand
Tanggal: $date
```

---

## `$time`

Waktu saat script dijalankan.

Format:

```text
HH:MM
```

Contoh:

```rand
Jam: $time
```

---

# 11. `$vars`

`$vars` menampilkan seluruh variable.

```rand
$var name = "Randy"
$var age = 21

$vars
```

Output:

```text
name = "Randy"
age = 21
```

`$vars` juga dapat digunakan di dalam teks:

```rand
Data saat ini:

$vars
```

Atau:

```rand
Variables:
$vars
```

---

# 12. `$vars.reset`

Menghapus seluruh variable.

```rand
$vars.reset
```

Runtime menghasilkan:

```text
Semua variable berhasil direset.
```

Setelah reset, variable custom sebelumnya tidak lagi tersedia.

---

# 13. `$vars.filter()`

Menampilkan variable berdasarkan tipe.

```rand
$vars.filter(string)
```

```rand
$vars.filter(number)
```

```rand
$vars.filter(boolean)
```

```rand
$vars.filter(array)
```

```rand
$vars.filter(object)
```

```rand
$vars.filter(null)
```

Tipe yang dikenali:

| Tipe      | Contoh             |
| --------- | ------------------ |
| `string`  | `"hello"`          |
| `number`  | `123`              |
| `boolean` | `true`             |
| `array`   | `[1, 2, 3]`        |
| `object`  | `{"name":"Randy"}` |
| `null`    | `null`             |

---

# 14. Conditional

RandEngine mendukung:

```text
$if
$elseif
$else
```

Block menggunakan `{` dan `}`.

Contoh:

```rand
$if age >= 18 {
    Dewasa.
}
```

Conditional juga dapat memakai parentheses:

```rand
$if (age >= 18) {
    Dewasa.
}
```

Keduanya valid.

---

# 15. `$if`

Contoh:

```rand
$var age = 21

$if age >= 18 {
    Dewasa.
}
```

Variable runtime juga dapat digunakan:

```rand
$if $username == $owner {
    Kamu adalah owner.
}
```

Contoh lainnya:

```rand
$if $score >= 80 {
    Lulus.
}
```

---

# 16. `$elseif`

Contoh:

```rand
$if age >= 18 {
    Dewasa.
} $elseif age >= 13 {
    Remaja.
}
```

Beberapa `$elseif` dapat digunakan:

```rand
$if score >= 90 {
    Grade A
} $elseif score >= 80 {
    Grade B
} $elseif score >= 70 {
    Grade C
} $else {
    Grade D
}
```

---

# 17. `$else`

Contoh:

```rand
$if age >= 18 {
    Dewasa.
} $else {
    Belum dewasa.
}
```

Format `} $else {` didukung.

Format tersebut juga berlaku untuk `$elseif`:

```rand
$if score >= 90 {
    A
} $elseif score >= 80 {
    B
} $else {
    C
}
```

---

# 18. Nested Conditional

Conditional dapat berada di dalam conditional lain.

```rand
$if $score >= 80 {
    Nilai bagus.

    $if $username == $owner {
        Owner dengan nilai bagus.
    } $else {
        User dengan nilai bagus.
    }
} $else {
    Nilai belum cukup.
}
```

---

# 19. Operator Comparison

Operator yang didukung:

```text
==
!=
===
!==
>
<
>=
<=
```

Contoh:

```rand
$if age == 21 {
    Umur sama.
}
```

```rand
$if age != 21 {
    Umur berbeda.
}
```

```rand
$if age >= 18 {
    Dewasa.
}
```

---

# 20. Logical Operator

RandEngine mendukung:

```text
&&
||
!
```

Contoh AND:

```rand
$if age >= 18 && online == true {
    Access granted.
}
```

Contoh OR:

```rand
$if $username == "Randy" || $username == "Admin" {
    Authorized.
}
```

Contoh NOT:

```rand
$var banned = false

$if !banned {
    Tidak dibanned.
}
```

---

# 21. `$stop`

Menghentikan execution.

```rand
Start

$stop

Baris ini tidak dijalankan.
```

Output:

```text
Start
```

---

# 22. `$resetAi`

Syntax:

```rand
$resetAi
```

Pada implementasi saat ini, `$resetAi` hanya dilewati oleh interpreter.

Tidak ada reset state tambahan yang dilakukan oleh class `RandEngine`.

---

# 23. `$wait`

Syntax:

```rand
$wait(1000)
```

Parameter menggunakan millisecond.

Contoh:

```rand
Start

$wait(1000)

Done
```

Runtime menjalankan delay ketika `$wait(...)` digunakan sebagai statement sendiri.

---

# 24. Function

RandEngine mendukung function-style syntax:

```text
$lowercase(...)
$uppercase(...)
$replace(...)
$repeat(...)
$random(...)
$getType(...)
$toString(...)
$math(...)
$rmath(...)
```

Function dapat digunakan sendiri:

```rand
$uppercase("hello")
```

atau sebagai bagian dari text:

```rand
Nama: $uppercase($username)
```

---

# 25. `$lowercase`

Mengubah text menjadi huruf kecil.

```rand
$lowercase("HELLO")
```

Hasil:

```text
hello
```

---

# 26. `$uppercase`

Mengubah text menjadi huruf besar.

```rand
$uppercase("hello")
```

Hasil:

```text
HELLO
```

---

# 27. `$replace`

Format:

```text
$replace(value, search, replacement)
```

Contoh:

```rand
$replace("Hello Randy", "Randy", "World")
```

Hasil:

```text
Hello World
```

---

# 28. `$repeat`

Format:

```text
$repeat(value, count)
```

Contoh:

```rand
$repeat("ha", 3)
```

Hasil:

```text
hahaha
```

Jumlah negatif dianggap `0`.

---

# 29. `$random`

## Tanpa argument

```rand
$random()
```

Menghasilkan angka random dari `0` sampai kurang dari `1`.

## Random integer

```rand
$random(1, 10)
```

Menghasilkan integer dari `1` sampai `10`, termasuk kedua batas.

## Beberapa nilai

```rand
$random("red", "blue", "green")
```

Menghasilkan salah satu value.

## Array

```rand
$random(["red", "blue", "green"])
```

Mengambil satu element secara random.

---

# 30. `$getType`

Mengecek tipe value.

```rand
$getType("hello")
```

Hasil:

```text
string
```

Contoh:

```rand
$getType(123)
```

```text
number
```

Array:

```rand
$getType([1, 2, 3])
```

```text
array
```

Object:

```rand
$getType({"name":"Randy"})
```

```text
object
```

Boolean:

```rand
$getType(true)
```

```text
boolean
```

Null:

```rand
$getType(null)
```

```text
null
```

---

# 31. `$toString`

Mengubah value menjadi string.

```rand
$toString(123)
```

Hasil:

```text
123
```

Object:

```rand
$toString({"name":"Randy"})
```

Hasil berupa JSON string.

---

# 32. Math Expression

RandEngine memiliki parser expression internal.

Operator matematika:

```text
+
-
*
/
%
```

Contoh:

```rand
$math(10 + 5)
```

Hasil:

```text
15
```

Precedence:

```text
()
*
/
%
+
-
```

Contoh:

```rand
$math(10 + 5 * 2)
```

Hasil:

```text
20
```

---

# 33. `$math`

Format:

```text
$math(expression)
```

Contoh:

```rand
$math(10 + 5 * 2)
```

Hasil:

```text
20
```

---

# 34. `$rmath`

`$rmath` adalah alias dari `$math`.

```rand
$rmath(10 + 5)
```

Hasil:

```text
15
```

---

# 35. Math dengan Variable

Variable dapat langsung dipakai sebagai operand.

```rand
$var a = 10
$var b = 5

$math(a + b)
```

Hasil:

```text
15
```

Comparison juga didukung:

```rand
$math(a > b)
```

Hasil:

```text
true
```

Runtime symbol juga dapat dipakai:

```rand
$if $username == $owner {
    Owner.
}
```

---

# 36. String Expression

String dapat digabung menggunakan `+` di dalam expression.

```rand
$var name = "Randy"

$math("Hello " + name)
```

Hasil:

```text
Hello Randy
```

Untuk output biasa, lebih sederhana menggunakan interpolation:

```rand
Hello $name
```

---

# 37. Array

Array dapat dibuat dalam satu expression.

```rand
$var items = [1, 2, 3]
```

Contoh:

```rand
$var colors = ["red", "green", "blue"]

Color: $random(colors)
```

Array juga dapat digunakan langsung:

```rand
$random(["red", "blue", "green"])
```

---

# 38. Object / JSON Value

Object dapat ditulis langsung menggunakan JSON dalam satu expression.

```rand
$var user = {"name":"Randy","age":21}
```

Object tersebut dapat diproses melalui JSON function atau chaining.

Object multiline tidak merupakan format statement tersendiri dalam parser line-based. Gunakan object JSON dalam satu expression.

Contoh yang disarankan:

```rand
$var user = {"name":"Randy","age":21}
```

---

# 39. `$rjson.toJson`

Mengubah JSON string menjadi object.

```rand
$rjson.toJson("{\"name\":\"Randy\"}")
```

Contoh:

```rand
$var json = $rjson.toJson("{\"name\":\"Randy\",\"age\":21}")
```

Variable `json` sekarang berisi object.

---

# 40. `$rjson.toString`

Mengubah object menjadi JSON string.

```rand
$rjson.toString({"name":"Randy","age":21})
```

Hasil:

```json
{"name":"Randy","age":21}
```

---

# 41. `$rjson.get`

Mengambil property dari object berdasarkan path.

Format:

```text
$rjson.get(object, path)
```

Contoh:

```rand
$rjson.get({"name":"Randy"}, "name")
```

Hasil:

```text
Randy
```

Nested object:

```rand
$rjson.get({"user":{"name":"Randy"}}, "user.name")
```

Hasil:

```text
Randy
```

---

# 42. Object Chaining

RandEngine mendukung chaining menggunakan:

```text
.$method(...)
```

Contoh:

```rand
"HELLO".$lowercase()
```

Hasil:

```text
hello
```

Contoh:

```rand
"hello".$uppercase()
```

Hasil:

```text
HELLO
```

---

# 43. Chaining pada Variable

Variable dapat dipanggil lalu diteruskan ke method.

```rand
$var name = "HELLO"

name.$lowercase()
```

Hasil:

```text
hello
```

Object:

```rand
$var user = {"name":"Randy","age":21}
```

Kemudian:

```rand
user.$get("name")
```

Hasil:

```text
Randy
```

---

# 44. `.$get()`

Mengambil property dari object.

```rand
$var user = {"name":"Randy","age":21}

user.$get("name")
```

Hasil:

```text
Randy
```

Nested:

```rand
$var user = {"profile":{"age":21}}

user.$get("profile.age")
```

Hasil:

```text
21
```

---

# 45. `.$getType()`

Mengecek tipe object atau value hasil chaining.

```rand
$var user = {"name":"Randy"}

user.$getType()
```

Hasil:

```text
object
```

---

# 46. `.$toString()`

Mengubah value menjadi string.

```rand
$var user = {"name":"Randy"}

user.$toString()
```

---

# 47. `.$lowercase()`

```rand
"HELLO".$lowercase()
```

Hasil:

```text
hello
```

---

# 48. `.$uppercase()`

```rand
"hello".$uppercase()
```

Hasil:

```text
HELLO
```

---

# 49. `.$replace()`

Format:

```text
value.$replace(search, replacement)
```

Contoh:

```rand
"Hello Randy".$replace("Randy", "World")
```

Hasil:

```text
Hello World
```

---

# 50. `.$repeat()`

Format:

```text
value.$repeat(count)
```

Contoh:

```rand
"ha".$repeat(3)
```

Hasil:

```text
hahaha
```

---

# 51. Nested Function

Function dapat berada di dalam function lain.

```rand
$uppercase($lowercase("HELLO"))
```

Hasil:

```text
HELLO
```

Contoh JSON:

```rand
$getType($rjson.toJson("{\"name\":\"Randy\"}"))
```

Hasil:

```text
object
```

---

# 52. JSON Chaining

Contoh:

```rand
$rjson.toJson("{\"user\":{\"name\":\"Randy\"}}").$get("user.name")
```

Hasil:

```text
Randy
```

---

# 53. Interpolation

RandEngine mendukung symbol langsung di dalam text.

Contoh:

```rand
$var name = "Randy"

Halo $name.
```

Built-in context:

```text
$username
$owner
$msg
$date
$time
```

Custom variable juga bisa digunakan:

```text
$myVariable
```

atau:

```text
#myVariable
```

---

# 54. Variable di Dalam Conditional

Variable runtime dapat menjadi operand langsung.

```rand
$if $username == $owner {
    Owner detected.
}
```

Alias `#` juga dapat digunakan:

```rand
$if #username == #owner {
    Owner detected.
}
```

Custom variable:

```rand
$var score = 90

$if $score >= 80 {
    Pass.
}
```

---

# 55. Variable di Mana Saja

Contoh lengkap:

```rand
$var name = "Randy"
$var score = 95

User: $name
Score: $score
Owner: $owner
Message: $msg

$if $score >= 90 {
    Grade A.
}
```

`$get()` tetap tersedia:

```rand
User: $get(name)
```

---

# 56. Command System

Runtime menerima array `commands`.

Contoh:

```javascript
const commands = [
  {
    name: "ping",
    description: "Mengecek bot"
  },
  {
    name: "menu",
    description: "Menampilkan menu"
  },
  {
    name: "help",
    description: "Menampilkan bantuan"
  }
]
```

Kemudian:

```javascript
const engine = new RandEngine({
  commands
})
```

---

# 57. `$cmd[n]`

Mengambil nama command berdasarkan index.

Index dimulai dari `1`.

```rand
$cmd[1]
```

Jika command pertama bernama `ping`, hasilnya:

```text
ping
```

`$cmd[n]` digunakan sebagai statement sendiri.

Contoh:

```rand
$cmd[1]
```

---

# 58. `$desc[n]`

Mengambil description command berdasarkan index.

```rand
$desc[1]
```

Jika description pertama:

```text
Mengecek bot
```

maka hasilnya:

```text
Mengecek bot
```

Index dimulai dari `1`.

---

# 59. `$//cmds`

Menghasilkan seluruh nama command sebagai daftar.

```rand
Daftar command:

$//cmds
```

Contoh:

```text
Daftar command:

ping
menu
help
```

---

# 60. `$//descs`

Menghasilkan seluruh description command.

```rand
$//descs
```

Contoh:

```text
Mengecek bot
Menampilkan menu
Menampilkan bantuan
```

---

# 61. `$cmds` dan `$descs`

`$cmds` dan `$descs` digunakan untuk membuat template berdasarkan seluruh command.

Placeholder:

```text
[no]
```

digunakan sebagai nomor command.

Contoh:

```rand
[no] $cmds - $descs
```

Dengan commands:

```javascript
[
  {
    name: "ping",
    description: "Mengecek bot"
  },
  {
    name: "menu",
    description: "Menampilkan menu"
  }
]
```

hasil:

```text
1 ping - Mengecek bot
2 menu - Menampilkan menu
```

Template akan dibuat untuk setiap command.

---

# 62. Command dengan Text Biasa

Command tidak membutuhkan `$print`.

Contoh command:

```json
{
  "name": "hello",
  "description": "Menyapa pengguna"
}
```

Kode:

```text
halo $username
```

Ketika command dijalankan, hasilnya misalnya:

```text
halo Randy
```

---

# 63. Shareable Templates

Share Template menggunakan JSON.

Format dasar:

```json
{
  "ai-setting": {},
  "menu": {}
}
```

---

# 64. Struktur `ai-setting`

`ai-setting` berisi konfigurasi AI template.

Contoh:

```json
"ai-setting": {
  "gender": "Male",
  "lore": "Lil Uzi Vert adalah rapper asal Amerika serikat yang sekarang bermain game PonyTown",
  "name": "Lil Uzi Vert",
  "sifat": "Rapper, Chill, Asik"
}
```

Properti:

| Properti | Deskripsi                    |
| -------- | ---------------------------- |
| `gender` | Gender AI                    |
| `lore`   | Latar belakang atau karakter |
| `name`   | Nama AI                      |
| `sifat`  | Sifat atau karakter AI       |

Properti tersebut merupakan struktur template dan tidak diproses langsung oleh class `RandEngine`.

---

# 65. Struktur `menu`

`menu` berisi command template.

Format:

```json
"nama-command-deskripsi": "kode RandEngine"
```

Contoh:

```json
"hello-Menyapa pengguna": "Halo $username"
```

Nama command:

```text
hello
```

Deskripsi:

```text
Menyapa pengguna
```

Kode command:

```text
Halo $username
```

---

# 66. Contoh Template

```json
{
  "ai-setting": {
    "gender": "Male",
    "lore": "AI assistant",
    "name": "RandAI",
    "sifat": "Chill, Friendly"
  },
  "menu": {
    "hello-Menyapa pengguna": "Halo $username",
    "waktu-Menampilkan waktu": "Sekarang $time"
  }
}
```

---

# 67. Aturan Nama Command

Format command template:

```text
nama-command-deskripsi
```

Contoh:

```text
hello-Menyapa pengguna
menu-Menampilkan menu
ping-Mengecek bot
```

Bagian sebelum tanda `-` adalah nama command.

Bagian setelah tanda `-` adalah deskripsi.

---

# 68. Minimal Template

Template paling sederhana:

```json
{
  "ai-setting": {},
  "menu": {}
}
```

Contoh dengan satu command:

```json
{
  "ai-setting": {},
  "menu": {
    "hello-Menyapa pengguna": "Halo $username"
  }
}
```

---

# 69. Variable dan Function di Command

Command dapat menggunakan seluruh syntax RandEngine yang tersedia.

Contoh:

```json
{
  "menu": {
    "hello-Menyapa pengguna": "Halo $username",
    "score-Menampilkan skor": "$var score = $random(1, 100)\nScore: $score"
  }
}
```

---

# 70. HTTP GET — `$rget`

Format:

```text
$rget(url, query, headers)
```

URL:

```rand
$rget("https://example.com/api")
```

Query:

```rand
$rget(
    "https://example.com/api",
    {"name":"Randy","page":1}
)
```

Headers:

```rand
$rget(
    "https://example.com/api",
    {},
    {"Authorization":"Bearer TOKEN"}
)
```

Query dan headers harus berupa value yang dapat dievaluasi menjadi object.

---

# 71. HTTP POST — `$rpost`

Format:

```text
$rpost(url, body, headers)
```

Contoh:

```rand
$rpost(
    "https://example.com/api",
    {"name":"Randy"}
)
```

Dengan header:

```rand
$rpost(
    "https://example.com/api",
    {"name":"Randy"},
    {"Authorization":"Bearer TOKEN"}
)
```

Jika `Content-Type` tidak diberikan, runtime menambahkan:

```text
Content-Type: application/json
```

---

# 72. HTTP Response

RandEngine membaca response dengan urutan:

1. `Content-Type`
2. JSON parsing
3. fallback ke text

Jika response berupa:

```json
{
  "name": "Randy"
}
```

hasil `$rget` dapat menjadi object.

Contoh:

```rand
$var response = $rget("https://example.com/api")

$rjson.get(response, "name")
```

---

# 73. HTTP Error

HTTP dengan status non-2xx menghasilkan `HTTP_ERROR`.

Contoh:

```text
HTTP 404: Not Found
```

---

# 74. Fetch Requirement

`fetch` tidak lagi diwajibkan ketika `run()` dimulai.

HTTP function akan memerlukan `fetch` ketika `$rget` atau `$rpost` benar-benar dijalankan.

Jika tidak tersedia:

```text
FETCH_UNAVAILABLE
```

---

# 75. Literal String

String dapat menggunakan double quote:

```rand
"Hello"
```

atau single quote:

```rand
'Hello'
```

Escape yang didukung:

```text
\n
\r
\t
\\
\"
\'
```

Contoh:

```rand
$var text = "Hello\nWorld"
```

---

# 76. Boolean

Literal boolean:

```rand
true
false
```

Contoh:

```rand
$var online = true
$var banned = false
```

Conditional:

```rand
$if online == true {
    Online.
}
```

---

# 77. Null

Literal:

```rand
null
```

Contoh:

```rand
$var data = null
```

Tipe value:

```rand
$getType(null)
```

Hasil:

```text
null
```

---

# 78. Expression

Expression dapat berisi:

* angka
* string
* boolean
* null
* variable
* runtime symbol
* function
* operator
* array

Contoh:

```rand
$var a = 10
$var b = 20

$math(a + b)
```

---

# 79. Array Expression

Array dapat digunakan sebagai value:

```rand
$var numbers = [1, 2, 3]
```

Array juga bisa digunakan pada `$random`:

```rand
$random([1, 2, 3])
```

---

# 80. Object Expression

Object dapat dibuat sebagai JSON value:

```rand
$var user = {"name":"Randy","age":21}
```

Object kemudian dapat diproses:

```rand
user.$get("name")
```

---

# 81. Function di Dalam Expression

Function dapat digunakan sebagai bagian expression.

```rand
$var name = $uppercase("randy")
```

Hasil variable:

```text
RANDY
```

Nested function:

```rand
$var name = $uppercase($lowercase("Randy"))
```

---

# 82. Chaining

Format:

```text
value.$method(...)
```

Method yang tersedia:

```text
$get
$getType
$toString
$lowercase
$uppercase
$replace
$repeat
```

Contoh:

```rand
"HELLO".$lowercase()
```

```rand
"hello".$uppercase()
```

```rand
"hello world".$replace("world", "Randy")
```

---

# 83. `$get` vs `.$get()`

Untuk variable:

```rand
$var name = "Randy"

$get("name")
```

Untuk object:

```rand
$var user = {"name":"Randy"}

user.$get("name")
```

`$get(...)` mengambil variable dari `this.vars`.

`.$get(...)` mengambil property dari object hasil sebelumnya.

---

# 84. `$rjson.get` vs `.$get`

Dengan object:

```rand
$var user = {"name":"Randy"}
```

Bisa menggunakan:

```rand
$rjson.get(user, "name")
```

atau:

```rand
user.$get("name")
```

Keduanya menghasilkan:

```text
Randy
```

---

# 85. Contoh Conditional dengan Runtime Symbol

```rand
$if $username == $owner {
    Access granted.
} $else {
    Access denied.
}
```

Alias `#`:

```rand
$if #username == #owner {
    Access granted.
} $else {
    Access denied.
}
```

---

# 86. Contoh Script dengan Variable

```rand
$var name = $username
$var score = $random(1, 100)

Halo $name.
Score: $score

$if $score >= 80 {
    Excellent.
} $elseif $score >= 60 {
    Good.
} $else {
    Need improvement.
}
```

---

# 87. Contoh Script JSON

```rand
$var user = {"name":"Randy","age":21}

Nama: $user.$get("name")
Age: $user.$get("age")
```

Cara yang lebih langsung:

```rand
$var user = {"name":"Randy","age":21}

user.$get("name")
```

---

# 88. Contoh Script API

```rand
$var response = $rget("https://example.com/api")

$if $getType(response) == "object" {
    $rjson.toString(response)
} $else {
    API tidak menghasilkan object.
}
```

---

# 89. Contoh Command Menu

Dengan command:

```javascript
[
  {
    name: "menu",
    description: "Menampilkan menu utama"
  },
  {
    name: "ping",
    description: "Mengecek response bot"
  },
  {
    name: "help",
    description: "Menampilkan bantuan"
  }
]
```

Script:

```rand
=== MENU ===

[no] $cmds - $descs
```

Hasil:

```text
=== MENU ===

1 menu - Menampilkan menu utama
2 ping - Mengecek response bot
3 help - Menampilkan bantuan
```

---

# 90. Contoh Sistem Pesan

```rand
Bot aktif.

User: $username
Owner: $owner
Message: $msg
Date: $date
Time: $time
```

---

# 91. Contoh Authorization

```rand
$if $username == $owner {
    Authorized.
} $else {
    Unauthorized.
}
```

Dengan variable:

```rand
$var role = "admin"

$if $role == "admin" {
    Admin access.
} $else {
    User access.
}
```

---

# 92. Contoh Score System

```rand
$var score = $random(1, 100)

Score: $score

$if $score >= 90 {
    Grade A
} $elseif $score >= 80 {
    Grade B
} $elseif $score >= 70 {
    Grade C
} $else {
    Grade D
}
```

---

# 93. Contoh Function + Variable

```rand
$var name = "randy"

Nama asli: $name
Nama besar: $uppercase($name)
Nama kecil: $lowercase($name)
```

---

# 94. Contoh `$vars`

```rand
$var name = "Randy"
$var age = 21
$var online = true

Variables:

$vars
```

Output:

```text
Variables:

name = Randy
age = 21
online = true
```

Nilai object dan array akan diformat sebagai JSON.

---

# 95. Syntax Reference

## Variables

```text
$var name = value
$set name = value
$set(name = value)

$get("name")
$get(name)

$name
#name

$vars
$vars.reset
$vars.filter(type)
```

## Conditional

```text
$if condition {

}

$elseif condition {

}

$else {

}
```

## Runtime

```text
$stop
$resetAi
$wait(milliseconds)
```

## Raw Output

```text
$rawText value
```

## Runtime Context

```text
$username
$owner
$msg
$date
$time
```

## Commands

```text
$cmd[n]
$desc[n]

$//cmds
$//descs

$cmds
$descs
```

## String

```text
$lowercase(value)
$uppercase(value)
$replace(value, search, replacement)
$repeat(value, count)
```

## Utility

```text
$random(...)
$getType(value)
$toString(value)
```

## Math

```text
$math(expression)
$rmath(expression)
```

## JSON

```text
$rjson.toJson(value)
$rjson.toString(value)
$rjson.get(object, path)
```

## HTTP

```text
$rget(url, query, headers)
$rpost(url, body, headers)
```

## Chaining

```text
value.$get(path)
value.$getType()
value.$toString()
value.$lowercase()
value.$uppercase()
value.$replace(search, replacement)
value.$repeat(count)
```

---

# 96. Operator Reference

| Operator | Fungsi                             |   |    |
| -------- | ---------------------------------- | - | -- |
| `+`      | Penjumlahan / string concatenation |   |    |
| `-`      | Pengurangan                        |   |    |
| `*`      | Perkalian                          |   |    |
| `/`      | Pembagian                          |   |    |
| `%`      | Modulo                             |   |    |
| `==`     | Equality                           |   |    |
| `===`    | Strict equality                    |   |    |
| `!=`     | Not equal                          |   |    |
| `!==`    | Strict not equal                   |   |    |
| `>`      | Lebih besar                        |   |    |
| `<`      | Lebih kecil                        |   |    |
| `>=`     | Lebih besar atau sama              |   |    |
| `<=`     | Lebih kecil atau sama              |   |    |
| `&&`     | AND                                |   |    |
| `        |                                    | ` | OR |
| `!`      | NOT                                |   |    |

---

# 97. Execution Flow

RandEngine menjalankan script melalui tahapan:

```text
Source Code
    ↓
normalize()
    ↓
validateStructure()
    ↓
execute()
    ↓
validateLine()
    ↓
Statement / Expression / Block
    ↓
Output / Variable
    ↓
Result Object
```

---

# 98. Error Object

Error runtime menggunakan:

```javascript
{
  name: "RandEngineError",
  code: "...",
  lineNumber: 0,
  line: "...",
  source: "..."
}
```

`lineNumber` menunjukkan line asli source.

---

# 99. Error Code

Beberapa error yang tersedia:

```text
RUNTIME_ERROR

UNEXPECTED_CLOSING_BRACE
MISSING_CLOSING_BRACE
UNEXPECTED_OPENING_BRACE

INVALID_DOLLAR_TOKEN
UNKNOWN_SYNTAX
UNCLOSED_STRING

INVALID_BLOCK_SYNTAX
INVALID_IF_SYNTAX
INVALID_ELSEIF_SYNTAX
INVALID_ELSE_SYNTAX

INVALID_VAR_SYNTAX
INVALID_SET_SYNTAX
INVALID_GET_SYNTAX

INVALID_CMD_SYNTAX
INVALID_DESC_SYNTAX
INVALID_WAIT_SYNTAX

INVALID_VARS_FILTER_SYNTAX

COMMAND_NOT_FOUND

PRINT_REMOVED

INVALID_FUNCTION
UNKNOWN_FUNCTION
MISSING_CLOSING_PARENTHESIS

INVALID_CHAIN
UNKNOWN_OBJECT_METHOD

INVALID_JSON
INVALID_URL

FETCH_UNAVAILABLE
INVALID_RESPONSE

RGET_ARGUMENT_ERROR
RGET_ERROR

RPOST_ARGUMENT_ERROR
RPOST_ERROR

HTTP_ERROR

INVALID_EXPRESSION
INVALID_ARRAY
DIVISION_BY_ZERO
UNEXPECTED_TOKEN
INVALID_CHARACTER

INVALID_ARGUMENT_STRUCTURE
UNCLOSED_ARGUMENT_STRUCTURE

INTERPOLATION_LIMIT
EXPRESSION_CALL_LIMIT
```

---

# 100. Syntax yang Tidak Digunakan

RandEngine **bukan JavaScript**.

Syntax JavaScript berikut tidak digunakan:

```rand
console.log("hello")
```

```rand
function() {}
```

```rand
object.property
```

Untuk object gunakan:

```rand
object.$get("property")
```

atau:

```rand
$rjson.get(object, "property")
```

---

# 101. `$print`

`$print` **sudah dihapus dari syntax RandEngine versi ini**.

Kode berikut tidak valid:

```rand
$print "Hello"
```

dan:

```rand
$print("Hello")
```

Runtime akan menghasilkan:

```text
PRINT_REMOVED
```

Gunakan text biasa:

```rand
Hello
```

atau:

```rand
Hello $username
```

Untuk output sekaligus menghentikan execution gunakan:

```rand
$rawText Hello
```

---

# 102. Syntax yang Tidak Lagi Digunakan

Beberapa syntax lama tidak termasuk dalam runtime saat ini:

```text
$randint
$print
```

Untuk random integer gunakan:

```rand
$random(1, 100)
```

Untuk output gunakan text biasa:

```rand
Halo $username
```

---

# 103. Best Practice

Gunakan variable:

```rand
$var name = "Randy"

Hello $name.
```

Gunakan conditional:

```rand
$if $username == $owner {
    Owner.
} $else {
    User.
}
```

Gunakan function:

```rand
Name: $uppercase($username)
```

Gunakan math:

```rand
$var score = $random(1, 100)

$if $score >= 80 {
    Good.
}
```

Gunakan JSON:

```rand
$var user = {"name":"Randy","age":21}

user.$get("name")
```

Gunakan API:

```rand
$var data = $rget("https://example.com/api")

$rjson.toString(data)
```

---

# 104. Full Example

```rand
$var name = $username
$var message = $msg
$var score = $random(1, 100)

=== RAND ENGINE ===

User: $name
Message: $message
Score: $score
Owner: $owner
Date: $date
Time: $time

$if $username == $owner {
    Role: Owner
} $else {
    Role: User
}

$if $score >= 80 {
    Result: Excellent
} $elseif $score >= 60 {
    Result: Good
} $else {
    Result: Need improvement
}

$var data = {"name":"Randy","score":$score}

$data.$get("name")
$getType($data)
```

---

# 105. Complete Syntax List

Berdasarkan class `RandEngine` saat ini, syntax utama yang tersedia adalah:

```text
$var
$set
$get

$rawText

$if
$elseif
$else

$wait
$vars
$vars.filter
$vars.reset

$resetAi
$stop

$cmd
$desc
$cmds
$descs
$//cmds
$//descs

$username
$owner
$msg
$date
$time

$random
$lowercase
$uppercase
$replace
$repeat

$math
$rmath

$rget
$rpost

$rjson.toJson
$rjson.toString
$rjson.get

$getType
$toString
```

Variable custom dapat diakses melalui:

```text
$variable
#variable
$get(variable)
```

Built-in context juga dapat diakses melalui:

```text
$username
#username

$owner
#owner

$msg
#msg

$date
#date

$time
#time
```

Object chaining:

```text
value.$get(...)
value.$getType()
value.$toString()
value.$lowercase()
value.$uppercase()
value.$replace(...)
value.$repeat(...)
```

---

# 106. Share Template Lengkap

Contoh template yang sesuai dengan syntax RandEngine versi saat ini:

```json
{
  "ai-setting": {
    "gender": "Male",
    "lore": "AI assistant",
    "name": "RandAI",
    "sifat": "Chill, Friendly"
  },
  "menu": {
    "hello-Menyapa pengguna": "Halo $username",
    "owner-Mengecek owner": "$if $username == $owner {\n    Kamu adalah owner.\n} $else {\n    Kamu bukan owner.\n}",
    "score-Menghasilkan score": "$var score = $random(1, 100)\nScore: $score"
  }
}
```

---

# 107. Prinsip RandEngine

RandEngine terdiri dari beberapa lapisan:

```text
Variables
    $var / $set / $get
    $variable / #variable

Control Flow
    $if / $elseif / $else / $stop

Runtime
    $username / $owner / $msg / $date / $time

Functions
    $random
    $lowercase
    $uppercase
    $replace
    $repeat
    $getType
    $toString

Math
    $math / $rmath

JSON
    $rjson.*

Network
    $rget / $rpost

Commands
    $cmd / $desc
    $cmds / $descs
    $//cmds / $//descs

Object Chaining
    value.$get(...)
    value.$getType()
    value.$toString()
    value.$lowercase()
    value.$uppercase()
    value.$replace(...)
    value.$repeat(...)
```

Interpolation memungkinkan syntax tersebut dipakai langsung di dalam text:

```rand
Halo $username.
Score: $score
Owner: $owner
Data: $get(name)
```

---

# 108. RandEngine Quick Reference

```rand
$var name = "Randy"
$var score = $random(1, 100)

Halo $name.

User: $username
Owner: $owner
Message: $msg
Date: $date
Time: $time

$if $username == $owner {
    Authorized.
} $else {
    Unauthorized.
}

Score: $score

$if $score >= 80 {
    Excellent.
} $elseif $score >= 60 {
    Good.
} $else {
    Need improvement.
}

$var user = {"name":"Randy","age":21}

Nama: $user.$get("name")
Tipe: $user.$getType()

$vars
```

**RandEngine = Variables + Expressions + Blocks + Functions + JSON + HTTP + Command Runtime + Interpolation.**

