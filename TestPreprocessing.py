from Preprocessing import Preprocessing
#from Weighting import Weighting

class TestPreprocessing:
    with open('contoh-data/33-destinasi-di-toba-mulai-digarap.txt', 'r') as file:
        text = file.read()

    test = Preprocessing()
    test.result(text)
    