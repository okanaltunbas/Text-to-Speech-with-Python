from text_to_speech import save

metin_str = input("Lütfen seslendirmek istediğiniz metni yazın :")
dil_str = input("Dil belirleyiniz : (Örneğin tr, en)")
dosya_adi = input("Çıktı dosya adını giriniz : ")

try:
    save(metin_str, dil_str, file=f"{dosya_adi}.mp3")
    print(f"{dosya_adi}.mp3 oluşturuldu!")
except:
    print("İşlem başarısız!")
