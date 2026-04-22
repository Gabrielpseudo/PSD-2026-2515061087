class Node:
    def __init__(self, no_antrian, nama, nik, tgl_lahir, prioritas):
        self.no_antrian = no_antrian
        self.nama = nama
        self.nik = nik
        self.tgl_lahir = tgl_lahir
        self.prioritas = prioritas
        self.prev = None
        self.next = None


class AntrianRumahSakit:
    def __init__(self):
        self.start = None
        self.rear = None
        self.counter = 1  

    def tambah_pasien(self, nama, nik, tgl_lahir, prioritas):
        new_node = Node(self.counter, nama, nik, tgl_lahir, prioritas)
        self.counter += 1

        if self.start is None:
            self.start = self.rear = new_node
        else:
            if prioritas == "darurat":
                new_node.next = self.start
                self.start.prev = new_node
                self.start = new_node

            elif prioritas == "lansia":
                current = self.start
                while current and current.prioritas == "darurat":
                    current = current.next

                if current is None:
                    new_node.prev = self.rear
                    self.rear.next = new_node
                    self.rear = new_node
                elif current.prev is None:
                    new_node.next = self.start
                    self.start.prev = new_node
                    self.start = new_node
                else:
                    prev_node = current.prev
                    prev_node.next = new_node
                    new_node.prev = prev_node
                    new_node.next = current
                    current.prev = new_node

            else:  
                new_node.prev = self.rear
                self.rear.next = new_node
                self.rear = new_node

        print(f"Pasien '{nama}' berhasil ditambahkan dengan nomor antrian {new_node.no_antrian}")

    def panggil_pasien(self):
        if self.start is None:
            print("Antrian kosong!")
            return

        pasien = self.start
        print("\nMemanggil Pasien:")
        print(f"No: {pasien.no_antrian}")
        print(f"Nama: {pasien.nama}")
        print(f"NIK: {pasien.nik}")
        print(f"Tgl Lahir: {pasien.tgl_lahir}")
        print(f"Prioritas: {pasien.prioritas}")

        self.start = self.start.next
        if self.start:
            self.start.prev = None
        else:
            self.rear = None

    def tampilkan_antrian(self):
        if self.start is None:
            print("Tidak ada antrian.")
            return

        print("\n=== DAFTAR ANTRIAN ===")
        current = self.start
        while current:
            print(f"[{current.no_antrian}] {current.nama} | {current.prioritas}")
            current = current.next


def main():
    antrian = AntrianRumahSakit()

    while True:
        print("\n=== SISTEM ANTRIAN RUMAH SAKIT ===")
        print("1. Tambah Pasien")
        print("2. Panggil Pasien")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nama = input("Nama: ")
            nik = input("NIK: ")
            tgl_lahir = input("Tanggal Lahir (dd-mm-yyyy): ")

            print("Prioritas:")
            print("1. Darurat")
            print("2. Lansia")
            print("3. Umum")

            p = input("Pilih prioritas: ")

            if p == '1':
                prioritas = "darurat"
            elif p == '2':
                prioritas = "lansia"
            else:
                prioritas = "umum"

            antrian.tambah_pasien(nama, nik, tgl_lahir, prioritas)

        elif pilihan == '2':
            antrian.panggil_pasien()

        elif pilihan == '3':
            antrian.tampilkan_antrian()

        elif pilihan == '4':
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()