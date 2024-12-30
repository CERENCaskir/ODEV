# Öğrenci verilerini saklamak için bir sözlük kullanıyoruz
ogrenciler = {}

# Menü seçeneklerini gösteren fonksiyon
def menu():
    print("1. Öğrenci Ekle")
    print("2. Öğrencileri Listele")
    print("3. Not Analizi Yap")
    print("4. Çıkış")

# Öğrenci ekleme fonksiyonu
def ogrenci_ekle():
    ogrenci_no = input("Öğrenci numarasını girin: ")
    ad_soyad = input("Öğrencinin adını ve soyadını girin: ")
    notu = float(input("Öğrencinin notunu girin: "))
    ogrenciler[ogrenci_no] = {'ad_soyad': ad_soyad, 'not': notu}
    print("Öğrenci eklendi.\n")

# Öğrencileri listeleme fonksiyonu
def ogrencileri_listele():
    for ogrenci_no, bilgiler in ogrenciler.items():
        print(f"Öğrenci No: {ogrenci_no}, Ad Soyad: {bilgiler['ad_soyad']}, Not: {bilgiler['not']}")
    print("\n")

# Not analizi fonksiyonu
def not_analizi():
    if not ogrenciler:
        print("Öğrenci listesi boş.\n")
        return
    
    notlar = [bilgiler['not'] for bilgiler in ogrenciler.values()]
    ortalama = sum(notlar) / len(notlar)
    en_yuksek = max(notlar)
    en_dusuk = min(notlar)
    
    print(f"Ortalama Not: {ortalama:.2f}")
    print(f"En Yüksek Not: {en_yuksek:.2f}")
    print(f"En Düşük Not: {en_dusuk:.2f}")
    print("\n")

# Ana döngü
while True:
    menu()
    secim = input("Bir seçenek seçin (1-4): ")
    
    if secim == '1':
        ogrenci_ekle()
    elif secim == '2':
        ogrencileri_listele()
    elif secim == '3':
        not_analizi()
    elif secim == '4':
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz seçenek, lütfen tekrar deneyin.\n")
