stacjetrm
=========

Skrypcik do liczby rowerów na stacjach trm24.pl

Składnia:
./demon.sh [tryb pracy] [tryb debugu] [tryb zapisu] [plik zapisu]

nie należy pisać kolejnego prarmetru bez napisania pierwszego! 
jeżeli chcemy wybrać domyślny parametr, wiedzmy jaki on jest!

tryby pracy:
    
    l
        [domyślnie] w celu interfejsu pełnego, ale dla oczu ludzkich
    u
        w celu interfejsu bez debuga, dla oczu ludzkich
    p
        w celu interfejsu dla programu, sensownego do zapisu z command line'a 
    c
        w celu zapisu maksymalnie zminimalizowanego, tj. "[czasUNIX],[jednolubdwucyfrowynrstacji],[liczbarowerów]
    m
        w celu zapisu minimalnego, jeszcze nie wiem jakiego dokładnie
    d
        USTAWIENIE DOMYSLNE
tryby debugu:
    
    f
        w celu full debuga
    y
        w celu debuga delikatnego
    n
        bez debuga
    d
        USTAWIENIE DOMYSLNE
tryby zapisu:

    jeszcze nieustalone

plik zapisu:
    
    jeszcze nawet zapisu nie zrobiłem
