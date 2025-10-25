#Tugas 1
#Buat Variable
nama_produk1 = "Kopi Pagi"
harga_produk1 = 18000.5
nama_produk2 = "Roti Cokelat"
harga_produk2 = 10000
status_roti = True

# Menampilkan data
print("Nama produk 1:", nama_produk1)
print("Harga produk 1:", harga_produk1)
print("Nama produk 2:", nama_produk2)
print("Harga produk 2:", harga_produk2)
print("Status ketersediaan roti:", status_roti)


#Tugas 2
# input
jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")
jumlah_roti_str = input("Masukkan jumlah pesanan roti: ")

# tipe data awal
print("Tipe data awal jumlah kopi:", type(jumlah_kopi_str))
print("Tipe data awal jumlah roti:", type(jumlah_roti_str))

# Konversi ke integer
jumlah_kopi_int = int(jumlah_kopi_str)
jumlah_roti_int = int(jumlah_roti_str)

# Mengecek tipe data setelah konversi
print("Tipe data setelah konversi jumlah kopi:", type(jumlah_kopi_int))
print("Tipe data setelah konversi jumlah roti:", type(jumlah_roti_int))


#Tugas 3
# Hitung total harga masing-masing
total_harga_kopi = harga_produk1 * jumlah_kopi_int
total_harga_roti = harga_produk2 * jumlah_roti_int

# Hitung total belanja keseluruhan
total_belanja = total_harga_kopi + total_harga_roti

# Variabel uang bayar
uang_bayar = 50000

# Hitung kembalian
kembalian = uang_bayar - total_belanja

# Cetak hasil
print("Total harga kopi:", total_harga_kopi)
print("Total harga roti:", total_harga_roti)
print("Total belanja keseluruhan:", total_belanja)
print("Uang yang dibayarkan:", uang_bayar)
print("Kembalian:", kembalian)

#Tugas 4
# Input nama pelanggan
nama_pelanggan = input("Masukkan nama pelanggan: ")

# Membuat pesan terima kasih
pesan_terima_kasih = "Terima kasih, " + nama_pelanggan + " sudah berbelanja di Cat cafe!"

# Membuat garis pemisah (karakter * diulang 25 kali)
garis = "*" * 25

# Variabel dari tugas sebelumnya
nama_produk1 = "Kopi Pagi"
harga_kopi = 18000.5
jumlah_kopi_int = 2
total_harga_kopi = harga_kopi * jumlah_kopi_int

# Cetak struk
print(garis)
print(pesan_terima_kasih)
print(garis)
print(f"Total harga {nama_produk1} adalah Rp{total_harga_kopi}")