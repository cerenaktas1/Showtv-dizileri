import requests
from bs4 import BeautifulSoup

# Veri toplanacak web sayfasının URL'si
url = 'https://www.showtv.com.tr/diziler'

# Web sayfasını almak için GET isteği yapılır
response = requests.get(url)

# Web sayfasının içeriği BeautifulSoup ile parse edilir
soup = BeautifulSoup(response.text, 'html.parser')

# Tüm metin içeriği alınır
tum_metin = soup.get_text()

# Metni satır bazında böler
satirlar = tum_metin.splitlines()

# Dizi adlarını içeren satırları bul
dizi_adlari = [satir.strip() for satir in satirlar if satir.strip() != '']

# Her dizi adını ekrana yazdır
for dizi_adı in dizi_adlari:
    print(dizi_adı)
