def sequential_search(arr, target):
    counter = 0
    for item in arr:
        if item.lower() == target.lower():
            counter += 1
    return counter


def main():
    arr = input("Masukkan List Nama Pasien: ").split()
    print(f"List Nama Pasien: {arr}")

    target = input("Masukkan nama yang ingin dicari: ")

    counter = sequential_search(arr, target)

    if counter > 0:
        print(f"Pasien atas nama {target} ditemukan.")
    else:
        print(f"Pasien atas nama {target} tidak ditemukan.")


if __name__ == "__main__":
    main()
