
from hash_table import HashTable


class SistemInventaris:
    def __init__(self):
        self.penyimpanan = HashTable()

    # Mendaftarkan produk baru
    def daftarkan_produk(self, produk):
        return self.penyimpanan.insert(produk)

    # Mencari produk
    def cari_produk(self, id_produk):
        return self.penyimpanan.search(id_produk)

    # Menghapus produk
    def hapus_produk(self, id_produk):
        return self.penyimpanan.delete(id_produk)

    # Menampilkan detail produk
    def tampilkan_produk(self, id_produk):
        produk = self.cari_produk(id_produk)

        if produk is None:
            print("Produk tidak ditemukan")
            return

        print("\n=== DETAIL PRODUK ===")

        for atribut, nilai in produk.get_detail().items():
            print(f"{atribut}: {nilai}")
