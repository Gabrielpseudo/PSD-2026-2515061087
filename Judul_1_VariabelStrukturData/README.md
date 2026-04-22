Sistem Antrian Rumah Sakit

Program ini merupakan aplikasi berbasis terminal (CLI) yang digunakan untuk mengelola antrian pasien di rumah sakit secara sederhana. Pengguna dapat menambahkan pasien ke dalam antrian, memanggil pasien berdasarkan urutan, serta melihat daftar pasien yang sedang menunggu.
Program ini menerapkan struktur data Doubly Linked List, dimana setiap data pasien disimpan dalam sebuah node yang memiliki dua pointer yaitu prev (sebelumnya) dan next (berikutnya). Algoritma yang digunakan adalah FIFO (First In First Out), dimana pasien yang pertama masuk akan menjadi pasien pertama yang dipanggil.

<img width="758" height="585" alt="Screenshot 2026-04-22 184016" src="https://github.com/user-attachments/assets/62325586-d0c0-49b3-8486-fb85a8644c93" />
<img width="684" height="743" alt="Screenshot 2026-04-22 184031" src="https://github.com/user-attachments/assets/bbf6ef1c-8334-4164-9d67-ce5dafd070f6" />
<img width="801" height="688" alt="Screenshot 2026-04-22 184039" src="https://github.com/user-attachments/assets/73c591b4-54e7-4da0-85b3-a37a7c906c75" />
Pembuatan Node
Baris pertama mendefinisikan sebuah class yang digunakan sebagai wadah data pasien.
Baris kedua membuat konstruktor yang akan dijalankan saat objek node dibuat.
Baris ketiga menyimpan nilai input berupa nama pasien ke dalam atribut data.
Baris keempat menginisialisasi penunjuk ke node sebelumnya dengan nilai kosong.
Baris kelima menginisialisasi penunjuk ke node berikutnya dengan nilai kosong.

Inisialisasi Sistem Antrian
Baris berikutnya mendefinisikan class untuk mengelola antrian pasien.
Baris selanjutnya membuat konstruktor untuk class tersebut.
Baris berikutnya menginisialisasi penunjuk ke elemen pertama antrian sebagai kosong.
Baris terakhir pada bagian ini menginisialisasi penunjuk ke elemen terakhir antrian sebagai kosong.

Proses Menambahkan Pasien
Baris pertama pada bagian ini mendefinisikan fungsi untuk menambahkan pasien.
Baris berikutnya membuat objek node baru berdasarkan nama pasien yang diinput.
Baris selanjutnya mengecek apakah antrian masih kosong.
Jika kondisi kosong terpenuhi, maka node baru langsung dijadikan sebagai elemen pertama dan terakhir.
Jika tidak kosong, program masuk ke kondisi lain.
Node baru dihubungkan ke node terakhir sebelumnya melalui pointer sebelumnya.
Node terakhir lama kemudian dihubungkan ke node baru melalui pointer berikutnya.
Setelah itu posisi elemen terakhir diperbarui menjadi node yang baru ditambahkan.
Baris terakhir menampilkan pesan bahwa pasien berhasil ditambahkan ke antrian.

Proses Memanggil Pasien
Baris pertama mendefinisikan fungsi untuk memanggil pasien.
Baris berikutnya mengecek apakah antrian kosong.
Jika kosong, program menampilkan pesan bahwa antrian tidak tersedia.
Baris selanjutnya menghentikan proses agar tidak terjadi error.
Jika antrian tidak kosong, data pasien pada posisi paling depan diambil.
Baris berikutnya menampilkan nama pasien yang dipanggil.
Selanjutnya, penunjuk ke elemen pertama digeser ke node berikutnya.
Program kemudian mengecek apakah masih ada data setelah pergeseran.
Jika masih ada, hubungan ke node sebelumnya dihapus agar tidak terjadi referensi lama.
Jika tidak ada, penunjuk ke elemen terakhir juga dikosongkan.

Menampilkan Antrian
Baris pertama mendefinisikan fungsi untuk menampilkan seluruh antrian.
Baris berikutnya mengecek apakah antrian kosong.
Jika kosong, program menampilkan pesan bahwa tidak ada data.
Baris selanjutnya menghentikan fungsi.
Jika tidak kosong, program menampilkan judul daftar antrian.
Kemudian sistem mulai dari elemen pertama sebagai titik awal penelusuran.
Sebuah variabel dibuat untuk memberi nomor urutan.
Program melakukan perulangan selama masih ada node.
Setiap iterasi akan menampilkan data pasien beserta nomor urutnya.
Penunjuk kemudian berpindah ke node berikutnya.
Nomor urutan ditambah setiap perulangan.

Program Utama 
Baris pertama mendefinisikan fungsi utama program.
Baris berikutnya membuat objek antrian dari class yang telah dibuat.
Program masuk ke perulangan tak terbatas agar dapat terus menerima input.
Baris berikutnya menampilkan judul sistem.
Selanjutnya menampilkan pilihan menu yang tersedia.
Program kemudian meminta input dari pengguna.
Jika pengguna memilih opsi pertama, program akan meminta nama pasien lalu memanggil fungsi untuk menambahkan pasien ke dalam antrian.
Jika memilih opsi kedua, program akan menjalankan fungsi untuk memanggil pasien dari depan antrian.
Jika memilih opsi ketiga, program akan menampilkan seluruh isi antrian.
Jika memilih opsi keempat, program akan menampilkan pesan selesai lalu menghentikan perulangan.
Jika input tidak sesuai pilihan, program akan menampilkan pesan kesalahan.

Eksekusi Program
Baris terakhir digunakan untuk memastikan bahwa program hanya dijalankan ketika file dieksekusi secara langsung.
Jika kondisi terpenuhi, maka fungsi utama akan dipanggil dan seluruh program mulai berjalan.

Link Video : 
