class Ramada_PLaza:

    def __init__(self,müsteri_tipi,kapasite,oda_tipi,oda_sayisi,müsteri_sayisi,ad):
        self.müsteri_tipi = müsteri_tipi
        self.kapasite = kapasite
        self.oda_tipi = oda_tipi
        self.oda_sayisi = oda_sayisi
        self.müsteri_sayisi = müsteri_sayisi
        self.ad = ad

    def dolu_mu(self,oda_tipi):
      if oda_tipi == 0 :
        return True

    def oda_rezarvasyon(self,oda_tipi):
       if self.dolu_mu(oda_tipi) :
          print("bos odamiz bulunmamamktadir")
       
       else: 
            print("oda rezarvasyonu basarili")
            return -1
    
    def oda(self,oda_tipi,kat_numatasi):
        döngü = -1
        for oda in oda_tipi[kat_numatasi]:
            döngü += 1 
            if oda != 0 :
                return döngü
        return -1
    
       
    def lokanta_rezarvasyon(self,ad,müsteri_listesi,lokanta_masa):

        if lokanta_masa == 0 :

            print("bos masa yok")

        else:

            for musteri in müsteri_listesi:
                if musteri == ad :
                    print("masa rezarvasyonu basarili")
                    return lokanta_masa - 1 

            print("masa rezarvasyon basarisiz")
                
    def müsteri_kayit(self,ad,müsteri_listesi):

        for müsteri in müsteri_listesi:
            if müsteri == ad :
                return -1 # müsteri kayitli demek
            else:
                return +1 # müsteri yok demek
            
    def havuz(self,ad,müsteri_listesi,havuz_doluluk):

        if havuz_doluluk >= 10:
            print("maalesef havuzumuz fazla dolu ")
            return -1 
        
        else:
            for musteri in müsteri_listesi:
                if musteri == ad :
                    print("havuz rezarvasyonu basarili")
                    return havuz_doluluk +1 

            print("havuz rezerve basarisiz")

            return havuz_doluluk

    def müsteri_bilgileri(self):
        pass
    
    def fatura(self,müsteri_tipi,oda_tipi,gün_sayisi,normal_müsteri,calisan_müsteri,müsteri_listesi,ad,calisan_liste):

        for müsteri in müsteri_listesi:
            if müsteri == ad:

                fiyat = 0 

                if müsteri_tipi == "normal" :
                    if  oda_tipi == "kral_dairesi":
                        fiyat = normal_müsteri[2]
                    elif oda_tipi == "üclü_yatak":
                        fiyat = normal_müsteri[1]
                    elif oda_tipi == "ikili_yatak" :
                        fiyat = normal_müsteri[0]
                

                elif müsteri_tipi == "calisan" :
                    if self.calisan_kontrol(ad,calisan_liste):
                        if  oda_tipi == "kral_dairesi":
                            fiyat = calisan_müsteri[2]
                        elif oda_tipi == "üclü_yatak":
                            fiyat = calisan_müsteri[1]
                        elif oda_tipi == "ikili_yatak" :
                            fiyat = calisan_müsteri[0]
                    
                    else: 
                        print("calisan yakini degilsiniz **")
                        müsteri_tipi = "normal"
                        if  oda_tipi == "kral_dairesi":
                            fiyat = normal_müsteri[2]
                        elif oda_tipi == "üclü_yatak":
                            fiyat = normal_müsteri[1]
                        elif oda_tipi == "ikili_yatak" :
                            fiyat = normal_müsteri[0]

                    fiyat = fiyat * gün_sayisi 
                
                return fiyat
        return -1
    
    def calisan_kontrol(self,ad,calisan_liste):

       for liste in calisan_liste:
            if ad in liste:
               return True
    
    def lokanta_rezerve_iptal(self,ad,lokanta_rezerve,lokanta_masa):

        for musteri in lokanta_rezerve:
            if musteri == ad:
                lokanta_rezerve.remove(ad)
                lokanta_masa +=1
                
                return lokanta_masa
        return -1 

    def havuz_rezerve_iptal(self,ad,havuz_rezerve,havuz_doluluk):

        for musteri in havuz_rezerve:

            if musteri == ad :
                havuz_rezerve.remove(ad)
                havuz_doluluk +=1
                print("havuz rezerve ipral edildi")
                return havuz_doluluk
        return -1 


class Ramada_Altin(Ramada_PLaza):

    havuz_rezerve = []

    lokanta_rezerve = []

    ödenecek_tutar = 0 # suanlık kişi bazlı olmasını planlıyorum 

    normal_müsteri = [2500,3500,6500] # normal bir müsteri kayıt olmak istediğinde bu fiyatı ödeyecek   (BUNLAR GÜNLÜK TUTAR)

    # index0 = ikili_yatak / index1 = üclü_yatak  / index2 = kral_dairesi

    calisan_müsteri = [1500,2000,6500] # çalısan yakını veya çalışan bir müşteri bu fiyatı ödeyecek (BUNLAR GÜNLÜK TUTAR)

    # index0 = ikili_yatak / index1 = üclü_yatak  / index2 = kral_dairesi

    calisan_liste =  [["Ali Yılmaz", "Ayşe Kara", "Ahmet Demir"],["Zeynep Çelik", "Mehmet Yıldız", "Elif Aydın"],["Cem Şahin", "Fatma Öz", "Can Kurt"] ]
    # ali (calisan) , ayse ahmet (alin yakınları)

    müsteri_listesi = [] # normal müsteri listesi

    havuz_doluluk = 0 # havuz da aktif olarak kaç kişi olduğu yazıyor 

    lokanta_masa = 2 # lokonta da kaç masa müsait onu yazıyor

    oda_index = 0 # hangi odanın kaçınçı indexte olduğunu söylüyor ona göre kullanıcı girdi yapıyor

    ikili_yatak = [[1,2],[3,4,5,6],[7,8,9]]  # burda ikili yatak aslında kat numarası ve listenin içindeki indexe göre kaç tane oda olduğunu söylüyor

    üclü_yatak = [[1],[2,3,4],[5,6]]

    kral_dairesi = [[0],[0],[1,2,3]]  # üc kisilik olacak fakat daha büyük olacak  (0 ya dolu ya da o katta oda yok anlamaına geliyor)


    # kapasite = ikili_yatak * 2 + üclü_yatak * 3 + kral_dairesi * 3  # odanın tüm kapasitesi
   
    def __init__(self,müsteri_tipi,oda_tipi,müsteri_sayisi,ad,kat_numarasi,gün_sayisi):

        self.kat_numarasi = kat_numarasi
        self.müsteri_sayisi = müsteri_sayisi
        self.ad = ad
        self.oda_tipi = oda_tipi
        self.müsteri_tipi = müsteri_tipi
        self.gün_sayisi = gün_sayisi

    def kayit_ekle(self):
        
        # x = Ramada_PLaza.müsteri_kayit(self,self.ad,self.müsteri_listesi)

        if Ramada_PLaza.müsteri_kayit(self,self.ad,self.müsteri_listesi) == -1 :
            print("müsteri zaten kayitli")

        else:
            self.müsteri_listesi.append(self.ad)

            if self.oda_tipi == "ikili_yatak" : # ota dipine göre kontrol 

                if self.müsteri_sayisi >2 :
                    print("oda kapasitesinden fazla giriş yapmaya çalisiyorusunuz")

                if self.müsteri_sayisi <=2 :
                    self.oda_index = Ramada_PLaza.oda(self,self.ikili_yatak,self.kat_numarasi)

                    # if (self.oda_index) == -1 :
                    #     print("bos odamiz bulunmamaktadir")

                    if Ramada_PLaza.oda_rezarvasyon(self,self.ikili_yatak[self.kat_numarasi][self.oda_index]) == -1 : # 
                        self.ikili_yatak[self.kat_numarasi][self.oda_index] = 0 # oda sayısını bir azaltıyoruz ram de ama azalıyor 
                
            elif self.oda_tipi == "üclü_yatak" :

                if self.müsteri_sayisi >3 :
                    print("oda kapasitesinden fazla giriş yapmaya çalisiyorusunuz")

                if self.müsteri_sayisi <=3:
                    self.oda_index = Ramada_PLaza.oda(self,self.üclü_yatak,self.kat_numarasi)

                    # if (self.oda_index) == -1 :
                    #     print("bos odamiz bulunmamaktadir")

                    if Ramada_PLaza.oda_rezarvasyon(self,self.üclü_yatak[self.kat_numarasi][self.oda_index]) == -1 : # kral_dairesi = [[0],[0],[1,2,3,]]
                        self.üclü_yatak[self.kat_numarasi][self.oda_index] = 0                 

            elif self.oda_tipi == "kral_dairesi" :

                if self.kat_numarasi :
                    pass

                if self.müsteri_sayisi >3 :
                    print("oda kapasitesinden fazla giriş yapmaya çalisiyorusunuz")

                if self.müsteri_sayisi <=3:
                    self.oda_index = Ramada_PLaza.oda(self,self.kral_dairesi,self.kat_numarasi)

                    # if (self.oda_index) == -1 :
                    #     print("bos odamiz bulunmamaktadir")

                    if Ramada_PLaza.oda_rezarvasyon(self,self.kral_dairesi[self.kat_numarasi][self.oda_index]) == -1:
                        self.kral_dairesi[self.kat_numarasi][self.oda_index] = 0

    
    def lokanta_rezarvasyonu(self):

        self.lokanta_masa = Ramada_PLaza.lokanta_rezarvasyon(self,self.ad,self.müsteri_listesi,self.lokanta_masa)

        self.lokanta_rezerve.append(self.ad)

    def havuz(self):

        x = Ramada_PLaza.havuz(self,self.ad,self.müsteri_listesi,self.havuz_doluluk)

        if x!= -1 :

            self.havuz_rezerve.append(self.ad)

            self.havuz_doluluk = Ramada_PLaza.havuz(self,self.ad,self.müsteri_listesi,self.havuz_doluluk)

    def müsteriListesi_yazdir(self):
        print("Müsteri listesi: ", self.müsteri_listesi)

    def fatura_yazdir(self):

        self.ödenecek_tutar = Ramada_PLaza.fatura(self,self.müsteri_tipi,self.oda_tipi,self.gün_sayisi,self.normal_müsteri,self.calisan_müsteri,self.müsteri_listesi,self.ad,self.calisan_liste)

        if self.ödenecek_tutar == -1:
            print("müsteri kayitli degil")
        
        else:
        
            print(f"sayin {self.ad} ödenemiz gereken tutar {self.ödenecek_tutar}" )

    def lokanta_rezerve_iptal(self):
        
        if self.lokanta_masa == Ramada_PLaza.lokanta_rezerve_iptal(self,self.ad,self.lokanta_rezerve,self.lokanta_masa):
            print("lokanta rezerve bulunamadi")
        else: 
            self.lokanta_masa = Ramada_PLaza.lokanta_rezerve_iptal(self,self.ad,self.lokanta_rezerve,self.lokanta_masa)
            print("lokanta rezerve iptal edildi")

    def havuz_rezerve_iptal(self):

        x = Ramada_PLaza.havuz_rezerve_iptal(self,self.ad,self.havuz_rezerve,self.havuz_doluluk)

        if x != -1 :
            self.havuz_doluluk = Ramada_PLaza.havuz_rezerve_iptal(self,self.ad,self.havuz_rezerve,self.havuz_doluluk)
        else: 
            print("havuz rezerve bulunamadi")
        
    def kayit_sil(self):

        if Ramada_PLaza.müsteri_kayit(self,self.ad,self.müsteri_listesi) == -1 :

            if self.oda_tipi == "ikili_yatak":
                pass
            elif self.oda_tipi == "üclü_yatak":
                pass
            elif self.oda_tipi == "kral_dairesi":
                pass
            pass

        else:
            print("müsteri kayitli degil")

#  def __init__(self,müsteri_tipi,oda_tipi,müsteri_sayisi,ad,kat_numarasi,gün_sayisi):
          
    
deneme = Ramada_Altin("normal","kral_dairesi",2,"hulusi demir",2,1)
deneme1 = Ramada_Altin("normal","kral_dairesi",2,"emirhan beyaz",2,3)
deneme2 = Ramada_Altin("calisan","ikili_yatak",2,"Zeynep Çelik",2,3)

# deneme2.kayit_ekle()
# deneme2.fatura_yazdir()

# deneme1.kayit_ekle()
# deneme1.müsteriListesi_yazdir()

deneme.kayit_ekle()
deneme.müsteriListesi_yazdir()

deneme.lokanta_rezarvasyonu()

deneme.havuz()

deneme.fatura_yazdir()

print("---------------")

deneme.lokanta_rezerve_iptal()

deneme.havuz_rezerve_iptal()
print("---------------")

deneme.havuz_rezerve_iptal()


'''
class müsteri:

     
    def __init__(self,müsteri_tipi,oda_tipi,müsteri_sayisi,ad,kat_numarasi):

        self.kat_numarasi = kat_numarasi
        self.müsteri_sayisi = müsteri_sayisi
        self.ad = ad
        self.oda_tipi = oda_tipi
        self.müsteri_tipi = müsteri_tipi

deneme2 = müsteri("normal","kral_dairesi",2,"hulusi demir",2) # müsteri_tipi ,oda_tipi, müsteri_sayisi, ad, kat_numarasi
'''