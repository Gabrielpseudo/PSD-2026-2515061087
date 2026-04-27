def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def exchange_sort(arr, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i][1] > arr[j][1]:
                tukar(arr, i, j)


def main():
    try:
        n = int(input("Masukkan jumlah Mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan nama dan nilai Mahasiswa:")
    for i in range(n):
        while True:
            try:
                nama = (input())
                nilai = int(input())
                arr.append([nama,nilai])
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
    print(f"Data awal: {arr}")
    exchange_sort(arr, n)
    print("Data terurut:", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    main()