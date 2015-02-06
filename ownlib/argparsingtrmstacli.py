# -*- coding: utf-8 -*-
#TODO: Fix error when trying --help
def argparsowanie(defwvt,defwvc):
	import argparse
	argh = argparse.ArgumentParser()

	arglang = argh.add_mutually_exclusive_group()
	argchar = argh.add_mutually_exclusive_group()
	argwaitbetweenloops = argh.add_mutually_exclusive_group()
	argstac = argh.add_mutually_exclusive_group()
	argpracy = argh.add_mutually_exclusive_group()
	argdebugu = argh.add_mutually_exclusive_group()
	argzapisu = argh  # .add_mutually_exclusive_group()
	argadrlang = argh.add_mutually_exclusive_group()
	argvolumeny = argh.add_mutually_exclusive_group()
	arggetu = argh.add_mutually_exclusive_group()

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

	argadrlang.add_argument("-al", "--adrlanglocal", action="store_true",help="Adresy w języku lokalnym (polskim), dotyczy trybów wyświetlania(pracy) z adresami")
	argadrlang.add_argument("-ac", "--adrlangchosen",action="store_true",help="Adresy w wybranym języku, dotyczy trybów wyświetlania(pracy) z adresami")

	argpracy.add_argument("-pf", "--pracyfull", action="store_true",help="Interfejs pełny z przedzieleniem na pętli i adresami")
	argpracy.add_argument("-pr", "--pracyrazem", action="store_true",help="Interfejs pełny tabelowy, wszystkie stacje w jednej linii")
	argpracy.add_argument("-pl", "--pracylong", action="store_true", help="Interfejs pełny z przedzieleniem na pętli")
	argpracy.add_argument("-pu", "--pracyuser", action="store_true", help="Interfejs pełny ciągły")
	argpracy.add_argument("-pa", "--pracyadres", action="store_true",help="Interfejs pełny z adresami")
	argpracy.add_argument("-pt", "--pracytabela", action="store_true", help="Interfejs tabeli z adresami")
	argpracy.add_argument("-pk", "--pracykomp", action="store_true", help="Interfejs programowy")
	argpracy.add_argument("-pc", "--pracycompressed", action="store_true",help="Interfejs programowy czasUNIX,jedno- lub dwu cyfrowy numer stacji, liczba rowerów")
	argpracy.add_argument("-pm", "--pracyminim", action="store_true", help="Interfejs programowy minimalistyczny")
	argpracy.add_argument("-prk", "--pracyrazkomp", action="store_true",help="Interfejs programowy, wszystkie stacje naraz")
	argpracy.add_argument("-pn", "--pracynone", action="store_true", help="Interfejs bez danych na stdout")
	argpracy.add_argument("-pd", "--pracydef", action="store_true", help="Opcja domyślna trybu pracy")

	argdebugu.add_argument("-bf", "--debugfull", action="store_true", help="Debug pełny")
	argdebugu.add_argument("-by", "--debugyes", action="store_true", help="Debug częściowy")
	argdebugu.add_argument("-bn", "--debugno", action="store_true", help="Debug wyłączony")
	argdebugu.add_argument("-bd", "--debugdef", action="store_true", help="Domyślne opcje debugu")

	#argvolumeny.add_argument("-vs","--singlefile",action="store_true",help="Zapis do pojedyńczego pliku, bez podziału na wolumeny")
	#argvolumeny.add_argument("-vt","--volumesbytime",type=float,help="Zapis z podziałem na wolumeny wg czasu: podaj liczbę godzin pomiędzy podziałami (może być ułamek)")
	#argvolumeny.add_argument("-vc","--volumesbycount",type=int,help="Zapis z podziałem na wolumeny wg ilości wpisów: podaj próg podziału")

	argzapisu.add_argument("-wcksf","--writetocsvkolsinglefile",type=str,nargs=2,action="append",help="Zapis do csv (stacje kolejno, po jednej na linię - czas zapisywany dla każdego odczytu z osobna), do pojedyńczego pliku, bez podziału na wolumeny,wpisz nazwę pliku")
	argzapisu.add_argument("-wcrsf", "--writetocsvrazsinglefile", type=str, nargs=2,action="append",help="Zapis do csv (wszystkie stacje naraz, w jednej linii - czas zapisywany jednorazowo dla całej serii odczytów), do pojedyńczego pliku, bez podziału na wolumeny,wpisz nazwę pliku")

	argzapisu.add_argument("-wckvt","--writetocsvkolvolumesbytime",type=str,nargs=2,action="append",help="Zapis do csv (stacje kolejno, po jednej na linię - czas zapisywany dla każdego odczytu z osobna), zapis z podziałem na wolumeny wg czasu: podaj liczbę godzin pomiędzy podziałami (może być ułamek),wpisz nazwę pliku")
	argzapisu.add_argument("-wcrvt", "--writetocsvrazvolumesbytime", type=str, nargs=2,action="append",help="Zapis do csv (wszystkie stacje naraz, w jednej linii - czas zapisywany jednorazowo dla całej serii odczytów), zapis z podziałem na wolumeny wg czasu: podaj liczbę godzin pomiędzy podziałami (może być ułamek),wpisz nazwę pliku")

	argzapisu.add_argument("-wckvc","--writetocsvkolvolumesbycount",type=str,nargs=2,action="append",help="Zapis do csv (stacje kolejno, po jednej na linię - czas zapisywany dla każdego odczytu z osobna), zapis z podziałem na wolumeny wg ilości wpisów: podaj próg podziału,wpisz nazwę pliku")
	argzapisu.add_argument("-wcrvc", "--writetocsvrazvolumesbycount", type=str, nargs=2,action="append",help="Zapis do csv (wszystkie stacje naraz, w jednej linii - czas zapisywany jednorazowo dla całej serii odczytów), zapis z podziałem na wolumeny wg ilości wpisów: podaj próg podziału,wpisz nazwę pliku")

	argzapisu.add_argument("-wn", "--writeno", action="store_true", help="Nie zapisuj")

	arggetu.add_argument("-gj", "--getjednoczesnie", action="store_true", help="Pobieraj jednocześnie")
	arggetu.add_argument("-gk", "--getkolejno", action="store_true", help="Pobieraj kolejno bez odstępu czasowego")
	arggetu.add_argument("-gkw", "--getkolejnowait", type=int, help="Pobieraj kolejno z odstępem czasowym pomiędzy odczytami pojedyńczych stacji (podaj w sekundach)")
	arggetu.add_argument("-gd", "--getdef", action="store_true", help="Pobieraj w trybie domyślnym")

	argh.add_argument("-in", "--instantly", action="store_true", help="Wyświetlaj oraz zapisuj natychmiast po pobraniu informacji, równoważne z -iw oraz -id")
	argh.add_argument("-iw", "--instawrite", action="store_true",help="Zapisuj natycmiast po pobraniu informacji., konieczny tryb wyświetlania pojedyńczego")
	argh.add_argument("-id", "--instadisp", action="store_true",help="Wyświetlaj natychmiast po pobraniu informacji, konieczny tryb wyświetlania pojedyńczego")

	parmetry = argh.parse_args()
	return parmetry