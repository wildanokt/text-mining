import re
import csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class Preprocessing:

    # Menghapus karakter non-huruf dan spasi
    def cleaning(self, doc):
        return re.compile('[^a-zA-Z ]').sub('', doc)

    # Mengubah semua huruf menjadi huruf huruf kecil
    def case_folding(self, doc):
        return doc.lower()

    # Memecah sebuah dokumen teks menjadi sekumpulan token
    def tokenisasi(self, doc):
        return doc.split()

    # Menghapus token yang terdapat pada stoplist.
    def filtering(self, arr_doc):
        # Stoplist bahasa Indonesia menggunakan metode Tala
        with open('stoplist.csv', mode='r') as file:
            read = csv.reader(file)
            stoplist = list(read)

        # Dilakukan proses ini karena hasil baca csv menghasilkan karakter [,], dan "
        stopword = self.tokenisasi(self.cleaning(" ".join(str(x) for x in stoplist)))
        return [x for x in arr_doc if x not in stopword]

    # Mengubah token menjadi stem
    def stemming(self, arr_doc):
        text = " ".join(str(x) for x in arr_doc)
        return self.tokenisasi(StemmerFactory().create_stemmer().stem(text))

    def result(self, doc):
        hasil = self.filtering(self.tokenisasi(self.case_folding(self.cleaning(doc))))
        #Membuat term dengan menghapus duplikasi dari hasil stemming
        print(list(dict.fromkeys(self.stemming(hasil))))


    