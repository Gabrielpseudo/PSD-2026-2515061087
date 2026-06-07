class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY

class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nIsi Hash Table (Open Addressing, Linear Probing):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key},{self.table[i].value})")

def menu():
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Hapus Buku")
    print("4. Tampilkan Semua Buku")
    print("5. Keluar")

def main():
    hashmap = HashMapOpenAddressing()
    while True:
        menu()
        choice = int(input("Pilih Menu: "))
        if choice == 1:
            key = int(input("Masukkan Kode Buku: "))
            value = input("Masukkan Judul Buku: ")
            if hashmap.insert(key, value):
                print("Buku Berhasil Ditambahkan.")
            else:
                print("Buku Tidak Ditemukan!")
        elif choice == 2:
             key = int(input("Masukkan Kode Buku Yang Ingin Dicari: "))
             entry = hashmap.search(key)
             if entry is not None:
                print(f"Buku Ditemukan: {entry.value}")
             else:
                print("Buku Tidak Ditemukan")
        elif choice == 3:
            key = int(input("Masukkan Kode Buku Yang Ingin Dihapus: "))
            if hashmap.remove_key(key):
                print("Buku Berhasil Dihapus")
            else:
                print("Buku Tidak Ditemukan")
        elif choice == 4:
            hashmap.display()
        elif choice == 5:
            break
        else:
            print("Pilihan Tidak Valid")

if __name__ == "__main__":
    main()