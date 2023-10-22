for i in range(1, 100):
    if i%2 == 0:
        break
    print(i)


while True:
    data = input("Masukkan 1 huruf : ")
    if data == "x":
        print("Selamat kamu berhasil")
        break
    print(f"Maaf {data} tidak sama dengan x")
