__author__ = 'dyju'

Wynik=[1,2]

for i in range (2,100):
    Wynik.append(Wynik[i-1]+Wynik[i-2])
    if Wynik[i]<4000000:
        print(Wynik[i])