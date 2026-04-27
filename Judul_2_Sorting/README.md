Sistem Pengurutan Nilai Mahasiswa Menggunakan Exchange Sort

Program ini merupakan aplikasi sederhana berbasis Python yang digunakan untuk mengurutkan data mahasiswa berdasarkan nilai yang dimiliki. Pengguna diminta memasukkan jumlah mahasiswa, kemudian menginput nama dan nilai masing-masing mahasiswa. Setelah seluruh data dimasukkan, program akan menampilkan data awal dan hasil data yang sudah diurutkan dari nilai terkecil ke terbesar. Program ini menerapkan algoritma Exchange Sort, yaitu metode pengurutan dengan cara membandingkan setiap elemen dengan elemen lain yang berada setelahnya, lalu menukar posisi jika urutannya salah. Struktur data yang digunakan adalah list dua dimensi, dimana setiap data mahasiswa disimpan dalam bentuk pasangan [nama, nilai].

<img width="813" height="377" alt="Screenshot 2026-04-27 190750" src="https://github.com/user-attachments/assets/70fda412-668d-43d3-b738-a0a00ded5572" />
<img width="989" height="813" alt="Screenshot 2026-04-27 190807" src="https://github.com/user-attachments/assets/6ee3a092-e7b1-4a4d-b586-40636a694a5d" />

Fungsi Tukar Data
Pada bagian awal program dibuat fungsi khusus untuk menukar posisi dua data dalam list. Fungsi ini menerima parameter berupa array, indeks pertama, dan indeks kedua. Nilai pada indeks pertama disimpan sementara ke variabel bantuan, kemudian isi indeks pertama diganti dengan isi indeks kedua, lalu isi indeks kedua diganti dengan nilai sementara. Fungsi ini digunakan saat proses sorting jika ditemukan data yang urutannya salah.

Fungsi Exchange Sort
Selanjutnya dibuat fungsi utama untuk proses pengurutan data. Fungsi ini menerima parameter array dan jumlah data. Program menggunakan perulangan pertama untuk menentukan posisi elemen yang sedang dicek, kemudian perulangan kedua digunakan untuk membandingkan elemen tersebut dengan data setelahnya. Setiap kali program menemukan nilai mahasiswa pada posisi sekarang lebih besar daripada nilai mahasiswa setelahnya, maka fungsi tukar akan dipanggil untuk menukar posisi kedua data tersebut. Proses ini terus berjalan hingga seluruh data tersusun dari nilai terkecil ke terbesar.

Fungsi Main (Program Utama)
Pada bagian utama program, sistem pertama kali meminta input jumlah mahasiswa. Program menggunakan try-except untuk mencegah kesalahan jika pengguna memasukkan data selain angka. Jika input tidak valid, maka program menampilkan pesan error dan berhenti. Jika input benar, program membuat list kosong untuk menampung data mahasiswa. Selanjutnya program menampilkan instruksi agar pengguna memasukkan nama dan nilai mahasiswa.Program melakukan perulangan sebanyak jumlah mahasiswa yang dimasukkan. Di setiap perulangan, sistem meminta nama mahasiswa lalu meminta nilai mahasiswa. Nilai harus berupa angka, sehingga jika pengguna memasukkan selain angka, program akan menampilkan pesan kesalahan dan meminta input ulang. Setelah data berhasil dimasukkan, nama dan nilai disimpan ke dalam list dalam bentuk pasangan data. Setelah semua data selesai diinput, program menampilkan data awal sebelum diurutkan.

Menampilkan Hasil Sorting
Setelah itu, fungsi exchange_sort() dipanggil untuk mengurutkan data mahasiswa berdasarkan nilai. Setelah proses sorting selesai, program menampilkan hasil data yang sudah terurut secara berurutan dari nilai terkecil ke terbesar. Program menggunakan perulangan terakhir untuk mencetak seluruh isi list hasil pengurutan ke layar.

<img width="1573" height="469" alt="Screenshot 2026-04-27 190628" src="https://github.com/user-attachments/assets/1f89e36b-1f4c-44e7-a65f-248373526273" />
Penjelasan Output
Pada saat program dijalankan, sistem pertama kali meminta pengguna memasukkan jumlah mahasiswa. Pada contoh di atas, pengguna memasukkan angka 5, artinya akan ada lima data mahasiswa yang dimasukkan. Selanjutnya program meminta input nama dan nilai masing-masing mahasiswa. Data yang dimasukkan adalah:
[Adi 67,
Arief 69,
Budi 72,
Brahma 70,
Dani 76]
Setelah seluruh data selesai diinput, program menampilkan Data awal, yaitu data mahasiswa sesuai urutan saat dimasukkan oleh pengguna dan belum mengalami proses pengurutan. Kemudian program menjalankan algoritma Exchange Sort untuk mengurutkan data berdasarkan nilai dari yang terkecil ke terbesar. Hasil akhirnya ditampilkan pada bagian Data terurut, yaitu:
[Adi 67,
Arief 69,
Brahma 70,
Budi 72,
Dani 76]
Urutan tersebut membuktikan bahwa program berhasil melakukan proses sorting sesuai studi kasus, yaitu mengurutkan nilai mahasiswa secara ascending.

Link video : 
