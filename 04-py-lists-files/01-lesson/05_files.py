from pathlib import Path
print(f"Current directory is: {Path.cwd()}")

data_directory = Path("..") / "data"
#print(data_directory)

prices_path = data_directory / "price.txt"

print(data_directory)
print(data_directory.exists())
print(f"Directory exists: {data_directory.exists()}")


print(prices_path)
print(prices_path.exists())
print(f"Prices_path exists: {prices_path.exists()}")

print("\n---\n")

with open(prices_path, "r", encoding="utf-8") as file:
    content = file.read()
#dosyanin tum icerigini tek bir uzun metin(string) olarak okur ve content degiskenine atar.
print(content)

print("\n---\n")

prices = []
with open(prices_path,"r", encoding="utf-8") as file:
#UTF-8 øæå ve sgi gibi norvec ve turk karakterlerini dogru okuyup yazabilen dunyadaki en yaygin standarttir.
    for line in file:
#.read() tum icerigi tek metin olarak verir; oyna benim her satiri ayri ayri bir sayiya cevirmem gerekiyor.
#"for line in file:" dosyayi satir satir dolasmami saglar. her turda line degiskeni o satirin metnini tutar.
#tipki "for guest in guests:" da her turda bir misafiri tutamasi gibi, ama burada liste yerine dosya satirlari geziliyor.

        price = float(line.strip())
#bir dosyadan okunan her satirin sonunda gorunmeyen bir satir sonu karakteri "\n" bulunur, bazen basinda/sonunda fazladan bosluk da olabilir.
#.strip() bunlari temizler.
        prices.append(price)
#prices.append(price) satirinda, o satirdan hesaplanan tek bir sayiyi (price degiskeni) prices listesinin sonuna ekliyoruz. Dongu her turda yeni bir satir okuyor. O satiri sayiya ceviriyor. listeye ekliyor. Dongu bitince prices listesi, dosyadaki tum sayilari iceren bir liste oluyor.
# girinti seviyesi dusunce bunu blok bitisi olarak algilar ve dosya otomatik kapanir. Boylece sistem kaynagi (file handle) tuketimi durur (acik dosya sistem kaynagi tuketir. acik kalan cok fazla dosya olursa sistem hatalari olusur.)
# with kullanmazsak file = open(prices_path,"r") content = file.read() file.coles() yazmangerekir, unutrsan dosya acik kalir.
# ama with open(......) as file: blogunu kullanirsan dosya kendisi kapanir.
print(prices)

print("\n---\n")

report_path = data_directory / "price_report.txt"

#existing content is replaced

with open(report_path, "w", encoding="utf-8") as file:
    file.write("First line\n")

# "r" oku read - dosya var olmali
# "w" uzerine yaz write dosya varsa icerigini tamamen siler ve bastan yazar, yoksa yeni olusturur.
# "a" sonuna ekle append - mevcut icerigi kuru ve sonuna yeni icerik ekler. doysa yoksa yeni olusturur.

print("\n---\n")

#Existing content kept, new content added at the end.
with open(report_path, "a", encoding="utf-8") as file:
    file.write("Another line\n")

report_line = [
    "Item: Epler",
    "Amount: 20",
    "Price: 96.50"]
with open(report_path, "a", encoding="utf-8") as file:
    for line in report_line:
        file.write(line + "\n")

with open(report_path, "a", encoding="utf-8") as file:
    file.write("Kommenta: Husk blåbær og grøt!\n")