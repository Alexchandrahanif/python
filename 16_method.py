# Methon disini sama aja dengan function


def tambah(angka1, angka2):
    return(angka1 + angka2)

hasil = tambah(10, 10)
print(hasil)


# bisa kita tambahkan default value nya
def namaLengkap(nama_awal="Alex", nama_akhir="Chandra"):
    return(nama_awal + nama_akhir)

hasil2 = namaLengkap() # tanpa kita mengisi parameter, kita bisa dapat hasilnya
hasil3 = namaLengkap(nama_awal="Hanif") # Dengan mengubah 1 parameter aja juga bisa
hasil4 = namaLengkap(nama_awal="Hanif", nama_akhir="Hanif") # Dengan mengubah 2 parameter juga bisa
print(hasil2, hasil3, hasil4)