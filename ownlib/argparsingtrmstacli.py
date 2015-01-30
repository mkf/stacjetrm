# -*- coding: utf-8 -*-
def argparsowanie(allsta,defsta,defpracy,defdebugu,defwritemode,defwaitbetweenloops,deflang,defget,defadrlangczy,defadrchar,defwvt,defwvc):
	import argparse
	argh = argparse.ArgumentParser();arglang = argh.add_mutually_exclusive_group();argchar = argh.add_mutually_exclusive_group()
	argwaitbetweenloops = argh.add_mutually_exclusive_group();argstac = argh.add_mutually_exclusive_group()
	argpracy = argh.add_mutually_exclusive_group();argdebugu = argh.add_mutually_exclusive_group()
	argzapisu = argh  # .add_mutually_exclusive_group()
	arggetu = argh.add_mutually_exclusive_group()
	# argh.add_argument("-l", "--lang", type=str, help="Jednoznakowy kod języka: \nOne-character language code: \nUnulitera lingvkodo: \n - a - English \n - e - Esperanto \n - p - Polski \n - d - Deutsch \n ")
	argchar.add_argument("-cs", "--charsafe", action="store_true",
						 help='No "unsafe" national characters in language and adresses')
	argchar.add_argument("-cn", "--charwithnational", action="store_true",
						 help='Enable "unsafe" national characters in language and adresses')
	arglang.add_argument("-la", "--langenglish", action="store_true", help="LANG: English")
	arglang.add_argument("-le", "--langesperanto", action="store_true", help="LANG: Esperanto")
	arglang.add_argument("-lp", "--langpolski", action="store_true", help="LANG: Polski")
	arglang.add_argument("-ld", "--langdeutsch", action="store_true", help="LANG: Deutsch")
	argwaitbetweenloops.add_argument(
		"-t", "--waitbetweenloops", type=int,
		help="Opóźnienie między zbieraniem danych w sekundach/Atendtempo/Delay between instances")
	argwaitbetweenloops.add_argument("-td", "--defwaitbetweenloops", action="store_true",
		help="-t z domyślną wartością/-t with default value")
	argwaitbetweenloops.add_argument("-ts", "--singlecheck", action="store_true", help="Jednorazowe sprawdzenie/Check once")
	argstac.add_argument("-sa", "--allstations", action="store_true",
		help="Wszystkie stacje/Ĉiuj biciklstacjoj/All stations")
	argstac.add_argument("-sd", "--defstations", action="store_true",
		help="Domyślne stacje/[def] biciklstacjoj/Default stations")
	argstac.add_argument("-s", "--station", type=int, action="append", choices=range(1, 14),
		help="Wybierz stację, można użyć wielokrotnie")
	# argpracy.add_argument("-pf", "--pracyfull", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i adresami")
	argpracy.add_argument("-pfc", "--pracyfulladrlangchosen", action="store_true",
		help="Interfejs pełny z przedzieleniem na pętli i w wybranym języku adresami")
	argpracy.add_argument("-pfl", "--pracyfulladrlanglocal", action="store_true",
		help="Interfejs pełny z przedzieleniem na pętli i w lokalnym(polskim) języku adresami w alfabecie polskim")
	# argpracy.add_argument("-pfle", "--pracyfulladrlanglocalenglishalphabet", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i w lokalnym(polskim) języku adresami w alfabecie angielskim")
	argpracy.add_argument("-pr", "--pracyrazem", action="store_true",
		help="Interfejs pełny tabelowy, wszystkie stacje w jednej linii")
	argpracy.add_argument("-pl", "--pracylong", action="store_true", help="Interfejs pełny z przedzieleniem na pętli")
	argpracy.add_argument("-pu", "--pracyuser", action="store_true", help="Interfejs pełny ciągły")
	# argpracy.add_argument("-pa", "--pracyadres", action="store_true", help="Interfejs pełny z adresami")
	argpracy.add_argument("-pac", "--pracyadresadrlangchosen", action="store_true",
		help="Interfejs pełny z w wybranym języku adresami")
	argpracy.add_argument("-pal", "--pracyadresadrlanglocal", action="store_true",
		help="Interfejs pełny z w lokalnym(polskim) języku adresami w alfabecie polskim")
	# argpracy.add_argument("-pale", "--pracyadresadrlanglocalenglishalphabet", action="store_true", 
	#	help="Interfejs pełny z w lokalnym(polskim) języku adresami w alfabecie angielskim")
	# argpracy.add_argument("-pt", "--pracytabela", action="store_true", help="Interfejs tabeli z adresami")
	argpracy.add_argument("-ptc", "--pracytabelaadrlangchosen", action="store_true",
		help="Interfejs tabeli z w wybranym języku adresami")
	argpracy.add_argument("-ptl", "--pracytabelaadrlanglocal", action="store_true",
		help="Interfejs tabeli z w lokalnym(polskim) języku adresami w alfabecie polskim")
	# argpracy.add_argument("-ptle", "--pracytabelaadrlanglocalenglishalphabet", action="store_true", help="Interfejs tabeli z w lokalnym(polskim) języku adresami w alfabecie angielskim")
	argpracy.add_argument("-pk", "--pracykomp", action="store_true", help="Interfejs programowy")
	argpracy.add_argument("-pc", "--pracycompressed", action="store_true",
		help="Interfejs programowy czasUNIX,jedno- lub dwu cyfrowy numer stacji, liczba rowerów")
	argpracy.add_argument("-pm", "--pracyminim", action="store_true", help="Interfejs programowy minimalistyczny")
	argpracy.add_argument("-prk", "--pracyrazkomp", action="store_true",
		help="Interfejs programowy, wszystkie stacje naraz")
	argpracy.add_argument("-pn", "--pracynone", action="store_true", help="Interfejs bez danych na stdout")
	argpracy.add_argument("-pd", "--pracydef", action="store_true", help="Opcja domyślna trybu pracy")
	argdebugu.add_argument("-bf", "--debugfull", action="store_true", help="Debug pełny")
	argdebugu.add_argument("-by", "--debugyes", action="store_true", help="Debug częściowy")
	argdebugu.add_argument("-bn", "--debugno", action="store_true", help="Debug wyłączony")
	argdebugu.add_argument("-bd", "--debugdef", action="store_true", help="Domyślne opcje debugu")
	argzapisu.add_argument("-wcks", "--writetocsvkolsinglefile", type=str, action="append",
		help="Zapis do csv (stacje kolejno, po jednej na linię - czas zapisywany dla każdego odczytu z osobna), wpisz nazwę pliku, zapis do jednego pliku ciągły")
	argzapisu.add_argument("-wcrs", "--writetocsvrazsinglefile", type=str, action="append",
		help="Zapis do csv (wszystkie stacje naraz, w jednej linii - czas zapisywany jednorazowo dla całej serii odczytów), wpisz nazwę pliku, zapis do jednego pliku ciągły")
	argzapisu.add_argument("-wckvt", "--writetocsvkolmultiwaitbetweenloopsvolumefile", action="append", type=str, nargs=2,
		help=str("Zapis do csv (stacje kolejno, po jednej na linię - czas zapisywany dla każdego odczytu z osobna), wpisz początek nazwy pliku i liczbę godzin (ta druga domyślnie %s); zapis wielowolumenowy wg czasu" % defwvt))
	argzapisu.add_argument("-wcrvt", "--writetocsvrazmultiwaitbetweenloopsvolumefile", action="append", type=str, nargs=2,
		help=str("Zapis do csv (wszystkie stacje naraz, w jednej linii - czas zapisywany jednorazowo dla całej serii odczytów), wpisz początek nazwy pliku i liczbę godzin (ta druga domyślnie %s); zapis wielowolumenowy wg czasu" % defwvt))
	# argzapisu.add_argument("-wvt", "--writemultivolumewaitbetweenloopshours", type=int, action="store_true", 
	#	help="Parametr opcjonalny zapisu wielowolumenowego: czas w godzinach na jeden plik"
	argzapisu.add_argument("-wckvc", "--writetocsvkolmulticountvolumefile", type=str, action="append", nargs=2, 
		help=str("Zapis do csv (stacje kolejno, po jednej na linię - czas zapisywany dla każdego odczytu z osobna), wpisz początek nazwy pliku i liczbę zapisów na wolumen (domyślnie %s); zapis wielowolumenowy wg ilości zapisów" % defwvc))
	argzapisu.add_argument("-wcrvc", "--writetocsvrazmulticountvolumefile", type=str, action="append", nargs=2, 
		help=str("Zapis do csv (wszystkie stacje naraz, w jednej linii - czas zapisywany jednorazowo dla całej serii odczytów), wpisz początek nazwy pliku i liczbę zapisów na wolumen (domyślnie %s); zapis wielowolumenowy wg ilości zapisów" % defwvc))
	# argzapisu.add_argument("-wvc", "--writemultivolumeentrycount", type=int, action="store_true", 
	#	help="Parametr opcjonalny zapisu wielowolumenowego: ilość wpisów na jeden plik"
	argzapisu.add_argument("-wn", "--writeno", action="store_true", help="Nie zapisuj")
	arggetu.add_argument("-gj", "--getjednoczesnie", action="store_true", help="Pobieraj jednocześnie")
	arggetu.add_argument("-gk", "--getkolejno", action="store_true", help="Pobieraj kolejno bez odstępu czasowego")
	arggetu.add_argument("-gkw", "--getkolejnowait", type=int,
		help="Pobieraj kolejno z odstępem czasowym pomiędzy odczytami pojedyńczych stacji")
	arggetu.add_argument("-gd", "--getdef", action="store_true", help="Pobieraj w trybie domyślnym")
	argh.add_argument("-in", "--instantly", action="store_true",
		help="Wyświetlaj oraz zapisuj natychmiast po pobraniu informacji, równoważne z -iw oraz -id")
	argh.add_argument("-iw", "--instawrite", action="store_true",
		help="Zapisuj natycmiast po pobraniu informacji., konieczny tryb wyświetlania pojedyńczego")
	argh.add_argument("-id", "--instadisp", action="store_true",
		help="Wyświetlaj natychmiast po pobraniu informacji, konieczny tryb wyświetlania pojedyńczego")
	argh.add_argument("-tor", "--tor", action="store_true", help="Pobieraj za pośrednictwem sieci Tor (wymaga stem)")
	parmetry = argh.parse_args()
	return parmetry
