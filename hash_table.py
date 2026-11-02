
from node_produk import NodeProduk


class HashTable:
    def __init__(self, kapasitas=8):
        self.kapasitas = kapasitas
        self.tabel = [None] * kapasitas
        self.jumlah_data = 0
        self.load_factor = 0
        self.batas_load_factor = 0.75

    # Menghitung indeks berdasarkan ID produk
    def hash(self, id_produk):
        hasil = 0

        for karakter in str(id_produk):
            hasil = (hasil * 31 + ord(karakter)) % self.kapasitas

        return hasil

    # Memperbarui load factor
    def perbarui_load_factor(self):
        self.load_factor = self.jumlah_data / self.kapasitas

    # Menambahkan produk
    def insert(self, produk):

        # Mencegah ID produk ganda
        if self.search(produk.id_produk) is not None:
            return False

        indeks = self.hash(produk.id_produk)

        node_baru = NodeProduk(produk)
        node_baru.set_next(self.tabel[indeks])

        self.tabel[indeks] = node_baru
        self.jumlah_data += 1

        self.perbarui_load_factor()

        # Memperbesar kapasitas jika terlalu penuh
        if self.load_factor > self.batas_load_factor:
            self.resize()

        return True

    # Mencari produk berdasarkan ID
    def search(self, id_produk):
        indeks = self.hash(id_produk)
        sekarang = self.tabel[indeks]

        while sekarang is not None:
            produk = sekarang.get_data()

            if produk.id_produk == str(id_produk):
                return produk

            sekarang = sekarang.get_next()

        return None

    # Menghapus produk berdasarkan ID
    def delete(self, id_produk):
        indeks = self.hash(id_produk)

        sekarang = self.tabel[indeks]
        sebelumnya = None

        while sekarang is not None:

            produk = sekarang.get_data()

            if produk.id_produk == str(id_produk):

                if sebelumnya is None:
                    self.tabel[indeks] = sekarang.get_next()
                else:
                    sebelumnya.set_next(sekarang.get_next())

                self.jumlah_data -= 1
                self.perbarui_load_factor()

                return True

            sebelumnya = sekarang
            sekarang = sekarang.get_next()

        return False

    # Memperbesar ukuran tabel
    def resize(self):
        tabel_lama = self.tabel

        self.kapasitas *= 2
        self.tabel = [None] * self.kapasitas
        self.jumlah_data = 0

        for kepala in tabel_lama:
            sekarang = kepala

            while sekarang is not None:
                produk = sekarang.get_data()

                indeks = self.hash(produk.id_produk)

                node_baru = NodeProduk(produk)
                node_baru.set_next(self.tabel[indeks])
                self.tabel[indeks] = node_baru

                self.jumlah_data += 1
                sekarang = sekarang.get_next()

        self.perbarui_load_factor()

    # Menghitung jumlah produk
    def ukuran(self):
        return self.jumlah_data
