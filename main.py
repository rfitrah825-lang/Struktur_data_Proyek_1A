
from produk import Produk
from sistem_inventaris import SistemInventaris


# Membuat objek sistem inventaris
inventaris = SistemInventaris()


# 1. MENDAFTARKAN PRODUK BARU
produk1 = Produk(
    "P001", "Laptop", 7000000, 10,
    "Elektronik", "Laptop untuk bekerja"
)

produk2 = Produk(
    "P002", "Mouse", 100000, 50,
    "Aksesoris", "Mouse wireless"
)

produk3 = Produk(
    "P003", "Keyboard", 250000, 30,
    "Aksesoris", "Keyboard mekanik"
)

print("=== MENDAFTARKAN PRODUK ===")

for produk in [produk1, produk2, produk3]:
    berhasil = inventaris.daftarkan_produk(produk)

    if berhasil:
        print(produk.nama, "berhasil ditambahkan")
    else:
        print("ID produk sudah terdaftar")


# 2. MENCARI DETAIL PRODUK
print("\n=== MENCARI PRODUK ===")
inventaris.tampilkan_produk("P001")


# 3. MENGUBAH STOK DAN HARGA
print("\n=== MENGUBAH DATA PRODUK ===")

produk = inventaris.cari_produk("P001")

if produk is not None:
    produk.update_stok(15)
    produk.update_harga(6500000)

    inventaris.tampilkan_produk("P001")


# 4. MENGHAPUS PRODUK
print("\n=== MENGHAPUS PRODUK ===")

berhasil = inventaris.hapus_produk("P002")

if berhasil:
    print("Produk P002 berhasil dihapus")
else:
    print("Produk tidak ditemukan")


# 5. MENAMPILKAN JUMLAH PRODUK
print("\nJumlah produk tersimpan:",
      inventaris.penyimpanan.ukuran())
