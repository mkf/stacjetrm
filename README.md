stacjetrm
=========

Skrypcik do liczby rowerów na stacjach trm24.pl

Składnia:
./demon.sh [tryb pracy] [tryb debugu] [tryb zapisu] [plik zapisu]

nie należy pisać kolejnego prarmetru bez napisania pierwszego! 
jeżeli chcemy wybrać domyślny parametr, wiedzmy jaki on jest!

tryby pracy:
    
    l
        [domyślnie] w celu interfejsu pełnego z przedzieleniem na pętli, dla oczu ludzkich
    u
        w celu interfejsu pełnego ciągłego, dla oczu ludzkich
    p
        w celu interfejsu dla programu, sensownego do zapisu z command line'a 
    c
        w celu zapisu maksymalnie zminimalizowanego, tj. "[czasUNIX],[jednolubdwucyfrowynrstacji],[liczbarowerów]
    m
        w celu zapisu minimalnego, jeszcze nie wiem jakiego dokładnie
    n
        w celu braku wypisywania danych do terminala, niepolecane, jeszcze nie istnieje
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

    c
        w celu zapisu do pliku csv, jeszcze nie istnieje
    n
        w celu braku zapisu, tylko standard output, jeszcze nie istnieje
    s
        w celu zapisu do bazy MySQL(?) jeszcze nie istnieje
    

plik zapisu:
    
    ten parametr równiez jeszcze nie istnieje
