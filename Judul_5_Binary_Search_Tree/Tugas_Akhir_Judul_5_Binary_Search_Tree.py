class Node:
    def __init__(self, barang, key):
        self.barang = barang
        self.key = key
        self.left = None
        self.right = None

class BSTLanjut:
    def __init__(self):
        self.root = None

    def insert_node(self, root, barang, key):
        if root is None:
            return Node(barang, key)
        if key < root.key:
            root.left = self.insert_node(root.left, barang, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, barang, key)
        return root

    def delete_node(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.barang = successor.barang
                root.right = self.delete_node(root.right, successor.key)
        return root

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def level_order(self, root):
        if root is None:
            print("(kosong)")
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(0)
            print(f"({current.key}, '{current.barang}')", end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

def main():
    bst = BSTLanjut()
    pilih = 0
    while pilih != 4: 
        print("\n=== Gudang Gula ===")
        print("1. Menambah stok barang")
        print("2. Menghapus stok barang")
        print("3. Menampilkan stok barang")
        print("4. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            continue
        if pilih == 1:
            try:
                barang = input("Masukkan nama barang: ")
                x = int(input("Masukkan kode barang: "))
                bst.insert(barang, x)
                print(f"Stok barang {barang} berhasil ditambahkan dengan kode {x}")
            except ValueError:
                print("Input kode barang tidak valid! Harap masukkan angka.")
        elif pilih == 2:
            try:
                x = int(input("Masukkan kode barang yang ingin dihapus: "))
                bst.delete(x)
                print(f"Stok barang dengan kode {x} berhasil dihapus")
            except ValueError:
                print("Input kode barang tidak valid! Harap masukkan angka.")
        elif pilih == 3:
            print("Daftar stok barang: ", end="")
            bst.level_order(bst.root)
        elif pilih == 4:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
