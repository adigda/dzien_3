

# 1. czy liczba jest podzielna przez 3 lub 5 lub 7
number = int(input('Podaj liczbę'))
if number % 3 == 0:
    print (number, 'jest podzielna przez 3')
elif number % 5 == 0:
    print (number, ' jest podzielna przez 5')
elif number % 7 == 0:
    print (number, ' jest podzielna przez 7')
else:
    print (number, ' nie jest podzielna przez 3, 5 i 7')





#######################################################################################
# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

year = int(input('Podaj rok'))
if year % 4 == 0:
    print ('Rok przestępny')
else:
    print ('Rok nie przestępny')



#########################################################################################
# 3. oblicz ocenę na podstawie progu procentowego
procent = float(input('Podaj procent'))
if procent < 30.0:
    print('Nie zdałeś. Pałka!')
elif procent < 60.0:
    print ('Nie najgorzej 3')
else:
    print ('Brawo 4! Na 5 i tak nie zasługujesz')



###########################################################################################
# 4. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu
month_31 = ['styczeń', 'marzec', 'maj', 'lipiec', 'sierpień', 'październik', 'grudzień']
month_30 = ['kwiecień', 'czerwiec', 'wrzesień', 'listopad']
luty = ['luty']

month = input('Podaj miesiąc')
if month in month_31:
    print(month, 'ma 31 dni')
elif month in month_30:
    print (month, 'ma 30 dni')
else:
    print ('Luty ma 28 dni, choć czasami 29')
print('Koniec sprawdzania ilości dni w miesiącu')
############################################################################################
# 5. inupt - miesiąc oraz dzien (np. mar-18),
#   okreslic pore roku

wiosna = ['marzec', 'kwiecień', 'maj', 'czerwiec']
lato = ['lipiec', 'sierpień', 'wrzesień']
jesien = ['pażdziernik', 'listopad', 'grudzień']
zima = ['styczeń', 'luty']

month = input('Wpisz miesiąc')
day = int(input ('Wpisz dzien miesiąca'))
if month in wiosna:
    print('Chyba wiosna')
    if month == wiosna[0]:
        if day < 22:
            print ('Wiosna!')
    if month == wiosna[4]:
        if day < 23:
            print ('Wiosna!')
        else:
            print ('A jednak to lato')

elif month in lato:
    print ('Chyba lato')
    if month == lato[2]:
        if day < 24:
            print ('Lato')
        else:
            print ('Jesień')
elif month in jesien:
    print ('Chyba jesień')
    if month == jesien[2]:
        if day < 23:
            print ('Jesień')
        else:
            print('To już jesień')
else:
    print ('Chyba zima')
###########################################################################################
# 6. ruletka: otrzymawszy liczbę, sprawdź czy jest ona (np. 17R, 2B):
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

liczba = input('Podaj ruletke: \n')
if liczba [-1] == "R":
    print ('Brawo, czerwień')
else:
    print ('O czarny')
cyfra = liczba[:-2]
cyfra = int(cyfra)
if cyfra >= 18:
    print (cyfra, 'to wysoka liczba')
else:
    print ('troche niska liczba')
print('Sprawdfzamy, czy parzysta:')
if cyfra % 2 == 0:
    print (' liczba parzysta')
else:
    print ('liczba nieparzysta')




###################################################################################
# 7. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32
print()
print('A teraz skonwertujemy temperaturę')
print ('W jakich stopniach podajesz temperaturę?\n W C czy w F?')
jednostka = input ('Podaje literę')
temp = float(input ('Podaj tempetartuę w stopniach:\n'))
if jednostka == 'F':
    celcjusz = ((temp - 32) * (5/9))
    print (celcjusz)
else:
    fahrenheit = (temp * (9/5) + 32)
    print (fahrenheit)


########################################################################################
# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny
bok_1 = float (input ('Podaj pierwszy bok'))
bok_2 = float (input ('Podaj drugi bok'))
bok_3 = float (input ('Podaj trzeci bok'))
lista = [bok_1, bok_2, bok_3]
if max(lista) == bok_1:
    if (bok_2 + bok_3) > bok_1:
        print('Zbudujesz trojkąt')
    else:
        print ('Nie zbudujesz trojkata')
elif max(lista) == bok_2:
    if (bok_1 + bok_3) > bok_2:
        print('Zbudujesz trojkąt')
    else:
        print ('Nie zbudujesz trojkata')
elif max(lista) == bok_3:
    if (bok_2 + bok_1) > bok_3:
        print('Zbudujesz trojkąt')
    else:
        print ('Nie zbudujesz trojkata')

print ('Koniec')





