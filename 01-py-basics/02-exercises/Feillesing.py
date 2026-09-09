#feillesing

number_1 = int(input("enter number_1 = "))
number_2 = int(input("enter number_2 = "))
#DRY = Dont repeat yourself

total = number_1 + number_2

print(f"Total: {total}")

#1 Hata türü: SyntaxError (unterminated string literal) Neden: Tırnak işareti eksikti, string kapatılmamıştı Düzeltme: Eksik tırnak işaretini ekledim
#2 Hata türü: NameError (name 'sonuc' is not defined) Neden: Var olmayan bir değişken adı kullanıldı Düzeltme: sonuc'u tanımlı bir değişkenle değiştirdim (ya da tanımladım)
#3 ata türü: TypeError (can only concatenate str to str) Neden: String ile int'i tip dönüşümü yapmadan toplamaya çalıştım Düzeltme: int() ile tip dönüşümü ekledim