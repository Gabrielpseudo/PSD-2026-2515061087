Sistem Manajemen Data Buku Menggunakan Hash Map Open Addressing

Program ini merupakan aplikasi sederhana berbasis Python yang digunakan untuk mengelola data buku pada sebuah perpustakaan atau toko buku. 
Program menyediakan fitur untuk menambahkan data buku berdasarkan kode buku dan judul buku, kemudian melakukan pencarian data berdasarkan kode buku yang telah dimasukkan. 
Seluruh proses dilakukan melalui menu interaktif yang dijalankan pada terminal sehingga pengguna dapat mengelola data dengan mudah.
Program ini menerapkan struktur data Hash Map dengan metode Open Addressing menggunakan teknik Linear Probing. 
Pada metode ini, setiap data disimpan pada indeks hasil fungsi hash. Apabila terjadi tabrakan (collision) karena indeks yang dituju telah terisi, maka program akan mencari slot kosong berikutnya secara berurutan hingga menemukan tempat penyimpanan yang tersedia. 
Pendekatan ini memungkinkan proses penyimpanan dan pencarian data berlangsung lebih efisien dibandingkan pencarian secara linear pada seluruh data.

Program diawali dengan pembuatan class SlotState yang digunakan untuk memberikan status pada setiap slot di dalam hash table. 
Class ini memiliki tiga kondisi, yaitu EMPTY yang menunjukkan slot masih kosong, OCCUPIED yang menunjukkan slot telah berisi data, dan DELETED yang menunjukkan data pada slot tersebut telah dihapus tetapi slot masih dipertahankan agar proses pencarian tetap berjalan dengan benar. 
Penggunaan status ini sangat penting pada implementasi Open Addressing karena slot yang dihapus tidak boleh langsung dianggap kosong.
Selanjutnya dibuat class Entry yang berfungsi sebagai wadah penyimpanan setiap data buku di dalam hash table. 
Setiap objek Entry memiliki atribut key untuk menyimpan kode buku, value untuk menyimpan judul buku, dan state untuk menyimpan status slot. 
Pada saat objek pertama kali dibuat, nilai key dan value diinisialisasi dengan None, sedangkan status slot diatur menjadi EMPTY, yang berarti slot tersebut belum digunakan.
Bagian berikutnya adalah class HashMapOpenAddressing, yaitu class utama yang mengelola seluruh operasi hash map. 
Pada konstruktor (__init__), program menentukan ukuran hash table melalui variabel SIZE yang secara default bernilai 10. 
Setelah itu dibuat sebuah list yang berisi objek Entry sebanyak ukuran yang telah ditentukan. 
Dengan demikian, setiap indeks pada hash table telah memiliki slot penyimpanan yang siap digunakan.
Program kemudian memiliki fungsi hash_function yang digunakan untuk menentukan posisi penyimpanan data berdasarkan kode buku. 
Fungsi ini menggunakan operasi modulus terhadap ukuran hash table sehingga hasil perhitungan selalu berada pada rentang indeks yang tersedia. 
Rumus tersebut juga mengantisipasi kemungkinan adanya nilai negatif sehingga hasil hash tetap valid.
Proses penambahan data dilakukan melalui fungsi insert. 
Fungsi ini menerima dua parameter, yaitu kode buku sebagai key dan judul buku sebagai value. Program pertama kali menghitung indeks awal menggunakan fungsi hash. 
Selanjutnya dibuat variabel first_deleted yang digunakan untuk menyimpan posisi slot yang sebelumnya telah dihapus apabila ditemukan selama proses pencarian slot kosong.
Program kemudian melakukan proses Linear Probing, yaitu memeriksa setiap slot secara berurutan mulai dari indeks hasil hash. 
Jika slot yang diperiksa berstatus OCCUPIED dan memiliki key yang sama, maka data lama akan diperbarui dengan data baru. 
Jika slot berstatus DELETED, maka posisi tersebut disimpan sebagai kandidat tempat penyimpanan apabila nantinya tidak ditemukan slot kosong lain. 
Jika ditemukan slot dengan status EMPTY, maka data langsung disimpan pada slot tersebut atau pada slot DELETED pertama yang telah ditemukan sebelumnya. 
Apabila seluruh proses selesai tanpa menemukan tempat penyimpanan, fungsi akan mengembalikan nilai False sebagai tanda bahwa penyimpanan gagal.
Untuk melakukan pencarian data, program menyediakan fungsi search. Fungsi ini menerima parameter berupa kode buku yang ingin dicari. 
Program menghitung indeks awal menggunakan fungsi hash, kemudian melakukan pemeriksaan slot satu per satu menggunakan teknik Linear Probing. Jika ditemukan slot dengan status EMPTY, maka pencarian langsung dihentikan karena data dipastikan tidak ada. 


Namun jika ditemukan slot dengan status OCCUPIED dan key yang sesuai, maka objek Entry tersebut dikembalikan sebagai hasil pencarian. Jika seluruh slot telah diperiksa tetapi data tidak ditemukan, fungsi mengembalikan nilai None.
Program juga menyediakan fungsi remove_key yang digunakan untuk menghapus data dari hash table. Fungsi ini terlebih dahulu mencari data menggunakan fungsi search. Jika data ditemukan, status slot diubah menjadi DELETED tanpa menghapus isi data secara langsung. Teknik ini digunakan agar proses pencarian pada slot berikutnya tetap dapat berjalan dengan benar sesuai prinsip Open Addressing. Jika data tidak ditemukan, fungsi mengembalikan nilai False.
Selain itu terdapat fungsi display yang digunakan untuk menampilkan seluruh isi hash table. Program melakukan perulangan dari indeks pertama hingga indeks terakhir, kemudian memeriksa status setiap slot. Jika slot kosong maka ditampilkan tulisan EMPTY, jika slot telah dihapus maka ditampilkan DELETED, sedangkan jika slot berisi data maka ditampilkan pasangan kode buku dan judul buku yang tersimpan pada slot tersebut. Fungsi ini berguna untuk melihat kondisi hash table setelah proses penambahan maupun penghapusan data.
Program juga memiliki fungsi menu yang bertugas menampilkan daftar pilihan operasi kepada pengguna. Menu terdiri atas tiga pilihan utama, yaitu menambahkan buku, mencari buku, dan keluar dari program. Fungsi ini hanya berfungsi sebagai tampilan antarmuka sederhana agar pengguna dapat memilih operasi yang diinginkan.
Bagian utama program berada pada fungsi main. Pada bagian ini program pertama kali membuat objek HashMapOpenAddressing sebagai tempat penyimpanan data buku. Selanjutnya program menjalankan perulangan tanpa batas sehingga menu akan terus ditampilkan sampai pengguna memilih keluar.
