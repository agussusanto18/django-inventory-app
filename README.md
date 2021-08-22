# Aplikasi Inventory Barang #

* Fitur Aplikasi
    * ADMIN
        * Management Barang
        * List Reservasi
        * Ubah Status Reservasi (Diterima/Ditolak)
        * List User
        * List Reservasi berdasarkan User
        * Export data reservasi ke PDF
    * USER
        * List Reservasi
        * Tambah Reservasi
    * Login
    * Logout
    * Register

## Menginstall Paket Yang Diperlukan ##
Aplikasi ini hanya membutuhkan satu paket Python "Django", itu dibangun dan diuji dengan versi Django 2.x. Untuk menginstalnya gunakan perintah berikut:

```
pip install -r requirements.txt
```

Django 2 membutuhkan Python 3, jika belum menginstall Python3 install terlebih dahulu.

## Menjalankan Aplikasi ##
Sebelum menjalankan aplikasi, kita perlu membuat tabel pada Database yang dibutuhkan:

```
.\manage.py migrate
```
atau
```
python3 manage.py migrate
```

Sekarang kita dapat menjalankan server web development:

```
.\manage.py runserver
```
atau
```
python manage.py runserver
```

Untuk mengakses aplikasi, buka URL http://localhost:8000/

## Akses Login ##

* Akun Admin
    * username: admin
    * password: admin123

* Akun User
    * username: aldo
    * password: aldo123