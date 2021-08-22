# Fungsi Management Kontak

def displayKontak(daftarKontak):
  for kontak in daftarKontak:
    print("")
    print("=================================")
    print(f"Nama : {kontak['nama']}")
    print(f"Telepon : {kontak['telepon']}")
    print("=================================")
    print("")
    
def newKontak():
  nama = input("nama : ")
  telepon = input("telepon : ")
  kontak = {
    "nama" : nama,
    "telepon" : telepon
  }
  return kontak
  
def hapusKontak(daftarKontak):
  telepon = input("Masukkan nomor telepon yang ingin di hapus: ")
  
  index = -1
  
  for i in range(0, len(daftarKontak)):
    kontak = daftarKontak[i]
    if telepon == kontak["telepon"]:
      index = i
      break
    
  if index == -1:
    print("Data kontak tidak ditemukan, Harap masukkan nomor telepon dengan benar")
  else:
    del daftarKontak[index]
    print("Data kontak berhasil dihapus")
    
def cariKontak(daftarKontak):
  namaYgDicari = input("Nama yang dicari: ")
  
  for kontak in daftarKontak:
    nama = kontak["nama"]
    if nama.lower().find(namaYgDicari.lower()) != -1:
      print("==============")
      print(f"Nama : {kontak['nama']}")
      print(f"Telepon : {kontak['telepon']}")
  
  
      
      

  
  
    