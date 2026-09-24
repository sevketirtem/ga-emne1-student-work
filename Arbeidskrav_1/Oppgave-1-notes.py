#Oppgave 1 - Grunnleggende programflyt: Variables, data types, operators, input, def functions, parameters,lists, tuples conditions,return_values, default_parameters comparisons, for_while_if_else_loops,

def print_error(message, prefix="Error: "):
    print(f"{prefix}{message}")
#Helper: error-printing function - a DEFAULT PARAMETER example. Yardimci: hata mesaji yazdirma fonksiyonu - DEFAULT PARAMETER ornegi
# prefix parametresine varsayilan bir deger verildi, bu yuzden fonksiyon cogu yerde argumansiz cagrilabilir; istenirse uzerine yazdirilabilir de.
print("\n---\n")
#Helper function: checks whether a text is a valid interger number.
def is_valid_integer(text):
    if text == "":
        return False
    #Splitt off a leading "-" to allow negative numbers.
    if text[0]=="-":
        digits_part = text[1:]
    else:
        digits_part = text

    if digits_part =="":
        return False
#UNIcode/ASCII ya gore alphabets > digits (0-9)
    for character in digits_part:
        if character < "0" or character > "9":
            return False
#return yerine break kullanabilirdim ama break koyduğumda, döngüden çıkılır ama kod akışı fonksiyonun içinde devam eder — döngüden sonraki satıra geçer (burada bu, en alttaki return True). Bu yüzden break kullandığında hep True alıyorsun; return False çağrılmadığı için.
#return fonksiyonu anında ve tamamen sonlandırır, döngüyü de içinde bulunduğu her şeyi de terk eder ve çağrı yapılan yere o değeri geri gönderir.Bu yüzden bu fonksiyonda break değil return False doğru seçim, çünkü geçersiz bir karakter bulduğumuz an hem döngüden hem fonksiyondan tamamen çıkmak istiyoruz.
    return True

print(is_valid_integer("abc"))
print(is_valid_integer(""))
print(is_valid_integer("0")) #Kural: harf ve rakam karsilastirilirken her karaktere bir kod verilir, buna UNICODE/ASCII denir. RAKAMLARIN KODU, HARFLERIN KODUNDAN DAHA DUSUKTUR.Yani "a" > "9" ifadesi True"dur. !!!!
print(is_valid_integer("-3"))
print(is_valid_integer("45"))





print("\n---\n")
#Oppgave_1_1_beregn_tidsbruk  - Calculate the time used
#Asks the user for a positive integer. First checks the text with "is_valid_integer" and only converts it with int() once it is valid.

def get_positive_integer(prompt):
    valid = False
    value = 0

    while not valid:
        text = input(prompt)

        if is_valid_integer(text):
            value = int(text)

            if value > 0:
                valid = True
            else:
                print_error("The number must be positive (greater than 0). Try again.")
        else:
            print_error("Invalid input. Please enter a whole number.")
    return value

print(is_valid_integer("abc"))
print(is_valid_integer(""))
print(is_valid_integer("0"))
print(is_valid_integer("-3"))
print(is_valid_integer("45"))





def beregn_tidsbruk():
    print("\n--- Beregn tidsbruk ---")

    number_of_studies = get_positive_integer("Enter the number of the studies:  ")
    length_of_each_study = get_positive_integer("Enter the length of each study in minutes: ")

    hour_total_time_used = (number_of_studies * length_of_each_study) // 60
    minutes_total_time_used = (number_of_studies * length_of_each_study) % 60
    total_time_used = (f"{hour_total_time_used } hours and {minutes_total_time_used} minutes")
    print(f"Samlet tidsbrukt : {total_time_used}")


print("\n---\n")
valid=False
print(not valid)

valid = True
print(not valid)

print("\n---\n")
valid = False
value = 0
while not valid:
    print("Donguye girdim")
    text = input("Bir sey yaz: ")
    break