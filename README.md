stacjetrm
=========

*Please use last release ("Releases") instead of current source code! I will remove this warning when I'll make current source code stable and begin to commit new features to another branch "new".*

A script for getting the count of bicycles present on the trm24.pl stations.
Skrypcik do liczby rowerów na stacjach trm24.pl.

Składnia:
Syntax:
./demon.sh [czas czekania] [tryb pracy] [tryb debugu] [tryb zapisu] [plik zapisu]
./demon.sh [waiting time] [working mode] [debug mode] [write mode] [write file]


nie należy pisać kolejnego prarmetru bez napisania pierwszego! 
jeżeli chcemy wybrać domyślny parametr, wiedzmy jaki on jest!

parametry wpisywać bez pierwszych liter, tymczasowo

język:
    la
        English
    le
        Esperanto
    lp
        Polski 
    ld
        Deutsch (not ready)

czas czekania:
    t[w sekundach], np. t30
        może być 0, może być liczba sensowna, może być niewiadomo ile 
        (jedyne ograniczenie to ograniczenie komendy 'sleep' ;p), w  
        celu praktycznie jednorazowego uruchomienia
    td
      lub brak parametru czasu czekania
        w celu domyślnego ustawienia, którym domyślnie jest 60 sekund

ustawienie tymczasowego zapisu

stacje do sprawdzania:
    sw
        wszystkie stacje po kolei
     lub
    s[a-l], tj. [ sa, sb, sc, sd, se, sf, sg, sh, si, sj, sk, sl ]
	wybór stacji do sprawdzania, można wybrać 12 stacji, kolejność alfabetyczna liter, każda litera od a do l może, 
       ale nie musi, mieć wybraną stację (musi być przynajmniej jedna litera ze stacją). Działają tylko litery od a do l
       i tylko pisane małą literą. 

tryby pracy:
    
    pf             [DOMYŚLNE]
        w celu interfejsu pełnego z przedzieleniem na pętli i adresami, dla oczu ludzkich
    pl
        w celu interfejsu pełnego z przedzieleniem na pętli, dla oczu ludzkich
    pu
        w celu interfejsu pełnego ciągłego, dla oczu ludzkich
    pa
	w celu interfejsu z adresami
    pt 
        w celu interfejsu tabeli z adresami
    pk (chwilowo jeszcze p)
        w celu interfejsu dla programu, sensownego do zapisu z command line'a 
    pc
        w celu zapisu maksymalnie zminimalizowanego, tj. "[czasUNIX],[jednolubdwucyfrowynrstacji],[liczbarowerów]
    pm
        w celu zapisu minimalnego, jeszcze nie wiem jakiego dokładnie
    pn
        w celu braku wypisywania danych do terminala, niepolecane, jeszcze nie istnieje
    pd
        USTAWIENIE DOMYSLNE
tryby debugu:
    
    bf
        w celu full debuga
    by
        w celu debuga delikatnego
    bn
        bez debuga
    bd
        USTAWIENIE DOMYSLNE
tryby zapisu:

    wc
        w celu zapisu do pliku csv, jeszcze nie istnieje
    wn
        w celu braku zapisu, tylko standard output, jeszcze nie istnieje
    ws
        w celu zapisu do bazy MySQL(?) jeszcze nie istnieje
    

plik zapisu:
    
    ten parametr równiez jeszcze nie istnieje
