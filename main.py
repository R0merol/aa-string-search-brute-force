import json

def baca_json() -> dict:  # pake txt juga bisa kali
    with open("teks.json", "r") as file:
        return json.load(file)
    

def cek_file_json():  # Gk penting
    try:
        with open("teks.json", "r") as file:
            file.close()
    except FileNotFoundError:
        default = {}
        with open("data.json", "w") as f:
            json.dump(default, f, indent=2)

def input_teks():
    print("-"*10+" Input Teks "+"-"*10)
    judul = input("Judul teks: ")
    teks = input("Tempelkan teks di sini: ")

    cek_file_json()
    
    with open("teks.json", "r") as file:
        teks_json = json.load(file)

    teks_json[judul] = teks
    teks_json = dict(sorted(teks_json.items()))
    
    with open("teks.json", "w") as file:
        json.dump(teks_json, file, indent=2)

def brute_force(teks: str):
    pass

def pencarian_string():
    print("-"*10+" Pencarian String "+"-"*10)
    while True:
        try:
            print("Pilih judul teks:")
            teks_json = baca_json()
            list_judul = []
            for i, judul in enumerate(teks_json):
                print(f"{i+1}. {judul}")
                list_judul.append(judul)
            index = int(input(">>> Pilihan: ")) - 1
            print("-"*20)
            print("Judul: " + list_judul[index])
            print("Teks:")
            teks = teks_json[list_judul[index]]
            print(teks)
            print("-"*20)
            brute_force(teks)
            break
        except IndexError:
            print("Pilihan tidak ada, silahkan input kembali")
            continue
        except ValueError:
            print("Pilihan harus berbentuk nomor, silahkan input kembali")
            continue

def apakah_ingin_mengulang() -> bool:
    print("Apakah anda ingin mengulang program?")
    jawaban = input(">>> Jawaban (y): ")
    return True if jawaban.lower() == "y" else False

def main():
    print("-" * 10 + " Pencarian String menggunakan Algoritma Brute-Force " + "-" * 10)
    while True:
        print("Pilih opsi tersebut:")
        print("1. Input teks")
        print("2. Pencarian string")
        pilihan = input(">>> Pilihan Anda: ")
        if pilihan=="1":
            input_teks()
        elif pilihan=="2":
            pencarian_string()
        else:
            print("Pilihan salah, silahkan input kembali")
            print("#"*20)
            continue
        if apakah_ingin_mengulang():
            continue
        break

if __name__ == '__main__':
    main()
