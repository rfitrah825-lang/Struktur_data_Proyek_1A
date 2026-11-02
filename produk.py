
class Produk:
    def __init__(self, id_produk, nama, harga, stok, kategori, deskripsi):
        self.id_produk = str(id_produk)
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori
        self.deskripsi = deskripsi

    def get_detail(self):
        return {
            "ID Produk": self.id_produk,
            "Nama": self.nama,
            "Harga": self.harga,
            "Stok": self.stok,
            "Kategori": self.kategori,
            "Deskripsi": self.deskripsi
        }

    def update_stok(self, jumlah):
        if jumlah < 0:
            raise ValueError("Stok tidak boleh negatif")

        self.stok = jumlah

    def update_harga(self, harga_baru):
        if harga_baru < 0:
            raise ValueError("Harga tidak boleh negatif")

        self.harga = harga_baru
