
import function

# list of dictionary
daftarKontak = []
daftarKontak.append({
  "nama" : "default",
  "telepon" : "123"
})

# Menu Program
while True:
  print("===== # Daftar Menu =====")
  print("1. Daftar Kontak")
  print("2. Tambah Kontak")
  print("3. Hapus Kontak")
  print("4. Cari Kontak")
  print("0. Keluar Program")
  
  menu = input("Pilih menu : ")
  
  if menu == "0":
    break
  elif menu == "1":
    function.displayKontak(daftarKontak)
  elif menu == "2":
    kontak = function.newKontak()
    daftarKontak.append(kontak)
  elif menu == "3":
    function.hapusKontak(daftarKontak)
  elif menu == "4":
    function.cariKontak(daftarKontak)
  else:
    print("Daftar tidak ditemukan.")
  
  
print("")  
print("=============================================")
print("Terimakasih telah menggunakan program ini")
print("=============================================")
