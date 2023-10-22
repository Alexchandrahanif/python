# Untuk Set Sendiri, hampir sama dengan tuple dan list, beda nya dia bersifat uniq
# Dan Set Tidak bisa di akses dengan index, dan urutanya selalu berubah
# kalau mau akses harus pakai pengulangan (for)

nama = {"Alex", "Chandra", "Alex"} 

print(nama) # disini yg keluar cuma Alex dan Chandra Karena Alex cuma kebaca 1 akibat uniq

# untuk menambah data dengan fungsi .add()
nama.add("Hanif")
print(nama)

# dan remove untuk menghapus

nama.remove("Alex")
print(nama)