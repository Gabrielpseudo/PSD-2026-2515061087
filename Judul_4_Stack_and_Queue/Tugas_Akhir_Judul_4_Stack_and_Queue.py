class StackArray:
    def __init__(self, max_size=1000):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Antrian Penuh")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"{x} Masuk Dalam Antrian")

    def pop(self):
        if self.is_empty():
            print("Antrian Kosong")
            return
        print(f"{self.st[self.top_idx]} Dipanggil Ke Kasir")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Antrian Kosong")
            return
        print(f"Customer Berikutnya: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Antrian Kosong")
            return
        print("Antrian Customer: ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" ")
        print()


def main():
    stack = StackArray()
    pilih = 0
    while pilih != 5:
        print("\n=== Toko Iskandar Jaya ===")
        print("1. Masukkan Nama Customer")
        print("2. Panggil Nama Customer")
        print("3. Antrian Terdepan")
        print("4. Tampilkan Antrian")
        print("5. Matikan Program")
        try:
            pilih = int(input("Pilih: ")) 
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            continue
        if pilih == 1:
            try:
                val = input("Nama Customer: ") 
                stack.push(val)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
