banyak = int(input("Berapa Banyak Data Yang Ingin Kamu Masukkan : "))

nama = []
umur = []

for i in range(0,banyak):
    print(f"Data ke {i + 1}")
    input_nama = input("Masukkan Nama : ")
    input_umur = input("Masukkan Umur : ")

    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    
    print(f"{i+1}.Nama {data_nama} Berumur {data_umur} tahun")


