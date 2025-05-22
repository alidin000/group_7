from calculator import koshuu
from calculator import kemituu
from calculator import koboituu
from calculator import boluu


def input_jardamchy():
    tuura_input_kirbedi = True
    while tuura_input_kirbedi:
        try:
            input_2 = int(input("tandoonu kirgiziniz:"))
            tuura_input_kirbedi = False
        except Exception as e:
            print("Tuura emes tandoo! Kaira araket kylynyz")
            tuura_input_kirbedi = True
    return input_2

import os
while True:
    os.system("cls")
    print("__Menu___")
    print("Tandanyz")
    print("1. Koshuu")
    print("2. Kemituu")
    print("3. Koboituu")
    print("4. Boluu")
    print("5. Chyguu")

    input_2 = input_jardamchy()
    
    print("________")
    if input_2 == 1:
        # a = 3
        # b = 3
        print("koshuluuchu sandy kirgiziniz:")
        a = input_jardamchy()
        print("koshuluuchu sandy kirgiziniz:")
        b = input_jardamchy()
        print(f"summasy : {koshuu(a,b)}")
    elif input_2 == 2:
        print("kemuuchu sandy kirgiziniz:")
        a = input_jardamchy()
        print("kemuuchu sandy kirgiziniz:")
        b = input_jardamchy()
        print(f"kemitindi : {kemituu(a,b)}")
    elif input_2 == 3:
        print("koboituuluuchu sandy kirgiziniz:")
        a = input_jardamchy()
        print("koboituuchu sandy kirgiziniz:")
        b = input_jardamchy()
        print(f"koboitundu : {koboituu(a,b)}")
    elif input_2 == 4:
        print("bolunuuchu sandy kirgiziniz:")
        a = input_jardamchy()
        print("boluuchu sandy kirgiziniz:")
        b = input_jardamchy()
        print(f"tiyindi : {boluu(a,b)}")
    elif input_2 == 5:
        print("Jakshy kalynyz")
        break
    else:
        print("Bizde andai tandoo jok!!!")