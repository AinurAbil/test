import datetime
import os

class Command:
    def __init__(self,dosyaismi,modu,mesaj = 'Burada yazin...'):
        self.dosyaismi = dosyaismi
        self.modu = modu
        self.mesaj = mesaj

    def yeniDosyaOlusturmak(self):
        try:
            f = open(self.dosyaismi,self.modu)
            f.write(self.mesaj)
            f.close()
        except:
            date = datetime.datetime.now()
            print('*** {}  HATA 305 ***'.format(date))

    def dosyaSilmek(self):
        try:
            os.remove(self.dosyaismi)
        except:
            print('*** {}  HATA 305  Dosya silemedik***'.format(self.dosyaismi))
    
    #for line in f:
    #if line.startswith('Dimash')