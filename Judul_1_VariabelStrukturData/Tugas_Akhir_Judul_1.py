class Node:
    def __init__(self, nama_pasien):
        self.data = nama_pasien
        self.prev = None
        self.next = None

class AntrianRumahSakit:
    def __init__(self):
        self.start = None  
        self.rear = None   

    def tambah_pasien(self, nama):
        new_node = Node(nama)
        if self.start is None:
            self.start = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        print(f"Pasien '{nama}' masuk antrian.")

    def panggil_pasien(self):
        if self.start is None:
            print("Antrian kosong!")
            return
        pasien = self.start.data
        print(f"Memanggil pasien: {pasien}")
        
        self.start = self.start.next
        if self.start is not None:
            self.start.prev = None
        else:
            self.rear = None  

    def tampilkan_antrian(self):
        if self.start is None:
            print("Tidak ada antrian.")
            return
            
        print("Antrian pasien:")
        current = self.start
        nomor = 1
        while current:
            print(f"{nomor}. {current.data}")
            current = current.next
            nomor += 1

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
            nama = input("Masukkan nama pasien: ")
            antrian.tambah_pasien(nama)
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