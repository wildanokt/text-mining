import re
import csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def cleaning(doc):    
    #regex: menghilangkan selain huruf dan spasi
    return re.compile('[^a-zA-Z ]').sub('',doc)

def case_folding(doc):
    return doc.lower()

def tokenisasi(doc):
    return doc.split()

#stoplist
with open('stoplist.csv', mode='r') as file:
        read = csv.reader(file)
        stoplist = list(read)
#dilakukan proses ini karena hasil baca csv menghasilkan karakter [, ], dan"
stopword = tokenisasi(cleaning(" ".join(str(x) for x in stoplist)))

def filtering(arr_doc):
    return [x for x in arr_doc if x not in stopword]
    
def stemming(arr_doc):
    text = " ".join(str(x) for x in arr_doc)
    return tokenisasi(StemmerFactory().create_stemmer().stem(text))

#sample        
tex = """
    Polusi udara di Jakarta tampaknya tidak berpengaruh dengan gerakan hari bebas kendaraan atau hari bebas kendaraan yang diadakan setiap hari Minggu. Gerakan ini dimulai pada pukul 06.00 sampai 11.00. Beberapa ruas jalanan di Jakarta memberlakukan gerakan ini, mulai dari kawasan pusat Jakarta di Bundaran HI, hingga kawasan Jakarta Barat, Jakarta Pusat, Jakarta Timur, Jakarta Selatan hingga Jakarta Utara.
"""
prs = filtering(tokenisasi(case_folding(cleaning(tex))))
print(stemming(prs))