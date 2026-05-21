Sistem Manajemen Stok Barang Menggunakan Binary Search Tree (BST)

Program ini merupakan aplikasi sederhana berbasis Python yang digunakan untuk mengelola data stok barang pada sebuah gudang bernama Gudang Gula.
Program menyediakan beberapa fitur utama seperti menambahkan stok barang, menghapus stok barang, serta menampilkan seluruh daftar barang yang tersimpan. 
Setiap barang memiliki nama dan kode barang sebagai identitas utama.
<img width="526" height="412" alt="Screenshot 2026-05-21 190945" src="https://github.com/user-attachments/assets/3fe5e88c-f93f-46f5-9ac6-7f0c83f3a71f" />
<img width="499" height="340" alt="Screenshot 2026-05-21 191001" src="https://github.com/user-attachments/assets/7f4e4f02-8f40-4472-bd50-9bc4dbd6ec7e" />
<img width="448" height="192" alt="Screenshot 2026-05-21 191011" src="https://github.com/user-attachments/assets/512ff910-f0c8-450e-8de0-c11e5a31bd64" />
<img width="673" height="316" alt="Screenshot 2026-05-21 191031" src="https://github.com/user-attachments/assets/b06414f7-7643-4a7a-8794-c9152039b060" />
<img width="572" height="263" alt="Screenshot 2026-05-21 191043" src="https://github.com/user-attachments/assets/9c07b497-9ee9-40c6-bf21-95ddc90af5db" />
Pada bagian awal program dibuat class bernama Node yang digunakan sebagai elemen dasar dalam Binary Search Tree. Setiap node menyimpan:
barang = nama barang
key = kode barang
left = pointer ke anak kiri
right = pointer ke anak kanan
Saat node pertama kali dibuat, pointer kiri dan kanan diinisialisasi dengan nilai None karena node belum memiliki cabang. 
Node ini menjadi tempat penyimpanan utama setiap data barang di dalam BST.
Bagian berikutnya membuat class BSTLanjut yang berfungsi untuk mengelola seluruh operasi Binary Search Tree.
Di dalam konstruktor (__init__), dibuat variabel root yang berfungsi sebagai akar pohon (root node). 
Pada awal program, nilai root masih None karena belum ada data barang yang dimasukkan.
Fungsi insert_node digunakan untuk menambahkan data barang ke dalam BST secara rekursif.
Fungsi menerima tiga parameter:
root = node saat ini
barang = nama barang
key = kode barang
Program pertama kali memeriksa apakah node saat ini kosong (None). Jika kosong, maka program membuat node baru dan mengembalikannya sebagai posisi baru di tree.
Jika key barang lebih kecil dari key root saat ini, maka program melanjutkan proses insert ke subtree kiri.
Jika key barang lebih besar dari key root saat ini, maka program melanjutkan proses insert ke subtree kanan.
Proses ini terus dilakukan secara rekursif sampai ditemukan posisi kosong untuk menyimpan data baru.
Struktur BST memastikan data tersusun secara otomatis berdasarkan kode barang.
