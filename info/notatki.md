- klasa listująca powinna sama brać czas unixowy, 
czas lokalny i datę lokalną
 
- później trza będzie zrobić też opcję pobierania 'jak kolejno, acz jednoczesnie', która będzie pobierała jednocześnie acz wyświelała w interfejsie kolejno, przy czym każde pobranie będzie miało swój waitbetweenloopsstamp
- mimo wielowątkowości, oczywistym jest, że część wątków wykona swoje zadanie szybciej od innych. W związku z tym ich wyni powinien iść dalej od razu, i nie czekać na resztę
- to trzeba będzie przepisać do Github Issues i potytułować po jednym
- mniej istotną jest możliwość odpalenia trybu kolejno w stylu jak jednocześnie
- później zrobi się konwerter danych zebranych kolejno do danych zebranych jednocześnie
- również jest jeszcze kwestia zapisu do wielu celów, do wielu plików/baz danych jednocześnie, przy dwóch różnych trybach
- możliwe musi być jednoczesne zapisywanie zupełnie odmiennymi we wszystkim trybami do wielu różnych plików i baz danych jednocześnie
- przepisać powyższe do GitHub Issues


