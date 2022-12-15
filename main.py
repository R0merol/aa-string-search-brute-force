import json
import textwrap


def baca_json() -> dict:
    with open("teks.json", "r") as file:
        return json.load(file)


def cek_file_json():  # cek apakah ada file teks.json atau tidak
    try:
        with open("teks.json", "r") as file:
            file.close()
    except FileNotFoundError:
        default = {}
        with open("data.json", "w") as f:
            json.dump(default, f, indent=2)


def input_teks():
    print(form_header(f"{' Input Teks ':=^100}"))
    judul = input("Judul teks: ")
    teks = input("Tempelkan teks di sini: ")

    cek_file_json()

    with open("teks.json", "r") as file:
        teks_json = json.load(file)

    teks_json[judul] = teks
    teks_json = dict(sorted(teks_json.items()))

    with open("teks.json", "w") as file:
        json.dump(teks_json, file, indent=2)


def brute_force(pola: str, teks: str):
    M = len(pola)
    N = len(teks)
    jumlah_pola = 0

    # Looping pola[] satu per satu
    for i in range(N - M + 1):
        j = 0

        # Untuk index i, cek pola yang cocok
        while(j < M):
            if (teks[i + j] != pola[j]):
                break
            j += 1

        if (j == M):
            print(f'Kata "{pola}" ditemukan pada indeks: {i}')
            jumlah_pola += 1

    if jumlah_pola == 0:
        print(f'Kata "{pola}" tidak ditemukan pada teks tersebut')


def pencarian_string():
    print(form_header(f"{' Pencarian String ':=^100}"))
    while True:
        try:
            print("Pilih judul teks:")
            teks_json = baca_json()
            list_judul = []
            for i, judul in enumerate(teks_json):
                print(f"{i+1}. {judul}")
                list_judul.append(judul)
            index = int(input(">>> Pilihan: ")) - 1
            print("-" * 100)
            print("Judul: " + list_judul[index])
            print("Teks:")
            teks = teks_json[list_judul[index]]
            print(textwrap.fill(teks, width=100))
            print("-" * 100)
            while True:
                pola = input(">>> Masukkan kata yang ingin dicari: ")
                brute_force(pola, teks)
                if apakah_ingin_mengulang("pencarian"):
                    continue
                break
            break
        except IndexError:
            print(form_error(f"{' Pilihan tidak ada, silahkan input kembali ':!^100}"))
            continue
        except ValueError:
            print(
                form_error(f"{' Pilihan harus berbentuk nomor, silahkan input kembali ':!^100}"))
            continue


def apakah_ingin_mengulang(program="program") -> bool:
    print(f"Apakah anda ingin mengulang {program}?")
    jawaban = input(">>> Jawaban (y): ")
    return True if jawaban.lower() == "y" else False


def form_header(text: str) -> str:
    return "\033[34m\033[1m" + text + "\033[0m"


def form_error(text: str) -> str:
    return "\033[31m" + text + "\033[0m"


def main():
    print(form_header(f"{' Pencarian String menggunakan Algoritma Brute-Force ':=^100}"))
    while True:
        print("Pilih opsi tersebut:")
        print("1. Pencarian string")
        print("2. Input teks")
        pilihan = input(">>> Pilihan Anda: ")
        if pilihan == "1":
            pencarian_string()
        elif pilihan == "2":
            input_teks()
        else:
            print(form_error(f"{' Pilihan salah, silahkan input kembali ':!^100}"))
            continue
        if apakah_ingin_mengulang():
            continue
        break


if __name__ == '__main__':
    main()
