"""Matemaatilised tehted"""
import math

# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b



# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
a = float(input("Sisesta arv a:"))
# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
b = float(input("Sisesta arv b:"))
# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
c = math.sqrt((a ** 2) + (b ** 2))
Umbermoot = a + b + c
SemiPerimeter = Umbermoot/2
Pindala = math.sqrt(SemiPerimeter * (SemiPerimeter - a) * (SemiPerimeter - b) * (SemiPerimeter - c))

answer1 = round(c, 2)
answer2 = round(Umbermoot, 2)
answer3 = round(Pindala, 2)
print(f"Hüpotenuus on: {answer1} Ümbermõõt on: {answer2} Pindala on {answer3}")
