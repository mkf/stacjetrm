class klasa1:
    'To jest klasa1'
    
    def __init__(self, skund, stacyjka):
        self.skund = skund
        self.stacyjka = stacyjka
        odnaleziono = re.search(r'w na stacji.*szt', skund, re.S)
        wynalezione = odnaleziono.group()
        odnalezione = str(wynalezione)
        stacjowystring = re.sub(r'\D',"",stacyjka)
        stacja = int(stacjowystring)
        #comaszukac = slowniczekkoncowek[plik] + szt
        comaszukac = 'th.*szt'
        renaleziono = re.search(comaszukac, odnalezione, re.S)
        renalezione = renaleziono.group()
        #reodnalezione = renalezione.group
        reodnalezione = re.sub(r'built-in method group of ',"",renalezione)
        #wlasciwie, to ten powyzszy re.sub jest zbedny, ale nic nie robi jesli tego built[...] nie ma, wiec niech ju
        rowerki = re.sub(r'\D',"",reodnalezione)
        rowery = int(rowerki)
        #stacjinazwa = re.sub(r'.jsp',"",plik)
        stacjinazwa = stacyja

