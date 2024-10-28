class Ramada_PLaza:

    def __init__(self,müsteri_tipi,kapasite,oda_tipi,oda_sayisi,müsteri_sayisi,ad,TC):
        self.müsteri_tipi = müsteri_tipi
        self.kapasite = kapasite
        self.oda_tipi = oda_tipi
        self.oda_sayisi = oda_sayisi
        self.müsteri_sayisi = müsteri_sayisi
        self.ad = ad
        self.TC = TC

    def dolu_mu(self,oda_numarasi):
      if oda_numarasi == 0 :
        return True

    def oda_rezarvasyon(self,oda_numarasi):
       if self.dolu_mu(oda_numarasi) :
          print("bos odamiz bulunmamamktadir")
       
       else: 
            print("oda rezarvasyonu basarili")
            return -1
    
    def oda(self,oda_tipi,kat_numatasi): 

        #  ikili_yatak = [[1,2],[3,4,5,6],[7,8,9]]  burda kat numarısıan göre bakıyoruz ve eğer o katta boş oylmayan er varsa ilk bulduğumuza atıyoruz
       
        döngü = -1
        for oda in oda_tipi[kat_numatasi]:
            döngü += 1 
            if oda != 0 :
                return döngü
        return -1

    def lokanta_rezarvasyon(self,TC,TC_listesi,lokanta_masa):

        if lokanta_masa == 0 :
            print("bos masa yok")

        else:

            for musteri in TC_listesi:
                if musteri == TC :
                    print("masa rezarvasyonu basarili")
                    return lokanta_masa - 1

            print("masa rezarvasyon basarisiz") # basarisiz olması için müsterinin kayıt olamamış olmasıgerekmekte
                
    def müsteri_kayit(self,TC,TC_listesi):

        for müsteri in TC_listesi:
            if müsteri == TC:
                return -1
            else: 
                return +1 
            
    def havuz_rezervasyon(self,TC,TC_listesi,havuz_doluluk):

        if havuz_doluluk >= 10:
            print("maalesef havuzumuz dolu ")
            return havuz_doluluk
        
        else:
            for musteri in TC_listesi:
                if musteri == TC:
                    print("havuz rezarvasyonu basarili")
                    return havuz_doluluk +1 

            print("havuz rezerve basarisiz") # basarisiz olması için müsterinin kayıt olamamış olması gerekmekte
    
    def fatura(self,müsteri_tipi,oda_tipi,gün_sayisi,normal_müsteri,
               calisan_müsteri,TC_listesi,TC,calisan_liste,ad):

        for müsteri in TC_listesi:
            if müsteri == TC:

                fiyat = 0 

                if müsteri_tipi == "normal" :
                    if  oda_tipi == "kral_dairesi":
                        fiyat = normal_müsteri[2]
                    elif oda_tipi == "üclü_yatak":
                        fiyat = normal_müsteri[1]
                    elif oda_tipi == "ikili_yatak" :
                        fiyat = normal_müsteri[0]
                

                elif müsteri_tipi == "calisan" :
                    if self.calisan_kontrol(calisan_liste,ad):
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
                
                return fiyat,müsteri_tipi
        return -1
    
    def calisan_kontrol(self,calisan_liste,ad):

        for sözlük in calisan_liste:
            for kontrol in sözlük:
                if kontrol == ad:
                    return True
        return False
               
    def lokanta_rezerve_iptal(self,TC,lokanta_rezerve,lokanta_masa):

        for musteri in lokanta_rezerve:
            if musteri == TC:
                lokanta_rezerve.remove(TC)
                lokanta_masa +=1
                
                return lokanta_masa
        return -1 

    def havuz_rezerve_iptal(self,TC,havuz_rezerve,havuz_doluluk):

        for musteri in havuz_rezerve:

            if musteri == TC :
                havuz_rezerve.remove(TC)
                havuz_doluluk +=1
                return havuz_doluluk
        return -1 
    
    def TC_kontrol(self,TC):

        if len(TC) != 11:
            print("lütfen 11 haneli bir değer giriniz")
            return True
        
        if TC.isdigit() == False:
            print("lütfen  sadece rakam giriniz")
            return True
        
    def kayit(self,TC,TC_listesi,oda_tipi,müsteri_sayisi,oda_index,ikili_yatak,
              üclü_yatak,kral_dairesi,kat_numarasi,müsteri_listesi,ad):
            
            if self.TC_kontrol(TC):
                return
            
            elif self.müsteri_kayit(TC,TC_listesi) == -1 :
                print("müsteri zaten kayitli")

            else:

                if oda_tipi == "ikili_yatak" : # oda dipine göre kontrol 

                    if müsteri_sayisi >2 :
                        print("oda kapasitesinden fazla giriş yapmaya çalisiyorusunuz")

                    if müsteri_sayisi <=2 :
                        oda_index = self.oda(ikili_yatak,kat_numarasi)   

                    if self.oda_rezarvasyon(ikili_yatak[kat_numarasi][oda_index]) == -1 : # 

                        müsteri_listesi[TC] = ad

                        TC_listesi.append(TC)

                        return [oda_index,müsteri_listesi,TC_listesi]

                elif oda_tipi == "üclü_yatak" : 

                    if  müsteri_sayisi >3 :
                        print("oda kapasitesinden fazla giriş yapmaya çalisiyorusunuz")

                    if müsteri_sayisi <=3:
                        oda_index = self.oda(üclü_yatak,kat_numarasi)

                    if self.oda_rezarvasyon(üclü_yatak[kat_numarasi][oda_index]) == -1 : # kral_dairesi = [[0],[0],[1,2,3,]]

                        müsteri_listesi[TC] = ad

                        TC_listesi.append(self.TC)

                        return [oda_index,müsteri_listesi,TC_listesi]
                    
                elif oda_tipi == "kral_dairesi" :

                    if müsteri_sayisi >3 :
                        print("oda kapasitesinden fazla giriş yapmaya çalisiyorusunuz")

                    if müsteri_sayisi <=3:
                        oda_index = self.oda(kral_dairesi,kat_numarasi)

                        if self.oda_rezarvasyon(kral_dairesi[kat_numarasi][oda_index]) == -1:

                            müsteri_listesi[TC] = ad

                            TC_listesi.append(TC)

                            return [oda_index,müsteri_listesi,TC_listesi]
                    


class müsteri_bilgileri:

    def __init__(self,ad,oda_tipi,kat_numarasi,gün_sayisi,müsteri_sayisi,müsteri_tipi,TC,oda_numarasi):
        self.ad = ad
        self.oda_tipi = oda_tipi
        self.kat_numarasi = kat_numarasi
        self.gün_sayisi = gün_sayisi
        self.müsteri_sayisi = müsteri_sayisi
        self.müsteri_tipi = müsteri_tipi
        self.TC = TC  # GENEL KONTROL ARTIK TC İLE YAPILACAK
        self.oda_numarasi = oda_numarasi
    
    def bilgiler(self):

        if self.oda_numarasi == -1:
            print("önce kayıt yapmanız gerekmektedir")
        
        else:

            print(f"Müşteri Adı: {self.ad}\n"
                    f"Oda Tipi: {self.oda_tipi}\n"
                    f"Kat Numarası: {self.kat_numarasi}\n"
                    f"Oda Numarası: {self.oda_numarasi}\n"
                    f"Kullanıcı TC: {self.TC}\n"
                    f"Gün Sayısı: {self.gün_sayisi}\n"
                    f"Müşteri Sayısı: {self.müsteri_sayisi}\n"
                    f"Müşteri Tipi: {self.müsteri_tipi}")

 
class Ramada_Altin(Ramada_PLaza):

    # müsteri_bilgi = [["hulusi demir","kat numarasi","oda numarasi","oda tipi","id"]]

    TC_listesi = []

    oda_numarasi = -1

    havuz_rezerve = []

    lokanta_rezerve = []

    ödenecek_tutar = 0 # suanlık kişi bazlı olmasını planlıyorum 

    normal_müsteri = [2500,3500,6500] # normal bir müsteri kayıt olmak istediğinde bu fiyatı ödeyecek   (BUNLAR GÜNLÜK TUTAR)

    # index0 = ikili_yatak / index1 = üclü_yatak  / index2 = kral_dairesi

    calisan_müsteri = [1500,2000,6500] # çalısan yakını veya çalışan bir müşteri bu fiyatı ödeyecek (BUNLAR GÜNLÜK TUTAR)

    # index0 = ikili_yatak / index1 = üclü_yatak  / index2 = kral_dairesi

    calisan_liste =  [{"Ali Yılmaz":" 49279929506" , "Ayşe Kara" :"10303854194" , "Ahmet Demir":"55453320984"}
                      ,{"Zeynep Çelik":"87539683942", "Mehmet Yıldız":"63487662338", "Elif Aydın":"18937137638"}
                      ,{"Cem Şahin":"74676617442", "Fatma Öz":"79473205984", "Can Kurt":"28104801330"}]
    # ali (calisan) , ayse ahmet (alin yakınları)

    müsteri_listesi = {} # normal müsteri listesi

    havuz_doluluk = 0 # havuz da aktif olarak kaç kişi olduğu yazıyor 

    lokanta_masa = 2 # lokonta da kaç masa müsait onu yazıyor

    oda_index = 0 # hangi odanın kaçınçı indexte olduğunu söylüyor ona göre kullanıcı girdi yapıyor

    ikili_yatak = [[1,2],[3,4,5,6],[7,8,9]]  # burda ikili yatak aslında kat numarası ve listenin içindeki indexe göre kaç tane oda olduğunu söylüyor

    üclü_yatak = [[1],[2,3,4],[5,6]]

    kral_dairesi = [[0],[0],[1,2,3]]  # üc kisilik olacak fakat daha büyük olacak  (0 ya dolu ya da o katta oda yok anlamaına geliyor)


    # kapasite = ikili_yatak * 2 + üclü_yatak * 3 + kral_dairesi * 3  # odanın tüm kapasitesi
   
    def __init__(self,müsteri_tipi,oda_tipi,müsteri_sayisi,ad,kat_numarasi,gün_sayisi,TC):

        self.kat_numarasi = kat_numarasi
        self.müsteri_sayisi = müsteri_sayisi
        self.ad = ad
        self.oda_tipi = oda_tipi
        self.müsteri_tipi = müsteri_tipi
        self.gün_sayisi = gün_sayisi
        self.TC = TC

    def kayit_ekle(self):

        if self.oda_tipi == "ikili_yatak":

            liste = Ramada_PLaza.kayit(self,self.TC,self.TC_listesi,self.oda_tipi,self.müsteri_sayisi,
                            self.oda_index,self.ikili_yatak,self.üclü_yatak,self.kral_dairesi,
                            self.kat_numarasi,self.müsteri_listesi,self.ad)
            
            liste[0] = self.oda_index
            liste[1] = self.müsteri_listesi
            liste[2] = self.TC_listesi

            self.oda_numarasi = self.ikili_yatak[self.kat_numarasi][self.oda_index]
    
            self.ikili_yatak[self.kat_numarasi][self.oda_index] = 0 

        elif self.oda_tipi == "üclü_yatak":

            liste = Ramada_PLaza.kayit(self,self.TC,self.TC_listesi,self.oda_tipi,self.müsteri_sayisi,
                            self.oda_index,self.ikili_yatak,self.üclü_yatak,self.kral_dairesi,
                            self.kat_numarasi,self.müsteri_listesi,self.ad)
            
            liste[0] = self.oda_index
            liste[1] = self.müsteri_listesi
            liste[2] = self.TC_listesi

            self.oda_numarasi = self.üclü_yatak[self.kat_numarasi][self.oda_index]

            self.üclü_yatak[self.kat_numarasi][self.oda_index] = 0 
        
        elif self.oda_tipi == "kral_dairesi":

            liste = Ramada_PLaza.kayit(self,self.TC,self.TC_listesi,self.oda_tipi,self.müsteri_sayisi,
                            self.oda_index,self.ikili_yatak,self.üclü_yatak,self.kral_dairesi,
                            self.kat_numarasi,self.müsteri_listesi,self.ad)
            
            liste[0] = self.oda_index
            liste[1] = self.müsteri_listesi
            liste[2] = self.TC_listesi

            self.oda_numarasi = self.kral_dairesi[self.kat_numarasi][self.oda_index]

            self.kral_dairesi[self.kat_numarasi][self.oda_index] = 0

    def lokanta_rezarvasyon(self):

        self.lokanta_masa = Ramada_PLaza.lokanta_rezarvasyon(self,self.TC,self.TC_listesi,self.lokanta_masa)

        self.lokanta_rezerve.append(self.TC)

    def havuz_rezarvasyon(self):

        self.havuz_doluluk = Ramada_PLaza.havuz_rezervasyon(self,self.TC,self.TC_listesi,self.havuz_doluluk)

        self.havuz_rezerve.append(self.TC)

    def MüsteriListesi_yazdir(self):
        print("Müsteri listesi: ", self.müsteri_listesi)


    def bilgiler(self):

        # def __init__(self,ad,oda_tipi,kat_numarasi,gün_sayisi,müsteri_sayisi,müsteri_tipi,TC):

        musteri = müsteri_bilgileri(self.ad,self.oda_tipi,self.kat_numarasi,
                                    self.gün_sayisi,self.müsteri_sayisi,
                                    self.müsteri_tipi,self.TC,self.oda_numarasi) 

        musteri.bilgiler()

    def fatura(self):

        self.ödenecek_tutar,self.müsteri_tipi = Ramada_PLaza.fatura(self,self.müsteri_tipi,self.oda_tipi,
                                                  self.gün_sayisi,self.normal_müsteri,
                                                  self.calisan_müsteri,self.TC_listesi,
                                                  self.TC,self.calisan_liste,self.ad)

        if self.ödenecek_tutar == -1:
            print("müsteri kayitli degil")
        
        else:
        
            print(f"sayin {self.ad} ödenemiz gereken tutar {self.ödenecek_tutar}" )

    def lokanta_rezerve_iptal(self):
        
        if Ramada_PLaza.lokanta_rezerve_iptal(self,self.TC,self.lokanta_rezerve,self.lokanta_masa) == -1:
            print("lokanta rezerve bulunamadi")
        else: 
            self.lokanta_masa = Ramada_PLaza.lokanta_rezerve_iptal(self,self.TC,self.lokanta_rezerve,self.lokanta_masa)
            print("lokanta rezerve iptal edildi")

    def havuz_rezerve_iptal(self):

        if Ramada_PLaza.havuz_rezerve_iptal(self,self.TC,self.havuz_rezerve,self.havuz_doluluk) == -1:
            print("havuz rezerve bulunamadi")

        else:
            self.havuz_doluluk = Ramada_PLaza.havuz_rezerve_iptal(self,self.TC,self.havuz_rezerve,self.havuz_doluluk)
            print("havuz rezerve iptal edildi")

    def kayit_sil(self): 

        # yapmamaız gereken sey odayı boşaltmak dolu oda 0 oluyor biz onu tekrardan oda numarasına çevirmemiz gerek 

        # müsteri listesinden ad silmemiz gerek 

        # bunun için de ad ile müsteri listesini kontrol edeçeğiz

        kontrol = -1

   
        for müsteri in self.TC_listesi:

            if müsteri == self.TC:

                kontrol = 0 

                musteri = müsteri_bilgileri(self.ad,self.oda_tipi,self.kat_numarasi,
                                            self.gün_sayisi,self.müsteri_sayisi,
                                            self.müsteri_tipi,self.TC,self.oda_numarasi) 
                
                if musteri.oda_tipi == "ikili_yatak":
                    self.ikili_yatak[self.kat_numarasi][self.oda_index] = self.oda_numarasi

                elif musteri.oda_tipi == "üclü_yatak":
                    self.üclü_yatak[musteri.kat_numarasi][self.oda_index] = musteri.oda_numarasi
                    
                elif musteri.oda_tipi == "kral_dairesi":
                    self.kral_dairesi[musteri.kat_numarasi][self.oda_index] = musteri.oda_numarasi

                Ramada_PLaza.havuz_rezerve_iptal(self,self.TC,self.havuz_rezerve,self.havuz_doluluk)
                Ramada_PLaza.lokanta_rezerve_iptal(self,self.TC,self.lokanta_rezerve,self.lokanta_masa)

                self.TC_listesi.remove(self.TC)
                del self.müsteri_listesi[self.TC]

                print("kayit silme işlemi başarili")

        if kontrol == -1:
            print("kayit silme işlemi başarisiz")

    # def __init__(self,müsteri_tipi,oda_tipi,müsteri_sayisi,ad,kat_numarasi,gün_sayisi,TC):


deneme = Ramada_Altin("calisan","ikili_yatak",2,"Zeynep Çelik",2,3,"34578945234")
deneme1 = Ramada_Altin("normal","üclü_yatak",2,"emirhan beyaz",2,3,"54820371946")
deneme2 = Ramada_Altin("normal","kral_dairesi",2,"hulusi demir",2,1,"27964583108")

deneme.kayit_ekle()
deneme1.kayit_ekle()
deneme2.kayit_ekle()


deneme.havuz_rezarvasyon()

deneme.lokanta_rezarvasyon()

deneme.bilgiler()

deneme.fatura()

deneme.havuz_rezerve_iptal()

deneme.lokanta_rezerve_iptal()

deneme.MüsteriListesi_yazdir()

deneme.kayit_sil()
deneme1.kayit_sil()
deneme2.kayit_sil()


